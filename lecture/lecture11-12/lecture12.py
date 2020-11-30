# ---------------------------------------------------------
# lecture 12 - More on plotting and Numpy
# -----------------------------------------------------------

# ------------------------------------------------------------------
# Outline
# 1) More on graphics
# 2) More on Numpy

# Remember:
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------
# The max temperature from the Dyce data

# Data_arr = np.loadtxt("AberdeenDyce.txt", skiprows=1)
# month = list(Data_arr[:,0])
# maxTemp = list(Data_arr[:, 1])
# minTemp = list(Data_arr[:, 2])

# plt.figure()
# plt.plot(month, maxTemp)
# plt.show()
# 12 points connected by straight lines, month contains their x-coordinates,
# maxTemp the corresponding y-coordinates


# ------------------------------------------------------------------------
# Pimping the plot

# plt.plot(month, maxTemp, color="green", marker="o", linestyle="dashed")
# plt.show()

# This does the same:

# plt.plot(month, maxTemp, "g--o")
# plt.show()

# Or magenta diamonds, no lines:

# plt.plot(month, maxTemp, "md")
# plt.show()

# -----------------------------------------------------------------
# Pimping the plot further

plt.figure()
# fontText = {"family": "serif", "size": 10}
# fontTitle = {"family": "serif", "size": 20}
# plt.rc("font", **fontText)      # ???
# ax = plt.axes()
# ax.xaxis.set_major_locator(plt.FixedLocator([1,2,3,4,5,6,7,8,9,10,11,12]))
# ax.xaxis.set_major_formatter(plt.FixedFormatter(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",\
# "Aug", "Sep", "Oct", "Nov", "Dec"]))
# ax.grid()
# plt.plot(month, maxTemp, "r--o", label="max")
# plt.plot(month, minTemp, "b--o", label="min")
# plt.legend()
# plt.xlim(0, 13)
# plt.ylim(-4, 24)
# plt.ylabel("Temperature (℃)")
# plt.title("Monthly temperatures at Aberdeen Dyce", fontdict=fontTitle)
# plt.show()

# -------------------------------------------------------
# Before we get back to Numpy arrays...
# let's get back to lists (cf.lecutre 07)

# L = [3, 4, 17]

# Elements can have different types:

# K = [2, 3, "cheese"]
# M = [3, 4, "cheese", [1, 2, 17]]

# Accessing single elements:

# L[1] = 1
# K[0] = "hello"

# A handy way to create lists: numbers from 10 to 20 (note: these are 11 numbers)

# N = list(range(10, 21))

# The length

# print(len(N))

# List slicing:
# print(N[0:5])
# print(N[0:5:2])
# print(N)
# print(N[3:-2])
# print(N[5])
# print(N[:])

# Aliasing:

# N2 = N
# print(N2)
# N[0] = -3.1415
# print(N[0])
# print(N2)

# ----------------------------------------------------
# Numpy arrays

# import numpy as np

# The core of numpy is the data type ndarray

# A = np.array([[1, 2, 3], [5, 6, 7]])

# print(A)
# [[1 2 3]
#  [5 6 7]]

# print(type(A))
# numpy.ndarray

# print(np.shape(A))
# (2, 3)

# accessing individual elements and parts by list slicing syntax:
# print(A[1, 1])

# this extracts the second column
# print(A[0:2,1])

# this does the same:
# print(A[:, 1])

# numpy also contains functions that work on arrays

# import math
# print(np.sqrt(2) == math.sqrt(2))
# print(np.sqrt(2))
# print(math.sqrt(2))

# print(np.sqrt(A))

# Simple arithmetics work element-wise

# B = A + 1
# C = A * B
# print(B)
# print(C)

# array([2, 6, 12],
#       [30, 42, 56])

# Some handy functions creating arrays:

# N = np.ones((4,3))
# print(N)
# 
# Z = np.zeros((4, 3))
# print(Z)
# 
# L = np.linspace(-2, 2, 100)
# print(L)

# Connecting the dots...
