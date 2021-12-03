# Customer Propensity

## Overview of propensity

- A propensity model is a model that predicts the likelihood that someone will do something.
- Propensity modeling allows you to allocate your resources more wisely, resulting in greater efficiencies while achieving better results.

## Project Description

- I use Customer propensity to purchase dataset, this is a data set logging shoppers interactions on an online store to build a predictive model.
- Based on some some customer's activities in website, the model can result in whether one specific customer will order a product or not so that we can target him/her as a potential customer. We can give our customers some coupons to courage them buy our products.
- I used EDA to explore dataset and also observed that the dataset is extremely imbalanced. So i dealt with it using SMOTE algorithm.
- After training and validating, i chose Model built in DecisionTreeClassifier to use in my project
- Finally, i created demo website using Flask and deployed it on Heroku cloud platform.
- Link to deployed website on Heroku cloud: https://customerpropensity.herokuapp.com/

## Pipeline

![pipeline](https://github.com/truongminhphung/customer_propensity_to_purchase/blob/master/images/project_pipeline.png?raw=true)

## Demo

![demo](https://github.com/truongminhphung/customer_propensity_to_purchase/blob/master/images/demo.gif?raw=true)

## Dataset

https://www.kaggle.com/benpowis/customer-propensity-to-purchase-data

## Installation

```
    pip install -r requirements.txt
```
