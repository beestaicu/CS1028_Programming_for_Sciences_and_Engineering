# ----------------------------------------------------------
# Practical 3
# -----------------------------------------------------------

import sys
import math
import random
# --------------------------------------------------------------
# Questions for Beginners
# --------------------------------------------------------------

# -------------------------------------------------------------
# 1. Does (math.sqrt(2) * math.sqrt(2) == 2) evaluate to True or False?
# a = math.sqrt(2)*math.sqrt(2) == 2
# print(a)
# Answer: False
# --------------------------------------------------------
# 2. Compose a program that takes two positive integers as command-line arguments and
# writes True if either evenly divides the other.

# Answer:
# F = int(sys.argv[1])
# S = int(sys.argv[2])
# if a % b == 0 or b % a == 0:
#     print("True")
# ----------------------------------------------------------
# 3. Compose a program that takes two integers m and d from the command line and writes
# True if day d of month m is between March 20 and June 20, and False otherwise.
# (Interpret m with 1 for January, 2 for February, and so forth.)

# Answer:
# m = int(sys.argv[1])
# d = int(sys.argv[2])
# if m in range(4, 6):
#     print("True")
# elif m == 3 and d in range(20, 32):
#     print("True")
# elif m == 6 and d in range(1, 21):
#     print("True")
# else:
#     print("False")
# ------------------------------------------------------------------
# 4. Compose a program that takes three integer command-line arguments and writes
# ’equal’ if all three are equal, and ’not equal’ otherwise.
#
# Answer:
# F = sys.argv[1]
# S = sys.argv[2]
# T = sys.argv[3]
# if F == S == T:
#     print("equal")
# else:
#     print("not equal")
# ---------------------------------------------------------------------
# 5. Write a code fragment that takes two float command-line arguments, and writes True
# if both are strictly between 0 and 1 and False otherwise.
#
# Answer:
# F = float(sys.argv[1])
# S = float(sys.argv[2])
# if 0 < F < 1  and 0< S < 1:
#     print("True")
# else:
#     print("Flase")
# ------------------------------------------------------------------------
# 6. What is the value of j after each of the following code fragments is executed?
#
# Answer:
# j = 0
# for i in range(0, 10):
#     j += 1
#   print(j)    # 10

# j = 1
# for i in range(0, 10):
#     j += j
#     print(j)  # 1024
#
# for j in range(0, 10):
#     print(j)
#     j += j
#     print(j)    # 18

