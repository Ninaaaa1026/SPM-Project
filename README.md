# SPM Group Project

## Knowledge Preparation
This section sums up all the required skills in a typical web development cycle. You don't need to rush yourself on all of them at this stage, nor get yourself overwhelmed. Just be aware of these technologies and keep youself upgraded day by day and you will be fine!

> Essential:

* Web app architecture (clear about what is front-end and what is back-end)
* Programming skill
    * Front-end: HTML, CSS, JavaScript
    * Back-end: In this project we will be using Python 3
* Git for version control and collaboration

> Fundamental

* Bootstrap (front-end framework)
* jQuery
* Database design and integration
* (Django) View, Model, Template concepts
* (Django) HTTPResponses (how front-end and back-end communicate)

> Advanced (for interests, probably not needed in this project)

* AJAX
* Website deployment
* RESTful architecture
* Websocket

# Environment Setup

## Text Editor

Use PyCharm as an ideal Django development tool.

> Note: Install the professional version of PyCharm, and apply for a student license following the link below.

* PyCharm: https://www.jetbrains.com/pycharm/
* Obtain a free student license: https://www.jetbrains.com/student/

## Install Python 3.6
* Download the latest Python 3 here: https://www.python.org/downloads/
* Documentation: https://docs.python.org/3.5/reference/index.html

## Install Django 2.0.4

#### 1. Virtualenv
* Install Virtualenv: https://virtualenv.pypa.io/en/stable/installation/
* (Optional but highly recommended) Install Virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
* How to use Virtualenv: https://virtualenv.pypa.io/en/stable/userguide/

> Virtualenv is a tool for creating isolated Python environment to prevent potential interferences of different versions of packages installed on the same machine. Django only works within virtual environments. Before installing Django, you need to install virtualenv.

> Note: If you have both Python 2 and Python 3 installed on your machine, make sure to replace every `python` command to `python3`, and `pip` command to `pip3`.

#### 2. Django

> Note: Django can only be installed or used within virtualenvs, before you type the commands for installing Django via pip, please make sure one of the virtualenv is activatied. You can see a pair of parentheses containing the name of the virtualenv before your terminal prompt if one is properly activated.

* Install the latest Django: https://www.djangoproject.com/
* Documentation: https://docs.djangoproject.com/en/2.0/

## Install Git
* Install git from here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* (Optional) Install a git GUI:
    * Sourcetree (recommended): https://www.sourcetreeapp.com/
