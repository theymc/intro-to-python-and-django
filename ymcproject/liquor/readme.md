#Assignment 2 Solution (LCBO API)

A comprehensive solution has been posted to the ymc github:
https://github.com/theymc/intro-to-python-and-django

###How to download the assignment from github:

* You will need to navigate to your code folder (In TERMINAL) and type in

```git clone git@github.com:theymc/intro-to-python-and-django.git```

```cd intro-to-python-and-django/ymcproject```

```sudo pip install -r requirements.txt```

You have now cloned the repository, and installed the necessary requirements to run the projects.

###Running the scripts
* Ensure that your database is set up --- remove the old one if it exists and then run:

```python manage.py syncdb```

* We will now run the script to copy data from the LCBO API

```python manage.py steal_booze```

Wait --- this could take a few minutes, as we are copying 10000+ products from the LcboAPI.

* Now -- to analyze the stolen data (to answer the questions), simply run:

```python manage.py analyze_booze```

###Explanation
The solution is in the **liquor/** folder. I created a python app to place and organize all our code in regards to this assignment. Heres how the code is organized in the liquor folder:

* **models.py** has all of my model definitions for our product
* **liquor_horse.py** contains the script used to copy data from lcboapi.com to our database
* **liquor_analysis.py** contains all of the orm queries and analysis used to answer the questions
* In the **management/commands** folder, you will find the definitions for the two commands we used. This is where the scripts are actually executed.

Happy hacking, and please tinker with the script to provide some insight on informed purchases from the LCBO.

###SOLUTION SIDE NOTES:
Two additional things were done, that were not outlined in the assignment.

1. I made an **isolated app**, with its own models and modules by using ```python manage.py startapp liquor```. All my code in relation to this assignment is in the liquor folder.
2. I then decided that the scripts may as well be **manage.py commands** -- rather than some arbitrary script to run (A more direct integration with Django). The explanation of how this works is here: https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
