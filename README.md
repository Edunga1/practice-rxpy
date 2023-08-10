# Introduction

This is a simple example of parallel processing using rxpy in python.

`python src/main.py` to run the example.

```bash
practice-rxpy-jPR28GGN-py3.11 ❯ python src/index.py
[15:29:59][MainThread] CPU count is 12
[15:30:02][ThreadPoolExecutor-0_0] passenger id 1 ~ 20 - MFFFMMMMFFFFMMFFMMFF
[15:30:02][ThreadPoolExecutor-0_1] passenger id 21 ~ 40 - MMFMFFMMFMMFFMMMMMFF
[15:30:02][ThreadPoolExecutor-0_3] passenger id 61 ~ 80 - MFMMMMFMFMMFMMMMMMMF
[15:30:02][ThreadPoolExecutor-0_2] passenger id 41 ~ 60 - FFMFFMMFMFMMFFMMFMFM
[15:30:02][ThreadPoolExecutor-0_4] passenger id 81 ~ 100 - MMFMFFMMFMMMMMMMMMFM
[15:30:02][ThreadPoolExecutor-0_5] passenger id 101 ~ 120 - FMMMMMFMMFMFMFFMMMMF
[15:30:02][ThreadPoolExecutor-0_6] passenger id 121 ~ 140 - MMMFMMMMFMMMFFMMFMMM
[15:30:02][ThreadPoolExecutor-0_7] passenger id 141 ~ 160 - FFFMMMMFMMMFMMMMFMMM
[15:30:02][ThreadPoolExecutor-0_8] passenger id 161 ~ 180 - MFMMMMFFMMMMFMMMMFMM
[15:30:02][ThreadPoolExecutor-0_9] passenger id 181 ~ 200 - FMMMFMFMMMFMFMFFMMFF
[15:30:02][ThreadPoolExecutor-0_10] passenger id 201 ~ 220 - MMMMMFMMFMMFMMMFFMFM
[15:30:02][ThreadPoolExecutor-0_11] passenger id 221 ~ 240 - MMMMMMMMMFFMMFMFMFMM
[15:30:05][ThreadPoolExecutor-0_0] passenger id 241 ~ 260 - FFMMMMFFMMMFMMFFFFFF
[15:30:05][ThreadPoolExecutor-0_1] passenger id 261 ~ 280 - MMMMFMMMFFMMFMFFFMMF
[15:30:05][ThreadPoolExecutor-0_3] passenger id 281 ~ 300 - MMMMMMMMMFFFMFMMMFMF
[15:30:05][ThreadPoolExecutor-0_2] passenger id 301 ~ 320 - FMMFMMFFMFFFFMMFFMFF
[15:30:05][ThreadPoolExecutor-0_4] passenger id 321 ~ 340 - MMFFMFMFFFFMMMFMMFMM
[15:30:05][ThreadPoolExecutor-0_5] passenger id 341 ~ 360 - MFMMMFFFMMMMMMMMFFFF
[15:30:05][ThreadPoolExecutor-0_6] passenger id 361 ~ 380 - MMFMMMFFFFMMMMFFFMMM
[15:30:05][ThreadPoolExecutor-0_7] passenger id 381 ~ 400 - FFMFMMMFMFMMMFFMFMMF
[15:30:05][ThreadPoolExecutor-0_8] passenger id 401 ~ 420 - MMFMFMMMMFMMFMMFFFMF
[15:30:05][ThreadPoolExecutor-0_9] passenger id 421 ~ 440 - MMMFMMFFMMMFFMMFFFMM
[15:30:05][ThreadPoolExecutor-0_10] passenger id 441 ~ 460 - FMMFMMFMFMMMMMMMMFFM
[15:30:05][ThreadPoolExecutor-0_11] passenger id 461 ~ 480 - MMMMMMMMMFMMFFFMMMMF
[15:30:08][ThreadPoolExecutor-0_0] passenger id 481 ~ 500 - MMMFMFFMMMMMMMMMFMFM
[15:30:08][ThreadPoolExecutor-0_1] passenger id 501 ~ 520 - MFFFFMFMMMMMMFMMFMFM
[15:30:08][ThreadPoolExecutor-0_3] passenger id 521 ~ 540 - FMMFMMFMMMFMMFFFMFMF
[15:30:08][ThreadPoolExecutor-0_2] passenger id 541 ~ 560 - FFFMMMFMMMMMMMFMFMFF
[15:30:08][ThreadPoolExecutor-0_4] passenger id 561 ~ 580 - MMMMFMMFMMMFMFMMFFFM
[15:30:08][ThreadPoolExecutor-0_5] passenger id 581 ~ 600 - FFMMMFMMMMMFMFMMFMMM
[15:30:08][ThreadPoolExecutor-0_6] passenger id 601 ~ 620 - FMMMMMMMFFFMFMMFMFFM
[15:30:08][ThreadPoolExecutor-0_7] passenger id 621 ~ 640 - MMMMMMMFMMMMMMFFMMFM
[15:30:08][ThreadPoolExecutor-0_8] passenger id 641 ~ 660 - MFFMFMMMMFMFMFFMMFMM
[15:30:08][ThreadPoolExecutor-0_9] passenger id 661 ~ 680 - MMMMMMMMMFFMMMMMMFFM
[15:30:08][ThreadPoolExecutor-0_10] passenger id 681 ~ 700 - FMMMMMMMMFMFMMMMMFMM
[15:30:08][ThreadPoolExecutor-0_11] passenger id 701 ~ 720 - FMFMMMFMFMFMMMMMFFMM
[15:30:11][ThreadPoolExecutor-0_0] passenger id 721 ~ 740 - FMMMMMFFMFFMMMMMFMMM
[15:30:11][ThreadPoolExecutor-0_1] passenger id 741 ~ 760 - MMFMMMMFMMFMMMFMMMMF
[15:30:11][ThreadPoolExecutor-0_3] passenger id 761 ~ 780 - MMMFMFMFMMMMFMFMMFMF
[15:30:11][ThreadPoolExecutor-0_2] passenger id 781 ~ 800 - FFMMMMFMMMMMFMMMFFMF
[15:30:11][ThreadPoolExecutor-0_4] passenger id 801 ~ 820 - MFMMMMMFMFMMMFMMFMMM
[15:30:11][ThreadPoolExecutor-0_5] passenger id 821 ~ 840 - FMMFMMMMMFFMMMMFMMMM
[15:30:11][ThreadPoolExecutor-0_6] passenger id 841 ~ 860 - MMFMMMMMMFMMFFFFFMFM
[15:30:11][ThreadPoolExecutor-0_7] passenger id 861 ~ 880 - MMFFMFFMMMMFMMFFMMMF
[15:30:11][ThreadPoolExecutor-0_8] passenger id 881 ~ 891 - FMFMMFMFFMM
[15:30:11][ThreadPoolExecutor-0_8] total count is 891
```

using 12 threads, each thread processes a chunk over 3 seconds.
