# Random-Forests-and-Gradient-Boosting-for-Bankruptcy-Prediction-in-Poland-and-Taiwan
This project compares **Random Forest** and **Gradient Boosting** models for predicting corporate bankruptcy using financial data from Poland and Taiwan. It includes data preprocessing, handling class imbalance, hyperparameter tuning, model evaluation with ROC-AUC and other metrics, and saving the best-performing model using Scikit-learn.
# Random Forests and Gradient Boosting for Bankruptcy Prediction in Poland and Taiwan

## Project Summary

This repository contains a comparative machine learning study on **corporate bankruptcy prediction** using financial statement data from companies in **Poland** and **Taiwan**. The project investigates how **ensemble learning algorithms** can be used to detect early signs of financial distress and improve risk assessment.

Bankruptcy prediction is a challenging **imbalanced binary classification problem**, where the number of bankrupt firms is much smaller than the number of healthy firms. To address this, the project combines robust preprocessing techniques with oversampling strategies and evaluates model performance using metrics that are appropriate for rare-event prediction.

The study focuses on two powerful ensemble methods:

* **Random Forest (Bagging)** – provides a strong baseline and robust performance through averaging multiple decision trees.
* **Gradient Boosting (Boosting)** – sequentially improves weak learners and often achieves higher predictive accuracy.

The final outcome is a tuned Gradient Boosting model capable of producing probability estimates for bankruptcy risk, which can be used in financial risk management and credit analysis applications.

---

## Why This Project Matters

Financial institutions, investors, and regulators rely on accurate bankruptcy prediction systems to:

* identify companies at risk of default,
* reduce credit losses,
* improve lending decisions,
* monitor financial stability, and
* support early intervention strategies.

This project demonstrates how machine learning can transform raw accounting data into actionable risk signals.

---

## Datasets

The analysis uses publicly available bankruptcy datasets for **Poland** and **Taiwan**, containing financial ratios and accounting indicators such as:

* profitability ratios,
* liquidity ratios,
* leverage ratios,
* operational efficiency measures, and
* cash-flow-related variables.

The target variable is binary:

* `1` → bankrupt company
* `0` → non-bankrupt company

---

## Methodology

### 1. Data Preprocessing

* Removed invalid observations
* Handled missing values using **median imputation**
* Converted categorical features where necessary
* Performed train-test splitting with a fixed random seed for reproducibility

### 2. Handling Class Imbalance

Because bankruptcy events are rare, the minority class was oversampled in the training set so that the models could learn meaningful bankruptcy patterns without bias toward the majority class.

### 3. Model Training

#### Random Forest

* Ensemble of decision trees
* Bootstrap sampling
* Feature randomness at each split
* Used as a benchmark model

#### Gradient Boosting

* Sequential boosting of weak learners
* Optimized for probability ranking
* Tuned using **GridSearchCV** with cross-validation

### 4. Hyperparameter Tuning

The following parameters were explored:

* `n_estimators`
* `learning_rate`
* `max_depth`
* `subsample`

Model selection was based on **ROC-AUC**, which is more informative than accuracy for imbalanced datasets.

---

## Evaluation Metrics

The models were evaluated on the untouched test set using:

* **Accuracy** – overall correctness
* **Precision** – proportion of predicted bankruptcies that were correct
* **Recall** – proportion of actual bankruptcies detected
* **F1-score** – balance between precision and recall
* **ROC-AUC** – ability to rank bankrupt firms above non-bankrupt firms

A comparison table was generated to identify the best-performing model across both countries.

---

## Key Findings

* Ensemble methods significantly outperform single decision trees.
* Gradient Boosting generally achieves the highest ROC-AUC after tuning.
* Oversampling improves recall, allowing the model to detect more bankrupt firms.
* The tuned boosting model provides a better balance between precision and recall, making it more suitable for real-world financial risk assessment.

---

## Repository Structure

```text
├── data/                      # Raw and processed datasets
├── notebooks/                 # Jupyter notebooks for analysis and modeling
├── models/                    # Saved trained models
│   └── poland_gradient_boosting.pkl
├── src/                       # Reusable Python scripts and helper functions
├── figures/                   # ROC curves, confusion matrices, and feature plots
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## Reproducibility

Clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/bankruptcy-prediction.git
cd bankruptcy-prediction
pip install -r requirements.txt
```

Run the notebooks in order to reproduce the preprocessing, training, tuning, and evaluation pipeline.

---

## Skills Demonstrated

This project showcases:

* **Machine Learning** (Random Forest, Gradient Boosting, GridSearchCV)
* **Statistical Thinking** (evaluation of imbalanced classifiers)
* **Data Preprocessing** (imputation, encoding, train-test splitting)
* **Model Validation** (cross-validation, ROC-AUC optimization)
* **Python Programming** (Pandas, NumPy, Scikit-learn)
* **Model Deployment Preparation** (serialization with Pickle)
* **Research Communication** (clear documentation and reproducible workflow)

---

## Future Work

* Compare with **XGBoost**, **LightGBM**, and **CatBoost**
* Apply **SMOTE** and other advanced resampling techniques
* Perform **feature importance** and **SHAP analysis** for interpretability
* Build a **Streamlit dashboard** for interactive bankruptcy risk prediction
* Investigate transfer learning between the Poland and Taiwan datasets

---

## Author

**Luzuko Nzayo**

Master of Mathematical Sciences | Mathematics Educator | Aspiring Data Scientist

I am passionate about using mathematics, statistics, and machine learning to solve practical problems in finance, education, and business analytics. This project reflects my interest in predictive modeling, risk analysis, and data-driven decision-making.

---

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and share it for educational and research purposes.
