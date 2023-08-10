# Introduction

This is a simple example of parallel processing using rxpy in python.

`python src/main.py` to run the example.

```bash
practice-rxpy-jPR28GGN-py3.11 ❯ python src/index.py

[15:26:21][MainThread] CPU count is 12
[15:26:24][ThreadPoolExecutor-0_0] passnger id 1 ~ 20 - MFFFMMMMFFFFMMFFMMFF
[15:26:24][ThreadPoolExecutor-0_1] passnger id 21 ~ 40 - MMFMFFMMFMMFFMMMMMFF
[15:26:24][ThreadPoolExecutor-0_2] passnger id 41 ~ 60 - FFMFFMMFMFMMFFMMFMFM
[15:26:24][ThreadPoolExecutor-0_3] passnger id 61 ~ 80 - MFMMMMFMFMMFMMMMMMMF
[15:26:24][ThreadPoolExecutor-0_4] passnger id 81 ~ 100 - MMFMFFMMFMMMMMMMMMFM
[15:26:24][ThreadPoolExecutor-0_5] passnger id 101 ~ 120 - FMMMMMFMMFMFMFFMMMMF
[15:26:24][ThreadPoolExecutor-0_6] passnger id 121 ~ 140 - MMMFMMMMFMMMFFMMFMMM
[15:26:24][ThreadPoolExecutor-0_7] passnger id 141 ~ 160 - FFFMMMMFMMMFMMMMFMMM
[15:26:24][ThreadPoolExecutor-0_8] passnger id 161 ~ 180 - MFMMMMFFMMMMFMMMMFMM
[15:26:24][ThreadPoolExecutor-0_9] passnger id 181 ~ 200 - FMMMFMFMMMFMFMFFMMFF
[15:26:24][ThreadPoolExecutor-0_10] passnger id 201 ~ 220 - MMMMMFMMFMMFMMMFFMFM
[15:26:24][ThreadPoolExecutor-0_11] passnger id 221 ~ 240 - MMMMMMMMMFFMMFMFMFMM
[15:26:27][ThreadPoolExecutor-0_0] passnger id 241 ~ 260 - FFMMMMFFMMMFMMFFFFFF
[15:26:27][ThreadPoolExecutor-0_1] passnger id 261 ~ 280 - MMMMFMMMFFMMFMFFFMMF
[15:26:27][ThreadPoolExecutor-0_2] passnger id 281 ~ 300 - MMMMMMMMMFFFMFMMMFMF
[15:26:27][ThreadPoolExecutor-0_3] passnger id 301 ~ 320 - FMMFMMFFMFFFFMMFFMFF
[15:26:27][ThreadPoolExecutor-0_4] passnger id 321 ~ 340 - MMFFMFMFFFFMMMFMMFMM
[15:26:27][ThreadPoolExecutor-0_5] passnger id 341 ~ 360 - MFMMMFFFMMMMMMMMFFFF
[15:26:27][ThreadPoolExecutor-0_6] passnger id 361 ~ 380 - MMFMMMFFFFMMMMFFFMMM
[15:26:27][ThreadPoolExecutor-0_7] passnger id 381 ~ 400 - FFMFMMMFMFMMMFFMFMMF
[15:26:27][ThreadPoolExecutor-0_8] passnger id 401 ~ 420 - MMFMFMMMMFMMFMMFFFMF
[15:26:27][ThreadPoolExecutor-0_9] passnger id 421 ~ 440 - MMMFMMFFMMMFFMMFFFMM
[15:26:27][ThreadPoolExecutor-0_10] passnger id 441 ~ 460 - FMMFMMFMFMMMMMMMMFFM
[15:26:27][ThreadPoolExecutor-0_11] passnger id 461 ~ 480 - MMMMMMMMMFMMFFFMMMMF
[15:26:30][ThreadPoolExecutor-0_0] passnger id 481 ~ 500 - MMMFMFFMMMMMMMMMFMFM
[15:26:30][ThreadPoolExecutor-0_1] passnger id 501 ~ 520 - MFFFFMFMMMMMMFMMFMFM
[15:26:30][ThreadPoolExecutor-0_2] passnger id 521 ~ 540 - FMMFMMFMMMFMMFFFMFMF
[15:26:30][ThreadPoolExecutor-0_3] passnger id 541 ~ 560 - FFFMMMFMMMMMMMFMFMFF
[15:26:30][ThreadPoolExecutor-0_4] passnger id 561 ~ 580 - MMMMFMMFMMMFMFMMFFFM
[15:26:30][ThreadPoolExecutor-0_5] passnger id 581 ~ 600 - FFMMMFMMMMMFMFMMFMMM
[15:26:30][ThreadPoolExecutor-0_6] passnger id 601 ~ 620 - FMMMMMMMFFFMFMMFMFFM
[15:26:30][ThreadPoolExecutor-0_7] passnger id 621 ~ 640 - MMMMMMMFMMMMMMFFMMFM
[15:26:30][ThreadPoolExecutor-0_8] passnger id 641 ~ 660 - MFFMFMMMMFMFMFFMMFMM
[15:26:30][ThreadPoolExecutor-0_9] passnger id 661 ~ 680 - MMMMMMMMMFFMMMMMMFFM
[15:26:30][ThreadPoolExecutor-0_10] passnger id 681 ~ 700 - FMMMMMMMMFMFMMMMMFMM
[15:26:30][ThreadPoolExecutor-0_11] passnger id 701 ~ 720 - FMFMMMFMFMFMMMMMFFMM
[15:26:33][ThreadPoolExecutor-0_0] passnger id 721 ~ 740 - FMMMMMFFMFFMMMMMFMMM
[15:26:33][ThreadPoolExecutor-0_1] passnger id 741 ~ 760 - MMFMMMMFMMFMMMFMMMMF
[15:26:33][ThreadPoolExecutor-0_2] passnger id 761 ~ 780 - MMMFMFMFMMMMFMFMMFMF
[15:26:33][ThreadPoolExecutor-0_3] passnger id 781 ~ 800 - FFMMMMFMMMMMFMMMFFMF
[15:26:33][ThreadPoolExecutor-0_4] passnger id 801 ~ 820 - MFMMMMMFMFMMMFMMFMMM
[15:26:33][ThreadPoolExecutor-0_5] passnger id 821 ~ 840 - FMMFMMMMMFFMMMMFMMMM
[15:26:33][ThreadPoolExecutor-0_6] passnger id 841 ~ 860 - MMFMMMMMMFMMFFFFFMFM
[15:26:33][ThreadPoolExecutor-0_7] passnger id 861 ~ 880 - MMFFMFFMMMMFMMFFMMMF
[15:26:33][ThreadPoolExecutor-0_8] passnger id 881 ~ 891 - FMFMMFMFFMM
[
```

using 12 threads, each thread processes a chunk over 3 seconds.
