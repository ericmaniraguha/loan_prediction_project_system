# Loan Prediction System

## Overview

This project aims to develop an end-to-end Loan Prediction System, including data preprocessing, model development, and deployment. The system predicts whether a loan application should be approved or not based on various factors.

## Data Source

The dataset used in this project is sourced from Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/burak3ergun/loan-data-set).

## Outline

1. **Loading and Exploring the Data**: Initial exploration of the dataset to understand its structure and features.
2. **Working with Missing Values**: Handling missing values in the dataset using appropriate techniques.
3. **Dropping Unnecessary Columns**: Identifying and removing columns that do not contribute significantly to the prediction task.
4. **Visualization or Making a Storyboard**: Visualizing data distribution and relationships between features to gain insights and create a storyboard.
5. **Encoding the Categorical Data**: Encoding categorical variables into numerical format for model compatibility.
6. **Model Development**: Building machine learning models for loan prediction using various algorithms.
7. **Dividing the Data**: Splitting the dataset into training and testing sets for model evaluation.
8. **Using GaussianNB**: Implementing Gaussian Naive Bayes classifier for prediction.
9. **Loss Function**: Defining and utilizing appropriate loss functions for evaluating model performance.
10. **Using SVC with Grid Search CV**: Employing Support Vector Classifier with Grid Search Cross Validation for parameter tuning.
11. **XGBoost Classifier**: Utilizing XGBoost Classifier for ensemble-based prediction.
12. **Decision Tree Using Randomized Search**: Building a decision tree classifier using Randomized Search for hyperparameter optimization.
13. **Random Forest Using Randomized Search**: Implementing Random Forest classifier with Randomized Search for enhanced performance.
14. **Selecting and Saving the Model**: Selecting the best-performing model and saving it for deployment.

## Readme Content

1. **Introduction**: Briefly explain the purpose and functionality of the Loan Prediction System.
2. **Installation**: Specify any dependencies or requirements needed to run the project.
3. **Usage**: Provide instructions on how to use the system, including data preparation, model training, and prediction.
4. **File Descriptions**: Describe the contents of each file in the project repository.
5. **Data Source**: Mention the source of the dataset used in the project.
   - Data source: [Loan Data Set](https://www.kaggle.com/datasets/burak3ergun/loan-data-set)
6. **Credits**: Acknowledge any data sources, libraries, or tutorials used in the project.
7. **License**: Specify the license under which the project is distributed.

## Conclusion

The Loan Prediction System presented in this project provides a robust framework for automating loan approval decisions. By leveraging machine learning algorithms, it offers a data-driven approach to enhance the efficiency and accuracy of loan processing operations.

## Weights & Biases Integration

This project is integrated with Weights & Biases (wandb) for experiment tracking and visualization. View the latest run at: [eager-breeze-22](https://wandb.ai/ericmaniraguha/loan_prediction_project/runs/4pz3wlsb). You can also explore the project and access logs at: [Loan Prediction Project](https://wandb.ai/ericmaniraguha/loan_prediction_project)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
