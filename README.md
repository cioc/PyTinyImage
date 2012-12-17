PyTinyImage
===========

Python version of matlab code for accessing the tiny image dataset: http://horatio.cs.nyu.edu/mit/tiny/data/index.html

(Started as a conversion of matlab to scilab code.  That was a mistake.)

USAGE
=====

loadFromKeywords.py

usage: python loadFromKeywords <keyword,keyword,keyword,...> <max> <output path>

e.g. python loadFromKeywords.py cat,hamburger 100 tacos
-The last command will fetch a hundred cats and a hundred hamburgers for you.  These cats and hamburgers will be put in tacos/cat and tacos/hamburger, respectively.

tinyimage.py

Contains helpful functions for manipulating the tinyimage dataset.  See the source of loadFromKeywords.py to see a good use of the library.
