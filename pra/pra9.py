# ---------------------------------------
# Practical 9
# ------------------------------------------

# 1. Write a function mySin(x,N) that takes two arguments: a float x and a positive
# integer N and returns the infinite sum on the right-hand side above truncated at N,
# i.e., it computes
# If you are not fluent with the summation sign Σ, this is
import math
import numpy as np

arr = np.loadtxt("testSine.txt")

def mySin(x,N):
    sum = 0
    for i in range(N+1):
        sin = ((-1)**i * x ** (2*i + 1))/ math.factorial(2*i+1)
        sum += sin
    return(sum)

def mySin2(x,N):
    a = x
    s = a
    for i in range(1, N):
        a = a * x**2 * (-1) / (2*i) /(2*i+1)
        s = s + a
    return s

def mySin3(x,N):
    x = in_period(x, 2* math.pi)
    total = 0
    for n in range(N+1):
        y = (-1)**n * x**(2*n+1)
        for i in range(1,2*n + 2):
            y /= i
        total += y
    return total




def in_period(x, period):
    if period == 0:
        x = 0
        return x
    while x > period:
        x -= period
    while x <= 0:
        x += period
    return x

def in_period2(x, period):
    if x > period or x < period:
        x = x % period
    return x



# print(in_period(-0.4,2))
# print(in_period2(-0.4,2))

def good_enough(x,N):
    try:
        result = mySin3(x,N)
    except OverflowError:
        return False
    return abs(result - math.sin(x)) < 1e-06

def check():
    for i in range(len(arr)):
        x = arr[i,0]
        N = int(arr[i,1])
        if good_enough(x,N):
            print("Work fine for ",x," ",N,".")
        else:
            print("Fail for ",x," ",N,".")

check()




