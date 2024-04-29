SpiffyDuck
==============
This GIT respository contains code to go along with the blog post
"Build your own Low-Code Business Applications with SpiffWorkflow"
https://medium.com/@danfunk/build-your-own-low-code-business-applications-with-spiffworkflow-1d0730acc1f3


How to use and extend
-----------------------
To interact with and extend this documentation you need:

.. sidebar:: Note

   As of writing, this documentation has not been tried on Windows

1) this repository
2) a supported version of Python 3 (as of the writing, that means >= 3.5) - Python 2 is not supported
3) a virtual environment 

Set up repository
------------------
Just use git clone to clone this repository

.. code:: bash

   git clone git@github.com:risclog-solution/spiffworkflow-example.git

Set up virtual environment
--------------------------

Python now includes virtualenv in the standard library.

.. code:: bash

    cd spiffworkflow-example
    python3 -m venv venv

This will setup a Python3 virtual environment.

Install Requirements
--------------------

Now that we have the Python virtual environment set up, let's get our requirements installed.

.. code:: bash

    venv/bin/pip install -r requirements.txt

This should get us all of the tools we will need to run the examples - Any of the .py files should be able to be run
in the SpiffyDuck main directory

.. code:: bash

    venv/bin/python ducks.py


