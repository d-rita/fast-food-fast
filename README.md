# fast-food-fast


[![Build Status](https://travis-ci.com/d-rita/fast-food-fast.svg?branch=ft-add-food-api-160939634)](https://travis-ci.com/d-rita/fast-food-fast)
[![Coverage Status](https://coveralls.io/repos/github/d-rita/fast-food-fast/badge.svg?branch=ft-add-food-api-160939634)](https://coveralls.io/github/d-rita/fast-food-fast?branch=ft-add-food-api-160939634)
[![Maintainability](https://api.codeclimate.com/v1/badges/ac9de1de92af85530407/maintainability)](https://codeclimate.com/github/d-rita/fast-food-fast/maintainability)



Fast-Food-Fast is a delivery service for a restaurant. 


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
- PostgreSQL

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
|/auth/signup           |POST       |Register a user     |
|/auth/login            |POST       |Login a user    |
|/users/order           |POST       |Place an order for food |
|/users/orders          |GET        |Get user history for a particular user|
|/orders                |GET        |Get all orders     |
|/orders/orderId        |GET        |Get specific order |
|/api/v1/orders/orderId |PUT        |Change order status|
|/menu                  |GET        |Get available menu     |
|/menu                  |POST       |Add a meal option to the menu  |


- Tests can be run using 
```
pytest tests
```

To get coverage report of tests, run:

```
pytest tests --cov=api
```

