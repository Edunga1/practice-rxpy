import csv
import multiprocessing
import time
from threading import current_thread
from datetime import datetime

import rx
from rx import operators as ops
from rx.scheduler.threadpoolscheduler import ThreadPoolScheduler


def print_t(it):
    ts = datetime.now().strftime('%H:%M:%S')
    print(f'[{ts}][{current_thread().name}] {it}')


# thread pool
thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)
print_t('CPU count is {0}'.format(thread_count))


def load_data():
    data = []
    with open('src/train.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'id': row['PassengerId'],
                'name': row['Name'],
                'sex': row['Sex'],
            })
    return data


def chunk(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]


def apply_delay(x):
    time.sleep(3)
    return x


def print_passnger_sex(items):
    min_id = items[0]['id']
    max_id = items[-1]['id']
    genders = [x['sex'][0].upper() for x in items]
    print_t(f'passnger id {min_id} ~ {max_id} - {"".join(genders)}')


def main():
    data = load_data()

    rx.from_iterable(data).pipe(
        # group by X
        ops.buffer_with_count(20),

        # wait for 3 seconds
        ops.flat_map(lambda x: rx.from_callable(
            lambda: apply_delay(x),
            scheduler=thread_pool_scheduler,
        )),

        # some operation to process data
        ops.do_action(on_next=print_passnger_sex),

        # sum
        ops.map(lambda x: len(x)),
        ops.sum(),
        ops.do_action(on_next=lambda x: print_t(f'total count is {x}'))
    ).run()


if __name__ == "__main__":
    main()
