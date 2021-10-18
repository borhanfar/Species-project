# Project Title : 
Predict the fish species via REST API based on the fish market sales dataset
# Problem Statement :
There are seven fish species in the fish market dataset, and the dataset was recorded in terms of biometric sizes. Seven researchers in the Kaggle website worked on the fish market dataset with different approaches. Unfortunately, the researchers did not find the best model in terms of accuracy for the dataset. The aim of this project is to find the best model with the highest accuracy and embeded in a web based application for educational purposes.
# Approach :
In this project, K-Nearest Neighbor, Support Vector Machine and Random Forest algorithms were applied on the fish market dataset. The accuracy of each model is calculated by five accuracy methods ( Train-Test-Split, K Fold Cross Validation, Stratified K-Fold Cross Validation, Leave one out Cross Validation ( LOOCV ), Repeated Random Test-Train-Split ). Ultimately, the Support Vector Machine had the best result.
# Results :
There are three main components ( application, model, templates ) in the application package. The application was developed by the Flask framework. The Support Vector Machine model connected to the application by pickle link. The templates were designed by HTML and CSS. Therefore, the application is able to predict fish species with 97% accuracy through the REST API on the Heroku cloud platform.
