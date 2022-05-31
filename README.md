# SHAP-in-repeated-nested-CV


This repository contains the algorithm used in study [1].
Briefly, we computed representative [SHAP](https://shap.readthedocs.io/en/latest/index.html) values [2] inside a repeated nested cross-validation procedure, for training and test sets separately.


| Representative SHAP values for the training set | Representative SHAP values for the test set |
|:----------------:|:--------------------:|
|<img src="https://github.com/Imaging-AI-for-Health-virtual-lab/SHAP-in-repeated-nested-CV/blob/main/regression_ICBM/average_plots/train.png" alt="drawing" width="500"/>| <img src="https://github.com/Imaging-AI-for-Health-virtual-lab/SHAP-in-repeated-nested-CV/blob/main/regression_ICBM/average_plots/test.png" alt="drawing" width="500"/>| 
 


## Datasets

To prove the utility of computing the SHAP values in repeated nCV, in this study, we considered two regression and one classification task for age prediction using features of brain complexity extracted from MRI data [3]. In particular, we used the high-resolution public and international T$_1$-weigthed datasets of healthy children and adolescents [Nathan Kline Institute (NKI)—Rockland Sample Pediatric Multimodal Imaging Test–Retest Sample—NKI2 dataset](https://fcon_1000.projects.nitrc.org/indi/CoRR/html/nki_2.html) and adults [International Consortium for Brain Mapping (ICBM) dataset]( https://fcon_1000.projects.nitrc.org/fcpClassic/FcpTable.html). Briefly, the NKI2 dataset comprises MRI examinations of 73 healthy pediatric subjects aged 6 to 17 years (43 males and 30 females, age 11.8 ± 3.1 years, mean ± standard deviation). The ICBM dataset comprises MRI examinations of 86 healthy adult and elderly subjects ranging from 19 to 85 years (41 males and 45 females, age 44.2 ± 17.1 years). For classification purposes, we also considered a dichotomous task defined for ICBM subjects as the prediction of a young group (age $\leq$ 30 years) with 25 samples (9 males and 16 females, 22.6 ± 3.3 years) vs. an elder group (age $\geq$ 56 years) with 28 samples (11 males and 17 females, 64.9 ± 8.2 years)


## Structure of the Repository
This repository contains 3 explanatory notebooks for experimental tests of our study:
- [`regression_NKI2.ipynb`](https://github.com/Imaging-AI-for-Health-virtual-lab/SHAP-in-repeated-nested-CV/blob/main/regression_NKI2.ipynb)
- [`regression_ICBM.ipynb`](https://github.com/Imaging-AI-for-Health-virtual-lab/SHAP-in-repeated-nested-CV/blob/main/regression_ICBM.ipynb)
- [`classification_ICBM.ipynb`](https://github.com/Imaging-AI-for-Health-virtual-lab/SHAP-in-repeated-nested-CV/blob/main/classification_ICBM.ipynb)



Each notebook produces a directory output with the results of the experiment (e.g. `classification_ICBM/`). In each results' directory there are other 3 directories:
- `Shap_values/` : which contains `.pkl` files of SHAP values for each fold of the nested cross-validation, for both training and test sets;
-   `plots/` : which contains beeswarm and bar plots of each fold of the nested cross-validation, for both training and test sets;
- `average plots/` : which contains beeswam and bar plots of averaged SHAP values over the folds and repetitions.

Directory `data/` contains two `.xlsx` files containing data: `NKI2_session1_data.xlsx` and `ICBM_data.xlsx`.
The file `utils.py` contains some functions including `average_shap_values()` which takes in input the `.pkl` files of SHAP values and makes an average.


```
.
├── requirements.txt
├── utils.py
├── classification_ICBM.ipynb
├── regression_ICBM.ipynb
├── regression_NKI2.ipynb
├── README.md
├── data/
│   ├── ICBM_data.xlsx
│   └── NKI2_session1_data.xlsx
├── classification_ICBM/
│   ├── average_plots/
│   │   ├── bar_test.png
│   │   ├── bar_train.png
│   │   ├── test.png
│   │   ├── train.png
│   │   └── XGBoost_ROCcurve.png
│   ├── plots/
│   │   ├── summary_plot_shap_0_0.png
│   │   ├──--------------------------
│   │   ├──--------------------------
│   │   └── summary_plot_shap_1_4.png
│   ├── roc_aucs.csv
│   └── Shap_values/
│       ├── train0fold0.pkl
│       ├── train0fold1.pkl
│       ├──---------------
│       ├──---------------
│       └── test1fold4.pkl
├── regression_ICBM/
│   ├── average_plots/
│   │   ├── bar_test.png
│   │   ├── bar_train.png
│   │   ├── test.png
│   │   └── train.png
│   ├── plots/
│   │   ├── test_summary_bar_plot_shap_0_0.png
│   │   ├── test_summary_bar_plot_shap_0_1.png
│   │   ├── train_summary_bar_plot_shap_0_0.png
│   │   ├── train_summary_bar_plot_shap_0_1.png
│   │   ├──------------------------------------
│   │   ├──------------------------------------
│   │   ├──------------------------------------
│   │   └── train_summary_bar_plot_shap_2_4.png
│   └── Shap_values/
│       ├── train0fold0.pkl
│       ├── train0fold1.pkl
│       ├──---------------
│       ├──---------------
│       └── test1fold4.pkl
└──  regression_NKI2/
│    ├── average_plots/
│    │   ├──------------------------------------
│    │   └──------------------------------------
│    ├── plots/
│    │   ├──------------------------------------
│    │   └──------------------------------------
│    └── Shap_values/
│        ├──------------------------------------
└──      └── -----------------------------------
```

## Usage
You can run the 3 notebooks in Google Colab. To reproduce the exact results of our study, please change the value of `num_trials` to 100 inside the notebooks, which is the number of repetitions for the nested cross-validation.

## References
1. 
2. Lundberg, Scott M., and Su-In Lee. "A unified approach to interpreting model predictions." Advances in neural information processing systems 30 (2017).
3. Marzi, C.; Giannelli, M.; Tessa, C.; Mascalchi, M.; Diciotti, S. Toward a more reliable characterization of fractal properties of the
cerebral cortex of healthy subjects during the lifespan. Scientific Reports 2020, 10, 16957. [](https://doi.org/10.1038/s41598-020-73961-w).
