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
* (Optional) Install Virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
* How to use Virtualenv: https://virtualenv.pypa.io/en/stable/userguide/

> Note: If you have both Python 2 and Python 3 installed on your machine, make sure to replace every `python` command to `python3`, and `pip` command to `pip3`.

#### 2. Django

> Note: Django can only be installed or used within virtualenvs, before you type the commands for installing Django via pip, please make sure one of the virtualenv is activatied. You can see a pair of parentheses containing the name of the virtualenv before your terminal prompt if one is properly activated.

* Install the latest Django: https://www.djangoproject.com/
* Documentation: https://docs.djangoproject.com/en/2.0/

## Install Git
* Install git from here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* (Optional) Install a git GUI:
    * Sourcetree (recommended): https://www.sourcetreeapp.com/

# Django Quick Guide

This quick guide can only be used as a reference or reminder in the development, it cannot replace the documentation of Django.

Django Documentation: https://docs.djangoproject.com/en/2.0/

## Run Django Development Server

1. Activate the virtualenv in which the Django installs;
2. `cd` into the root directory of a Django project and run `python manage.py runserver [ip:port]`.

> Note: The root directory is where `manage.py` locates; If ip address and port are left blank, the server will be run on `localhost:8000`.

## Database Migrations

After the database being connected to the backend, every changes commited in the Django model (recall that Django models are data structures that stored in the database) will not be reflected in the database until you migrate it. To migrate the changes to the database, follow the steps below.

1. run `python manage.py makemigrations`, and then
2. run `python manage.py migrate`.

> Note: Step 1 is not optional! You MUST run `makemigrations` before you `migrate`.

## Django Template Languages

Django supports a set of template languages to be used in conjunction of HTMLs to dynamically create web pages with ease. Imperatives are encapsulated in `{% %}` and template variables are encapsulated in `{{ }}`.

#### Template Inheritance
Django supports template inheritance by adding `{% extends %}` imperative at the beginning of the template and override a block with `{% block %}` imperatives.

> base.html

```
<!DOCTYPE html>
<html lang="en">
<head>
  <title> Base </title>
</head>
<body>
  <p> Text 1 </p>
  {% block body %}
    <p id="para1"> Text 2 </p>
  {% endblock %}
</body>
</html>
```

> inherit.html

```
{% extends 'base.html' %}

{% block body %}
  <p id="para2"> Text 3 </p>
{% endblock %}
```
> Result: base.html will display Text 1 and Text 2, inherit.html will display Text 1 and Text 3. Other parts are the same.
> Note: inherit.html will not have the `<p>` tag with its `id=para1`, insteadly, it will only have `<p id="para2">`. So it's not only the text that changed, it's the whole component that changed.

#### Template `if`
Syntax: `{% if %}` ... `{% endif %}`

> The following example checks if the template variable `avatar` is `null`, if it is `null`, setup a random generated avatar for the user, otherwise use user's avatar.

```
<div id="user_avatar_container" class="avatar_container left_btn">
  {% if not avatar %}
    <img class="avatar_img" src="https://api.adorable.io/avatars/50/{{ username }}"/>
  {% else %}
    <img class="avatar_img" src={{ avatar }}/>
  {% endif %}
</div>
```

#### Template `for`
Syntax: `{% for %}` ... `{% endfor %}`

> The following example creates a number of `div` components for user contacts.

```
{% for contact_obj in user_contacts %}
  <div id="bulletin_contact" class="bulletin_contacts contact_container">
    ...
  </div>
{% endfor %}
```