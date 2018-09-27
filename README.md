**Fast Food Fast**

[![Build Status](https://travis-ci.com/d-rita/fast-food-fast.svg?branch=test-apis)](https://travis-ci.com/d-rita/fast-food-fast)
[![Coverage Status](https://coveralls.io/repos/github/d-rita/fast-food-fast/badge.svg?branch=challenge2)](https://coveralls.io/github/d-rita/fast-food-fast?branch=challenge2)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac9de1de92af85530407/maintainability)](https://codeclimate.com/github/d-rita/fast-food-fast/maintainability)


Fast-Food-Fast is a delivery service for a restaurant. 

It is currently hosted on Heroku at https://diana-fast-food-fast.herokuapp.com/api/v1/orders

**UI**

The UI is hosted on Github pages at https://d-rita.github.io/fast-food-fast/UI/user_signup.html

**Getting Started**

These instructions will help you get this work on your local machine for development and testing.

**Prerequisites**

This is what you need on your machine:
- Web browser
- Python 
- Git
- Postman

**Get the repo**

Use: 
```
git clone https://github.com/d-rita/fast-food-fast.git 
```
on your local machine to set up the code for you. Then navigate to folder with
 ```
 cd fast-food-fast
 ```

**Installations**

In your terminal:
- Install virtualenv using:
```
 pip install virtualenv
```
- create virtual environments using: 
```
virtualenv venv
```
- activate virtual environment:
```
 venv\Scripts\activate
 ```
To install dependencies:
```
pip install -r requirements.txt
```

**Testing**

To test whether the endpoints work:
- Start server with: 
```
python run.py 
```

- Open Postman to test the endpoints

|Endpoint               | HTTP Verb | Action            | 
|-----------------------|-----------| ------------------|
|/api/v1/orders         |GET        |Get all orders     |
|/api/v1/orders         |POST       |Create an order    |
|/api/v1/orders/orderId |GET        |Get specific order |
|/api/v1/orders/orderId |PUT        |Change order status|

- Tests can be run using 
```
pytest tests/test.py
```
To get coverage report of tests, run:
```
pip install pytest-cov
```
```
pytest tests/test.py --cov=app --cov-report term missing
```

**Deployment**

This app is currently hosted on Heroku at https://diana-fast-food-fast.herokuapp.com/api/v1/orders
