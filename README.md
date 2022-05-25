# SHAP-in-repeated-nested-CV


This repository contains the algorithm used in study [1].
Briefly, we computed average SHAP values inside a repeated nested cross-validation procedure, for trainining and test sets separately.

## Datasets

To prove the utility of computing the SHAP values in repeated nCV, in this study, we considered two regression and one classification task for age prediction using features of brain complexity extracted from MRI data. In particular, we used the high-resolution public and international T$_1$-weigthed datasets of healthy children and adolescents [Nathan Kline Institute (NKI)—Rockland Sample Pediatric Multimodal Imaging Test–Retest Sample—NKI2 dataset](https://fcon_1000.projects.nitrc.org/indi/CoRR/html/nki_2.html) and adults [International Consortium for Brain Mapping (ICBM) dataset]( https://fcon_1000.projects.nitrc.org/fcpClassic/FcpTable.html). Briefly, the NKI2 dataset comprises MRI examinations of 73 healthy pediatric subjects aged 6 to 17 years (43 males and 30 females, age 11.8 ± 3.1 years, mean ± standard deviation). The ICBM dataset comprises MRI examinations of 86 healthy adult and elderly subjects ranging from 19 to 85 years (41 males and 45 females, age 44.2 ± 17.1 years). For classification purposes, we also considered a dichotomous task defined for ICBM subjects as the prediction of a young group (age $\leq$ 30 years) with 25 samples (9 males and 16 females, 22.6 ± 3.3 years) vs. an elder group (age $\geq$ 56 years) with 28 samples (11 males and 17 females, 64.9 ± 8.2 years)


## Structure of the Repository
This repository contains 3 explanatory notebooks for experimental tests of our study.
You can run them in Google Colab