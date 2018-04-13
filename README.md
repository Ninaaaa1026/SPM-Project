# SPM Group Project

## Knowledge Preparation
This section sums up all the required skills in a typical web development cycle. You don't need to rush yourself on all of them at this stage, nor get yourself overwhelmed. Just be aware of these technologies and keep youself upgraded day by day and you will be fine!

> Essential

* Web app architecture (clear about what is front-end and what is back-end)
* Programming skill
    * Front-end: HTML, CSS, JavaScript
    * Back-end: In this project we will be using Python 3
* Git for version control and collaboration

> Fundamental

* Bootstrap (front-end framework)
* Database design and integration
* (Django) View, Model, Template concepts
* Website deployment

## Text Editor
You will need a text editor to do the development. If you already have one installed on your machine, ignore this step. Some of the popular text editors are listed below.

> Note: You only need to install one of them, choose your favourite one!

* Visual Studio Code (recommended): https://code.visualstudio.com/
* Sublime: https://www.sublimetext.com/
* Notepad++ (Windows only): https://notepad-plus-plus.org/download/v7.5.6.html

## Install Python 3.6
* Download the latest Python 3 here: https://www.python.org/downloads/
* Documentation: https://docs.python.org/3.5/reference/index.html

After installation, open terminal and type `python3` to verify that Python is working. If you see output similar to the following, your Python is installed successfully.
```
aos112:~ LeonVincii$ python3
Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```
Type `quit()` to quit the Python shell.

## Install Django 2.0.4

#### 1. Verify pip
Open terminal and type `pip3 --version` to verify if pip is installed, if you see output similar to the following, your pip is working properly.
```
aos112:~ LeonVincii$ pip3 --version
pip 9.0.1 from /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (python 3.6)
```
Upgrade pip:

> Windows

```
python3 -m pip install -U pip
```

> MacOS/Linux

```
pip3 install -U pip
```

#### 2. Virtualenv
* Install Virtualenv: https://virtualenv.pypa.io/en/stable/installation/
* (Optional but highly recommended) Install Virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
* How to use Virtualenv: https://virtualenv.pypa.io/en/stable/userguide/

> Virtualenv is a tool for creating isolated Python environment to prevent potential interferences of different versions of packages installed on the same machine. Django only works within virtual environments. Before installing Django, you need to install virtualenv.

> Note: If you have both Python 2 and Python 3 installed on your machine, make sure to replace every `python` command to `python3`, and `pip` command to `pip3`.

#### 3. Django
* Download the latest Django here: https://www.djangoproject.com/
* Documentation: https://docs.djangoproject.com/en/2.0/

## Install Git
* Install git from here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* (Optional) Install a git GUI, you only need to choose one:
    * Sourcetree: https://www.sourcetreeapp.com/
    * Gitkraken: https://www.gitkraken.com/
