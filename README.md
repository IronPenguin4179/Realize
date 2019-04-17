[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
[![style](https://img.shields.io/badge/Style-PEP8-brightgreen.svg)](https://www.python.org/dev/peps/pep-0008/)

# Realize
Realize is a completely Python program designed to scan through a project and all its non standard lib imports to find class names, locations, and methods.

# Why would I want to do that?
The goal was to create a resource to assist in reading a program you were completely unfamiliar with. When I started in open source I often had trouble reading a new code base. So many classes and methods would get called, but it was hard to lookup and find out what each one was.

Realize is intended to help you read through unfamiliar code, find a method or class you aren’t familiar with, enter its name in the search bar, and turn up all relevant information. This includes where to find the method's definition, so you can look directly at how it functions.

# Project Status
Realize is currently functional and in continued development. I will continue to add features and improve its functionality as I can.

# Instructions
* Clone Realize.
* Run main.py. A window will appear. Click File, and  open example.py in the example folder or run it on itself with main.py.
* The search bar is used to find out info on any class throughtout the program and any files it imports from except base python libraries. Search for wanted class name to have it return info on the class.

# Caveats
 As each different language would have different rules for interpretation, it’s only designed for analyzing Python code. In the future, if the project is useful enough, it would be worth refactoring to allow for other language modules like C++ or Java.

# License
MIT © IronPenguin4179
