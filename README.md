# Learning Django REST Framework

## Overview
[Django](https://www.djangoproject.com/) is my favourite web development framework. I wanted to learn how to build APIs using the [Django Rest Framework](https://www.django-rest-framework.org/).

There are many resources available for learning and using Django REST framework. Personally, I think that the official documentation is a great starting point. I decided to follow a set of tutorials created by the [Django Rest Framework Team](https://www.django-rest-framework.org/#license).

Each branch on this repository contains a different topic.

## Requirements
Python 3.7+
Pipenv 2018.11.26+

## Installation
Make sure to be on the same level as the `Pipfile` and `Pipfile.lock` files. 

``` bash
# Install Virtual Environment:
$ pipenv install

# Activate Virtual Environemnt:
$ pipenv shell

# Running the Application
python manage.py migrate    # will create a SQLite database
python manage.py runserver  # will start the server
```