# -----------------------------------
# practical 7
# -----------------------------------
import math

# 1. Compose a function max3() that takes three int or float arguments and returns the
# largest one.

def max3(a, b, c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    elif b>=c:
        return b
    else:
        return c
# print(max3(2,2,1))

# 2. Compose a function odd() that takes three bool arguments and returns True if an
# odd number of arguments are True, and False otherwise.

def odd(a,b,c):
    if a and not b and not c:
        return True
    elif not a and b and c:
        return True
    elif not a and not b and c:
        return True
    elif a and b and c:
        return True
    else:
        return False
# print(odd(False,False,True))

def odd_2(a,b,c):
    return (a and not b and not c) or (not a and b and not c) or \
           (not a and not b and c) or (a and b and c)

# print(odd_2(False,True,True))


def odd_3(a,b,c):
    sum = a + b + c
    return sum % 2 == 1

odd_3(1,0,1)

# 3. Compose a function majority() that takes three bool arguments and returns True
# if at least two of the arguments are True, and False otherwise. Do not use an if
# statement.

def majority(a,b,c):
    sum = a + b + c
    return sum >=2

# print(majority(0,0,1))

def majority_2(a,b,c):
    return (a and b and not c) or (a and not b and c) or (not a and b and c )

# print(majority(False,False, True))

# 4. Compose a function areTriangular() that takes three numbers as arguments and
# returns True if they could be the sides of a triangle (none of them is greater than
# or equal to the sum of the other two), and False otherwise.

def areTriangular(a, b, c):

    return (a+b > c) and (a+c > b) and (b+c > a)

# print(areTriangular(3,4,5))

# 5. Compose a function sigmoid() that takes a float argument x and returns the float
# obtained from the formula: 1/(1 − e^(−x)).

def sigmoid(x):
    return 1/(1-(math.exp((-x))))

# print(sigmoid(2))

# 6. Compose function lg() that takes an integer n as an argument and returns the
# base-2 logarithm of n. You may use Python’s math module.

def lg(n):
    return math.log(n)/math.log(2)

# print(lg(2))

def lg_2(n):
    return math.log(n,2)
# print(lg(2))

def lg_3(n):
    return math.log2(n)
# print(lg_3(2))

# 7. Compose a function lg() that takes an integer n as an argument and returns the
# largest integer not larger than the base-2 logarithm of n. Do not use the standard
# Python math module.
def lg(x):
    n = 0
    while 2**n <= x:
        n += 1
    return n - 1
# print(lg(2))

# 8. Compose a function signum() that takes a float argument n and returns -1 if n
# is less than 0, 0 if n is equal to 0, and +1 if n is greater than 0.

def signum(n):
    if n <= 0:
        return -1
    elif n == 0:
        return 0
    else:
        return +1

# print(signum(-4))

# ------------------------------------------------------

# Advanced Questions:

# 1. Write a function that takes a positive integer as input and returns its prime
# decomposition as a list of numbers.
# Prime decomposition: Any positive integer n can, in a unique way, be written as a
# product of prime numbers. This is called the prime decomposition of n. Examples:
# 12 = 2 ∗ 2 ∗ 3
# 13 = 13
# 14 = 2 ∗ 7
# 15 = 3 ∗ 5
# 16 = 2 ∗ 2 ∗ 2 ∗ 2
# 17 = 17
# Hint: : Practical 4(is practical 3) had a question on counting primes. Its solution
# may come in handy here.

# Answer 1:(function)
a = []
def dec_prime(number):
    for i in range(2, number+1):
        if is_prime(i):
            while  number % i == 0:
                number /= i
                a.append(i)
    print(a)

def is_prime(my_number):
    prime = True
    for divisor in range(2, my_number//2 + 1):
        remainder = my_number % divisor
        if remainder == 0:
            prime = False
            break
    return prime

# dec_prime(16)

# 2. If you still do not feel sufficiently challenged: Euler’s totient function.
# Euler’s totient function is an important function in number theory:
# ϕ(n) is defined as the number of positive integers less than or equal
# to n that are relatively prime with n (no factors in common with n other than 1).
# Compose a function that takes an integer argument n and returns ϕ(n).
# Include global code that takes an integer from the command line,
# calls the function, and writes the result.

def phi(n):
    phi = 0
    a = []

    for i in range(2, n+1):
        if is_prime(i):
            a.append(i)
    for i in range(1,n+1):
        co_prime = True
        for h in a:
            print(h,i,n)
            if i % h == 0 and n % h == 0:
                co_prime = False
                print(co_prime)
        if co_prime:
            phi += 1
    print(phi)
    print(a)

phi(10)