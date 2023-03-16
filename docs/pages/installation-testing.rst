=======================================
Installation guide for testing purpose
=======================================

In this section, you will be guided on how to download the prototype, create virtual environment, install dependencies and run the taxed website.

First, make sure you have python and virtualenv installed on your computer.

If you have not installed, please head over to https://www.python.org/ and google on how to install virtualenv on your machine and comeback once they are installed.

Cloning the repository
=======================================

Clone the repository using the command below::
    
    $ git clone https://github.com/hienng9/taxed.git


Move into the directory where we have the project files::

    $ cd taxed

Create a virtual environment::

    # Let's install virtualenv first if you have not already
    $ pip install virtualenv
    # Then we create our virtual environment
    $ virtualenv envname


Activate the virtual environment using either::

    $ envname/scripts/activate
    $ source envname/bin/activate


Install the requirements::

    $ pip install -r requirements.txt



Running the App
======================================

To run the App, in the same directory, open one terminal::

    $ python3 -m celery -A taxedwebsite worker -l info


open another terminal, run the following::

    $ python3 manage.py runserver



Then, the development server will be started at http://127.0.0.1:8000/

