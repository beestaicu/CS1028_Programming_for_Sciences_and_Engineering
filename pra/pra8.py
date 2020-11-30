# --------------------------------------------
# Practical 8
# --------------------------------------------

import math

# 1. What happens if you run factorial() (considered in class) with negative value of n?
# With a large value, say 35?
n = -2 # ValueError: factorial() not defined for negative values
m = 30 # 10333147966386144929666651337523200000000
a = math.factorial(m)

# print(a)

# 2. Compose a recursive program that computes the value of ln(n!).
def ln(n):
    if n == 0:
        return 0
    else:
        return math.log(n) + ln(n-1)


# print(ln(10))

# 3. Consider the following recursive function
def someFun(n):
    if n <= 0:
        return
    print(n)
    someFun(n-2)
    someFun(n-3)
    print(n)
# Write down the sequence of integers written by a call to someFun(6). AFTERWARDS
# check your answer by running it.

# someFun(6)


# 4. Consider the following recursive function
def moreFun(n):
    if n <= 0:
        return ""
    return moreFun(n-3) + str(n) + moreFun(n-2) + str(n)
# What is the return value of moreFun(6)?

# print(moreFun(6)) # 34(int) or 311361142246(str)

# 5. Consider the following recursive function:
def mystery(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return mystery(a+a, b//2)
    return mystery(a+a, b//2) + a
# a) What does mystery(25, 2) return? # 50
# b) What does mystery(3, 11) return? #33
# c) Given positive integers a and b, describe what value mystery(a, b) computes.

# print(mystery(3,11))

# 1. Write a recursive function that takes a positive integer as input and returns its prime
# decomposition as a list of numbers.
# Sounds a lot like the first Advanced question from Practical 7, but this time you are
# explicitly asked to write a recursive function, i.e, one that is calling itself. Make
# use of the fact that, if m is a prime divisor of n, it suffices to compute the prime
# decomposition of n/m.

def is_prime(x):
    prime = True
    for i in range(2, x//2+1):
        if x % i == 0:
            prime = False
    return prime

def list_prime(n):
    a = []
    for i in range(2, n + 1):
        if is_prime(i):
            a.append(i)
    return a

def prime_divisor(n):
    for p in list_prime(n):
        if n % p == 0:
            return p
def factor(n):
    if n == 1:
        return []
    p = prime_divisor(n)
    return [p] + factor(n//p)

# print(factor(16))


# 2. If you still do not feel sufficiently challenged: Permutations. Compose a program
# that takes a command-line argument n and writes all n! permutations of the n letters
# starting at a (assume that n is no greater than 26). A permutation of n elements
# is one of the n! possible orderings of the elements. As an example, when n = 3 you
# should get the following output. Do not worry about the order in which you enumerate
# them.
# bca cba cab acb bac abc

letters = ["abcdefghijklmnopqrstuvwxyz"]

def permutation_helper(n):
    if n == 1:
        return [[1]]
    else:
        perms = permutation_helper(n-1)
        result = []
        for perm in perms:
            for i in range(n):
                x = perm.copy()
                x.insert(i,n)
                result.append(x)
        return result

letters = "abcdefghijklmnopqrstuvwxyz"

def stringify(permutation):
    s = ""
    for i in permutation:
        s += letters[i-1]
    return s

def permutations(n):
    perms = permutation_helper(n)
    result = []
    for perm in perms:
        result.append(stringify(perm))
    return result
