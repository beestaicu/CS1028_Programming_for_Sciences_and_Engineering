# ---------------------------------------
# lecture11.py-More on input/output
# ---------------------------------------

# ------------------------------------------------------
# Outline
# 1) Recap: input from keyboard
# 2) "Make up" some data
# 3) Reading and writing files
# 4) Output to graphics

# -------------------------------------------------------------
# 1) Recap: Entering data manually
# At the OS command prompt:
# The file Lec09_helloJimmy.py contains

# import sys
# print("Hi, ", end="")
# print(sys.argv[1], end="")
# print(". How are you?")

# At the command prompt:

# python Lec09_helloJimmy.py Daniel

# This print to the screen:

# Hi, Daniel, How are you?

# --------------------------------------------------
# Within Python (e.g. an IDE such as Spyder):

# nstr = input("Give me a number: ")

# This prints Give me a number: to the screen, and assigns whatever the user
# enters (finished ny Enter) to the variable nstr (of type string).

# n = int(nstr)
# x = float(nstr)

# These commands turn the input into a number (either integer ot floating point
# number), they will produce erroes if nstr does not "look like" a number.

# ------------------------------------------------------------
# Entering arbitrary many numbers:
# (e.g. for the min exercise, Q1 from Section 1.5 in the Princeton book)

# numbers = []
# a = int(input("GIve me a number: "))
# numbers = numbers + [a]
#
# a_str = input("Give me a number: ")
# while a_str != "":
#     a = int(a_str)
#     numbers = numbers +[a]
#     a_str = input("Give me a number: ")

# The loop is stopped if the user hits only Enter (returning an empty string).

# ---------------------------------------------------
# A litte fancier (and better): Exception handing

# numbers = []
# a_str = input("Give me a number (or simply 'Enter' to end reading) : ")
#
# while a_str != "":
#     try:
#         a = int(a_str)
#     except ValueError:
#         print("Last input was not a number. I stop reading input.")
#         break
#     numbers = numbers + [a]
#     a_str = input("Give me a number (or simply 'Enter' to end reading input:")

# --------------------------------------------------------------
# 2) Make up some data
# Entering data manually is tedious.

# --------------------------------------------------------------

# import random
#
# rN = []
# for i in range(10):
#     r = random.random()
#     rN = rN + [r]
# print(rN)

# THis prints something like:
# [0.3779938004082116, 0.42839310319079893, 0.26703316530158605,
# 0.15755944700059354, 0.3785540697692277, 0.49237408911448166,
# 0.8875949146801231, 0.37554399911554814, 0.9280065982812257,
# 0.5059462444941377]

# (random numbers drawn from uniform distribution)

# ----------------------------------------------------------

# import random
# random.seed(24102019)
# rN = []
# for i in range(10):
#     r = random.random()
#     rN = rN + [r]
# print(rN)

# This always prints:
# [0.3455885141390541, 0.23728051859614996, 0.42269425812458084,
# 0.005893225371031874, 0.3108901200262346, 0.6402619888670006,
# 0.20329670623540808, 0.5741181022063454, 0.160805772297278,
# 0.7714901240178259]

# -------------------------------------------
# Sometimes it is better to have integers (e.g., Q5 form section 1.5 ...
# longest run in a sequence)

# import random
#
# rN = []
# for i in range(20):
#     r = random.randint(0,10)
#     rN = rN + [r]
# print(rN)

# This prints someting like:
# [5, 4, 4, 0, 0, 10, 1, 7, 2, 7, 0, 0, 4, 4, 10, 4, 8, 3, 7, 2]

# ------------------------------------------------
# 3) Input from text files
# There are various ways how to read and write files in Python.
# I show you my preferred one.
# It uses Numpy.

# # Put this at the top of your Python code:
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Using Anaconda (i.e. in Spyder) the above should work.
# # If not, type this at the OS command prompt first:
#
# # python -m pip install -- user numpy matplotlib
#
# # ------------------------------------------------------
# # Save the random numbers to a file called someNumbers.txt
# # (created in the current working directory):
#
# np.savetxt("someNumbers.txt", rN)
#
# # With a little bit of formatting:
#
# # np.savetxt("someNumbers.txt" , rN, "%15.12f")
#
# # or
#
# # np.savetxt(fname= "someNumbers.txt", X = rN, fmt = "15.12f")
#
# # Each number is at most 15 characters wide with exactly
# # 12 after the decimal point.
#
# # -----------------------------------------------===
# # Read the numbers back from someNumber.txt:
#
# Data_arr = np.loadtxt("someNumbers.txt")
#
# # Data_arr is a numpy array (more later). To turn it into a list:
#
# Data = list(Data_arr)
#
# print(Data)

# --------------------------------------------------------------
# 4) Slightly more sophisticated example

import numpy as np
import matplotlib.pyplot as plt

fileName = "AberdeenDyce.txt"
Data_arr = np.loadtxt(fileName, skiprows=1)

# To get the header:
ColNames_arr = \
np.genfromtxt(fileName, dtype="str", skip_footer=12, delimiter="\t")

# (\line continuation charactor)
# Again, turn it into a list:

ColNames = list(ColNames_arr)
Data = list(Data_arr)
print(ColNames)
print(Data)

# ----------------------------------------------------------

month = list(Data_arr[:,0])
maxTemp = list(Data_arr[:, 1])
minTemp = list(Data_arr[:, 2])

plt.figure()
plt.plot(month, maxTemp)
plt.plot(month, minTemp)
