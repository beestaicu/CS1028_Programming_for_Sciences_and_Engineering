# -------------------------------------------------------
# practical 6
# -------------------------------------------------------

#----------------------------------------------------------------
# 1. Create a plot, similar to the one on the last slide of Lecture 12, 
# that shows the graph of the sine, the cosine, and the tangent function. 
# Take the x-range as [−2π, 2π]. Proceed in the following steps:
# a) Create a fine grid of (100 or more) x-values covering the x-range (as a list or a
# one-dimensional numpy array if you prefer).
# b) For each of the three functions, create a corresponding list of y-values.
# c) Plot all three in one figure.
# A couple of things to note:
# • You do not need numpy for the exercise (you can of course use it). However, you
# do need matplotlib for plotting.
# • The poles of the tangent function are a little challenge: you need to specify the
# y-range in order to get a sensible plot.

import matplotlib.pyplot as plt
import numpy as np
gird = np.linspace(-2*np.pi, 2*np.pi, 100)
sins = np.sin(gird)
coss = np.cos(gird)
tans = np.tan(gird)

plt.figure("Trig functions")

plt.plot(gird, sins)
plt.plot(gird, coss)
plt.plot(gird, tans)

plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plotting trig functions")

plt.ylim(-5, 5)
plt.show()

# -------------------------------------------------------------------------
# 2. Two-dimensional random walk
# a) Take n = 10 000 and create a sequence of random numbers x1, . . . , xn drawn from
# the standard normal distribution (hint: random.gauss(0,1)) and store them in
# a list (or a one-dimensional numpy array if you prefer). Then create the sequence
# s1, . . . , sn of cumulative sums, i.e.,
# sk = x1 + x2 + . . . + xk
# for any k from 1 to n.
# b) Store s1, . . . , sn in a text file called s-values.txt.
# c) Redo the whole thing, creating standard normal variates y1, . . . , yn, corresponding
# cumulative sums t1, . . . , tk and store them in a text file called t-values.txt.
# d) Make a plot of the n points (s1, t1), . . . ,(sn, tn), where two successive points are
# joint be a line.

# a)
import random
import numpy as np
import matplotlib.pyplot as plt
import stdarray

n = 10000
x = []
s = []
y = []
t = []

def number(number):
    for i in range(n):
        a = random.gauss(0, 1)
        number.append(a)

def sum(number,sum):
    total = 0
    for i in range(n):
        total += number[i]
        sum.append(total)
# b)

# c)
number(x)
number(y)
sum(x,s)
sum(y,t)
np.savetxt("s-values.txt", s)
np.savetxt("t-values.txt", t)

# listn= []
# for i in range(0,n):
#     listn.append(i)

listn= list(range(10000))
plt.figure("n-s figure")
plt.plot(s,listn)
plt.show()
