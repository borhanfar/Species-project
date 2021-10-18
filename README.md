# Project Title 
Predict the fish species via REST API based on the fish market sales dataset
# Problem Statement 
There are seven fish species in the fish market dataset, and the dataset was recorded in terms of biometric sizes. Seven researchers in the Kaggle website worked on the fish market dataset with different approaches. Unfortunately, the researchers did not find the best model in terms of accuracy for the dataset. The aim of this project is to find the best model with the highest accuracy and embeded the model in a web based application for educational purposes.
# Approach 
In this project, K-Nearest Neighbor, Support Vector Machine and Random Forest algorithms were applied on the fish market dataset. The accuracy of each model is calculated by five accuracy methods ( Train-Test-Split, K Fold Cross Validation, Stratified K-Fold Cross Validation, Leave one out Cross Validation ( LOOCV ), Repeated Random Test-Train-Split ). Ultimately, the Support Vector Machine had the best result.
# Results 
There are three main components ( application, model, templates ) in the application package. The application was developed by the Flask framework. The Support Vector Machine model connected to the application by pickle link. The templates were designed by HTML and CSS. Therefore, the application is able to predict fish species with 97% accuracy through the REST API on the Heroku cloud platform.
# Dataset Link
https://www.kaggle.com/aungpyaeap/fish-market
#  Main Pipeline
https://github.com/borhanfar/species-project-pipeline/blob/main/Apply_three_models_on_dataset.ipynb
# Software Solution
## Develop an application in the local machine.
1) Create a virtual environment in the local machine.
2) Developing the python app by Flask.
3) Developing the model and connecting the model to the main app.
4) Developing web templates by HTML and CSS 
## Transfer application to GitHub
GitHub ( use a GitHub link )
## Deploy application in the Heroku cloud application platform.
Create a new app on the Heroku platform and Deploy application repository through the Github connection section.
# Application
http://fish-prediction-api.herokuapp.com
