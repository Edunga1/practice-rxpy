# Introduction

This is a simple example of parallel processing using rxpy in python.

`python src/main.py` to run the example.

```bash
practice-rxpy-jPR28GGN-py3.11 ❯ python src/index.py

[MainThread] CPU count is 12
[ThreadPoolExecutor-0_0] passnger id 1 ~ 20 - MFFFMMMMFFFFMMFFMMFF
[ThreadPoolExecutor-0_1] passnger id 21 ~ 40 - MMFMFFMMFMMFFMMMMMFF
[ThreadPoolExecutor-0_2] passnger id 41 ~ 60 - FFMFFMMFMFMMFFMMFMFM
[ThreadPoolExecutor-0_3] passnger id 61 ~ 80 - MFMMMMFMFMMFMMMMMMMF
[ThreadPoolExecutor-0_4] passnger id 81 ~ 100 - MMFMFFMMFMMMMMMMMMFM
[ThreadPoolExecutor-0_5] passnger id 101 ~ 120 - FMMMMMFMMFMFMFFMMMMF
[ThreadPoolExecutor-0_6] passnger id 121 ~ 140 - MMMFMMMMFMMMFFMMFMMM
[ThreadPoolExecutor-0_7] passnger id 141 ~ 160 - FFFMMMMFMMMFMMMMFMMM
[ThreadPoolExecutor-0_8] passnger id 161 ~ 180 - MFMMMMFFMMMMFMMMMFMM
[ThreadPoolExecutor-0_9] passnger id 181 ~ 200 - FMMMFMFMMMFMFMFFMMFF
[ThreadPoolExecutor-0_10] passnger id 201 ~ 220 - MMMMMFMMFMMFMMMFFMFM
[ThreadPoolExecutor-0_11] passnger id 221 ~ 240 - MMMMMMMMMFFMMFMFMFMM
[ThreadPoolExecutor-0_0] passnger id 241 ~ 260 - FFMMMMFFMMMFMMFFFFFF
[ThreadPoolExecutor-0_1] passnger id 261 ~ 280 - MMMMFMMMFFMMFMFFFMMF
[ThreadPoolExecutor-0_2] passnger id 281 ~ 300 - MMMMMMMMMFFFMFMMMFMF
[ThreadPoolExecutor-0_3] passnger id 301 ~ 320 - FMMFMMFFMFFFFMMFFMFF
[ThreadPoolExecutor-0_4] passnger id 321 ~ 340 - MMFFMFMFFFFMMMFMMFMM
[ThreadPoolExecutor-0_5] passnger id 341 ~ 360 - MFMMMFFFMMMMMMMMFFFF
[ThreadPoolExecutor-0_6] passnger id 361 ~ 380 - MMFMMMFFFFMMMMFFFMMM
[ThreadPoolExecutor-0_7] passnger id 381 ~ 400 - FFMFMMMFMFMMMFFMFMMF
[ThreadPoolExecutor-0_8] passnger id 401 ~ 420 - MMFMFMMMMFMMFMMFFFMF
[ThreadPoolExecutor-0_9] passnger id 421 ~ 440 - MMMFMMFFMMMFFMMFFFMM
[ThreadPoolExecutor-0_10] passnger id 441 ~ 460 - FMMFMMFMFMMMMMMMMFFM
[ThreadPoolExecutor-0_11] passnger id 461 ~ 480 - MMMMMMMMMFMMFFFMMMMF
[ThreadPoolExecutor-0_0] passnger id 481 ~ 500 - MMMFMFFMMMMMMMMMFMFM
[ThreadPoolExecutor-0_1] passnger id 501 ~ 520 - MFFFFMFMMMMMMFMMFMFM
[ThreadPoolExecutor-0_2] passnger id 521 ~ 540 - FMMFMMFMMMFMMFFFMFMF
[ThreadPoolExecutor-0_3] passnger id 541 ~ 560 - FFFMMMFMMMMMMMFMFMFF
[ThreadPoolExecutor-0_4] passnger id 561 ~ 580 - MMMMFMMFMMMFMFMMFFFM
[ThreadPoolExecutor-0_5] passnger id 581 ~ 600 - FFMMMFMMMMMFMFMMFMMM
[ThreadPoolExecutor-0_6] passnger id 601 ~ 620 - FMMMMMMMFFFMFMMFMFFM
[ThreadPoolExecutor-0_7] passnger id 621 ~ 640 - MMMMMMMFMMMMMMFFMMFM
[ThreadPoolExecutor-0_8] passnger id 641 ~ 660 - MFFMFMMMMFMFMFFMMFMM
[ThreadPoolExecutor-0_9] passnger id 661 ~ 680 - MMMMMMMMMFFMMMMMMFFM
[ThreadPoolExecutor-0_10] passnger id 681 ~ 700 - FMMMMMMMMFMFMMMMMFMM
[ThreadPoolExecutor-0_11] passnger id 701 ~ 720 - FMFMMMFMFMFMMMMMFFMM
[ThreadPoolExecutor-0_0] passnger id 721 ~ 740 - FMMMMMFFMFFMMMMMFMMM
[ThreadPoolExecutor-0_1] passnger id 741 ~ 760 - MMFMMMMFMMFMMMFMMMMF
[ThreadPoolExecutor-0_2] passnger id 761 ~ 780 - MMMFMFMFMMMMFMFMMFMF
[ThreadPoolExecutor-0_3] passnger id 781 ~ 800 - FFMMMMFMMMMMFMMMFFMF
[ThreadPoolExecutor-0_4] passnger id 801 ~ 820 - MFMMMMMFMFMMMFMMFMMM
[ThreadPoolExecutor-0_5] passnger id 821 ~ 840 - FMMFMMMMMFFMMMMFMMMM
[ThreadPoolExecutor-0_6] passnger id 841 ~ 860 - MMFMMMMMMFMMFFFFFMFM
[ThreadPoolExecutor-0_7] passnger id 861 ~ 880 - MMFFMFFMMMMFMMFFMMMF
[ThreadPoolExecutor-0_8] passnger id 881 ~ 891 - FMFMMFMFFMM
[ThreadPoolExecutor-0_8] total count is 891
```

using 12 threads, each thread processes a chunk over 3 seconds.