# ---------------------------------------------------------------
# 7. Compose a program that, using one for loop and one if statement, writes the integers
# from 1000 (inclusive) to 2000 (exclusive) with five integers per line. Hint: use the %
# operator
#
# Answer:
# for i in range(1000,2000):
#     print(i, end= " ")    # print a space after the number
#     if i % 5 == 4:  # 1004,1009,1014, etc.
#         print("")   # print a newline only
# -----------------------------------------------------------------------
# 8. Describe what happens when you invoke rulern.py with an argument that is too large.
# For example, try executing the command python rulern 100.
#
# Answer:   MemoryError
# -----------------------------------------------------------------------
# 9. What are m and n after the following code is executed?
# n = 123456789
# m = 0
# while n != 0:
#     m = (10*n) * (n%10)
#     n //= 10
#     print(m,n)
# Answer:
# 10 0
# -------------------------------------------------------------------------
# 10. Compose a program that takes a command-line argument n and writes all the positive
# powers of 2 less than or equal to n. Make sure that your program works properly for
# all values of n. (Your program should write nothing if n is negative or zero.)
#
# Answer:
# n = int(sys.argv[1])
#
# power_of_2 = 1
#
# while power_of_2 <= n:
#     print(power_of_2)
#     power_of_2 *= 2
# --------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Some More Advanced Questions
# ----------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 1. Order check. Compose a program that takes three floats x, y, and z as command-line
# arguments and writes True if the values are strictly ascending or descending (x < y <
# z or x > y > z), and False otherwise.
#
# Amswer:
# x = float(sys.argv[1])
# y = float(sys.argv[2])
# z = float(sys.argv[3])
# if x < y < z or z < y < x:
#     print("True")
# else:   print("False")
# -------------------------------------------------------------------------------
# 2. Uniform random numbers. Compose a program that writes five uniform random floats
# between 0 and 1, their average value, and their minimum and maximum value. Use
# the built-in max() and min() functions.
#
# Answer:
# a1 = random.random()
# a2 = random.random()
# a3 = random.random()
# a4 = random.random()
# a5 = random.random()
# Max = max(a1, a2, a3, a4, a5,)
# Min = min(a1, a2, a3, a4, a5)
# Average = (a1+a2+a3+a4+a5)/5
# print("Maximum is " + str(Max))
# print("Minmum is " + str(Min))
# print("Average value is " + str(Average))
# -----------------------------------------------------------------------
# 3. Ramanujan’s taxi. S. Ramanujan was an Indian mathematician who became famous
# for his intuition for numbers. When the English mathematician G. H. Hardy came
# to visit him in the hospital one day, Hardy remarked that the number of his taxi was
# 1729, a rather dull number. To which Ramanujan replied, "No, Hardy! No, Hardy! It
# is a very interesting number. It is the smallest number expressible as the sum of two
# cubes in two different ways." Verify this claim by composing a program that takes a
# command line argument n and writes all integers less than or equal to n that can be
# expressed as the sum of two cubes in two different ways. In other words, find distinct
# positive integers a, b, c, and d such that a3 + b3 = c3 + d3. Use four nested for
# loops.
#
# Answer1(really slow implementation):
# n = int(sys.argv[1])
# for a in range(n):
#     for b in range(n):
#         for c in range(n):
#             for d in range(n):
#                 if (a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d) and (a**3 + b**3 == c**3 + d**3):
#                     print(a**3 + b**3)
# -------------------
# Answer2(faster):
# n = int(sys.argv[1])
# # First, find the largest number that we could possibly have as one of the cube.
# # it is the cube root of n.
# largest = int(math.pow(n, 1/3))
# # math.pow lets us take the cube root, int will round it to the integer below.
# sum_of_two_cubes = [0]*(2*largest**3)
# for i in range(largest):
#     for j in range(i+1, largest):
#         k = i**3 + j**3
#         sum_of_two_cubes[k] += 1
# print(sum_of_two_cubes)
# for i in range(n+1):
#     if sum_of_two_cubes[i] >= 2:
#         print(i)
# -----------------------------------------------------------------------------------
# 4. Counting primes. Compose a program that takes a command-line argument n and
# writes the number of primes less than n. Use it to write the number of primes less
# than 10 million. Note: if you are not careful to make your program efficient, it may
# not finish in a reasonable amount of time. Later in Section 1.4, you will learn about a
# more efficient way to perform this computation called the Sieve of Eratosthenes.
#
# Answer(1 function):
# the_number = int(sys.argv[1])
# print(f"The number: {the_number}")
#
# def is_prime(my_number):
#     """Is my_number prime? In other words, is it divisible by any integer lower than itself"""
#     prime =True
#     for divisor in range(2, my_number//2 + 1):
#         remainder = my_number % divisor
#         if remainder == 0:
#             prime = False
#             break   # one such number is enough - we don't need to check further
#     return prime
#     # if prime:
#     #     return True
#     # else:
#     #     return False
#
# if is_prime(the_number):
#     print(f"The number '{the_number}' is prime.")
# else:
#     print(f"The number '{the_number}' is a composite number.")
#
# all_primes = []
#
# for candidate in range(2, the_number):
#     if is_prime(candidate):
#         all_primes.append(candidate)
# print(f"All primes lower than {the_number}: {all_primes}")
# ------------------------------------------
# Answer(2 nested loop)
# the_number = int(sys.argv[1])
# print(f"The number: {the_number}")
#
# all_prime = []
#
# for candidate in range(2, the_number):
#     prime = True
#
#     for divisor in all_prime:
#         if divisor > candidate //2 +1:
#             break
#         remainder = candidate % divisor
#         # print(f"{candidate} % {divisor} = {remainder}")
#         if remainder == 0:
#             prime = False
#             break
#     if prime:
#         all_prime.append(candidate)
#
# print(f"All prime lower than {the_number}: {all_prime}")
# -----------------------------------------------------------------------------
# 5. Pepys’s problem. In 1693 Samuel Pepys asked Isaac Newton which is more likely:
# getting 1 at least once when rolling a fair die six times or getting 1 at least twice when
# rolling it 12 times. Compose a program that could have provided Newton with a quick answer
#
# Answer:

# def die():
#     return random.randrange(1,7)
#
# lista = []
# listb = []
#
# def size(size):
#     for i in range(size):
#         a = die()
#         listb.append(a)
#         if a == 1:
#             lista.append(a)
#
#
# def pro(sizes, time):
#     wins = 0
#     bets = 0
#     for i in range(10000):
#         size(sizes)
#         bets += 1
#         if len(lista)>=time:
#             wins +=1
#         lista.clear()
#         listb.clear()
#     ave = wins/bets
#     print(f"probability {sizes} times for {time} time(s) 1 is: {ave}")
# # pro = wins/bets
# pro(6,1)
# pro(12,2)



