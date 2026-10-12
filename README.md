# Insurance Claim Prediction Using Machine Learning

# 1. Project Overview

The Insurance Claim Prediction project uses machine learning classification algorithms to predict whether a vehicle insurance policyholder will file a claim based on available customer, vehicle, and policy-related attributes.

The project explores the dataset, performs statistical analysis and exploratory data analysis (EDA), preprocesses the data, develops multiple machine learning models, and compares their performance to select a suitable model.

# 2. Project Objectives

* Understand the dataset and its characteristics.
* Perform statistical analysis and exploratory data analysis.
* Clean and preprocess data for machine learning.
* Engineer useful features to improve prediction.
* Train and compare multiple classification algorithms.
* Evaluate models using appropriate classification metrics.
* Identify features associated with claim predictions.
* Develop business insights and recommendations.

# 3. Project Workflow

1. Data Understanding
2. Statistical Analysis
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Engineering
6. Model Development
7. Model Evaluation
8. Model Comparison
9. Final Model Selection
10. Prediction
11. Business Insights
12. Recommendations

# 4. Insurance Claim Process

Person
↓
Purchases insurance
↓
Becomes a policyholder
↓
Pays the premium
↓
Insurance policy becomes active
↓
A covered event may occur
↓
Policyholder may file a claim
↓
Insurance company evaluates the claim
↓
Historical claim information is recorded
↓
Machine learning model learns from historical data
↓
New policyholder's information is provided
↓
Model predicts the likelihood of a claim

# 5. Dataset Description

The project uses `Insurance_dataset.csv`.

The dataset contains information about insurance policies, customer age, vehicle age, region, vehicle specifications, safety features, and claim status.

**Target variable:** `claim_status`

* 0 — No claim
* 1 — Claim

The `policy_id` column is an identifier and is excluded from the model's input features.

# 6. Exploratory Data Analysis

The analysis includes:

* Dataset dimensions, data types, and unique values.
* Missing values and duplicate records.
* Numerical summaries and categorical value counts.
* Mean, median, mode, variance, standard deviation, quartiles, and IQR.
* Numerical and categorical feature distributions.
* Claim versus no-claim distribution.
* Relationships between available customer, vehicle, and regional attributes and claim status.
* Correlation analysis and visualizations.

Visualizations include histograms, boxplots, count plots, bar charts, scatter plots, and correlation heatmaps where appropriate.

## 7. Data Preprocessing and Feature Engineering

The preprocessing workflow includes:

* Handling missing values.
* Encoding categorical variables.
* Scaling numerical features where required.
* Separating input features and the target variable.
* Splitting data into training and testing sets.
* Creating useful features, such as vehicle age groups, where appropriate.

Preprocessing steps are fitted on the training data through a machine learning pipeline to reduce data leakage.

## 8. Machine Learning Algorithms

The project compares the following classification algorithms:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* AdaBoost Classifier
* K-Nearest Neighbors (KNN)

## 9. Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix

Training and testing performance are compared to identify possible overfitting or underfitting. The final model should be selected according to the evaluation results and the business objective, not accuracy alone.

## 10. Business Questions

The project investigates the following questions:

1. How do observed claim rates differ across customer age groups?
2. Which features contribute most to the model's predictions?
3. Are some regions associated with higher observed claim rates?
4. How is vehicle age associated with claim status?
5. Do claim rates differ across fuel types and vehicle models?
6. Which machine learning algorithm performs best on the evaluation metrics?
7. Does the selected model show signs of overfitting?
8. How could an insurer use predictions to support risk assessment?

The current dataset does not include a previous vehicle damage field, so that question cannot be directly investigated using this dataset.

## 11. Business Insights and Recommendations

The project analyzes customer and vehicle attributes to understand their relationship with insurance claim status.

Claim rates can be compared across customer age groups, vehicle age groups, fuel types, regions, and vehicle models. Random Forest feature importance can also help identify variables that the model relies on when making predictions.

These findings may support insurance risk assessment, underwriting review, and further investigation of potential pricing factors. However, observed relationships do not prove causation, and differences between groups should be validated before being used in business decisions.

Model performance should be evaluated using precision, recall, F1-score, and the confusion matrix in addition to accuracy. Predictions should support human review rather than automatically determine policy approval or claim rejection.

Potential limitations include missing or inaccurate data, class imbalance, limited generalization to future policyholders, and the absence of other variables that may affect claim likelihood. Further validation on new data is recommended before deployment.

## 12. Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## 13. Project Deliverables

* Jupyter Notebook containing analysis, preprocessing, modeling, and evaluation.
* Insurance dataset used for the project, subject to its sharing terms.
* Project report describing methodology and findings.
* Presentation summarizing results and recommendations.
* README documentation.

## 14. Conclusion

This project demonstrates an end-to-end machine learning workflow for insurance claim prediction, from data understanding and exploratory analysis to model evaluation and business interpretation.

The final model should be selected based on measured performance, appropriate validation, and the intended business use. Its predictions can help prioritize further review, but they should not be treated as proof that a particular policyholder will file a claim.


# Business Insights and Recommendations

The Insurance Claim Prediction project analyzes customer and vehicle attributes to understand their relationship with insurance claim status.

Claim rates are compared across customer age groups, vehicle age groups, fuel types, regions, and vehicle models. Random Forest feature importance is also used to identify variables that the model relies on when predicting claims.

These findings may support insurance risk assessment, further underwriting review, and investigation of possible pricing factors. However, observed relationships do not prove causation, and differences between groups should be validated before being used in business decisions.

The model should be evaluated using precision, recall, F1 score, and the confusion matrix in addition to accuracy. Its predictions should support human review rather than automatically determine policy approval or claim rejection.

Possible limitations include missing or inaccurate data, class imbalance, limited generalization to future policyholders, and the absence of variables that may affect claim likelihood. Further validation on new data is recommended before deployment.

# Project working step by step

                                      1. Data Understanding
                                              ↓
                                      2. Statistical Analysis
                                              ↓
                                      3. EDA
                                              ↓
                                      4. Data Preprocessing
                                              ↓
                                      5. Feature Engineering
                                              ↓
                                      6. Model Development
                                              ↓
                                      7. Model Evaluation
                                              ↓
                                      8. Model Comparison
                                              ↓
                                      9. Final Model Selection
                                              ↓
                                      10. Prediction
                                              ↓
                                      11. Business Insights
                                              ↓
                                      12. Recommendations 

