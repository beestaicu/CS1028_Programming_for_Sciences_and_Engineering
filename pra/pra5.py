# -------------------------------------------------------
# practical 5
# ---------------------------------------------------------

# 1. Compose a program that reads in integers (as many as the user enters) from standard
# input and writes the maximum and minimum values to standard output.
# Solution: See maxmin.py

# Way1:(use stdio.py) -----------------------------------------

# import stdio
# numbers = []
#
# while not stdio.isEmpty():
#     a = stdio.readInt()
#     numbers.append(a)
#
# minim = numbers[0]
# for n in numbers:
#     if n < numbers[0]:
#         minim = n
# print(numbers)
# print(minim)

# way2:(not use stdio.py) -----------------------------------------
#
# numbers = []
#
# a = int(input("Give me a number: "))
# numbers = numbers + [a]
# str_a = input("Give me a number: ")
#
# while str_a != "":
#     a = int(str_a)
#     numbers = numbers + [a]
#     str_a = input("Give me a number: ")
#
# minim = numbers[0]
# maxim = numbers[0]
# for n in numbers:
#     if n < minim:
#         minim = n
#     elif n > maxim:
#         maxim = n
#
#
# print(numbers)
# print("The minimum number is: {}, and the maximum is {}.".format(minim,maxim))

# ---------------------------------------------------------------
# 2. Modify your program from the previous exercise to insist that the integers must be
# positive (by prompting the user to enter positive integers whenever the value entered
# is not positive).

# numbers = []
#
# a = int(input("Give me a positive number: "))
# if a <= 0:
#     a = int(input("Positive: "))
#
# str_a = str(a)
#
# while str_a != "":
#     if int(str_a) >= 0:
#         a = int(str_a)
#         numbers = numbers + [a]
#         str_a = input("Give me a positive number: ")
#     else:
#         str_a = input("must Positive: ")
#
#
# minim = numbers[0]
# maxim = numbers[0]
# for n in numbers:
#     if n < minim:
#         minim = n
#     elif n > maxim:
#         maxim = n
#
#
# print(numbers)
# print("The minimum number is: {}, and the maximum is {}.".format(minim, maxim))

# ------------------------------------------------------------------------------
# 3. Compose a program that accepts an integer n from the command line, reads n floats
# from standard input, and writes their mean (average value) and standard deviation
# (square root of the sum of the squares of their differences from the average, divided
# by n). Solution: See stats2.py.

# import sys
# import math
# n = int(sys.argv[1])
# list = []
#
# for i in range(n):
#     a = input("Give me a float: ")
#     list.append(float(a))
#
# total = 0
#
# for i in list:
#     total += i
# mean = total / n
# print(f"Mean is: {mean}.")
#
# sum = 0
#
# for i in list:
#     sum += (mean-i)**2
# mean_of_sum = sum / n
# standard_deviation = math.sqrt(mean_of_sum)
# print(f"standard_deviation is: {standard_deviation}")

# -----------------------------------------------------------------
# 4. Extend your program from the previous exercise to create a filter that writes all the
# values that are further than 1.5 standard deviations from the mean.


# import sys
# import math
# n = int(sys.argv[1])
# list = []
#
# for i in range(n):
#     a = input("Give me a float: ")
#     list.append(float(a))
#
# total = 0
#
# for i in list:
#     total += i
# mean = total / n
# print(f"Mean is: {mean}.")
#
# sum = 0
#
# for i in list:
#     sum += (mean-i)**2
# mean_of_sum = sum / n
# standard_deviation = math.sqrt(mean_of_sum)
# print(f"standard_deviation is: {standard_deviation}")
#
# over_standard = []
# for n in list:
#     if abs(standard_deviation-n) > 1.5:
#         print(standard_deviation-n)
#         over_standard.append(n)
#
# print(over_standard)

# -------------------------------------------------------------
# 5. Compose a program that reads in a sequence of integers and writes both the integer
# that appears in a longest consecutive run and the length of the run. For example, if
# the input is 1 2 2 1 5 1 1 7 7 7 7 1 1, then your program should write Longest run: 4
# consecutive 7s.
# Solution: See longestrun.py.

# import sys
# numbers = sys.argv[1:]
# print(f"List of numbers to be processed: {numbers}")
# current_run = [numbers[0]]
# best_run = []
# for i in range(1, len(numbers)):
#     if numbers[i] == numbers[i-1]:
#         current_run.append(numbers[i])
#     else:
#         current_run = [numbers[i]]
#     if len(current_run) > len(best_run):
#         best_run = current_run[:]
# print(f"longest run: {best_run}")
# the_number = best_run[0]
# run_length = len(best_run)
# print(f"({run_length} consecutive {the_number}s)")

# --------------------------------------------------------
# 6. Compose a filter that reads in a sequence of integers and writes the integers, removing
# repeated values that appear consecutively. For example, if the input is 1 2 2 1 5 1 1 7
# 7 7 7 1 1 1 1 1 1 1 1 1, your program should write 1 2 1 5 1 7 1.

# import sys
# numbers = sys.argv[1:]
# print(f"List of numbers to be processed: {numbers}")
# current_run = [numbers[0]]
# best_run = []
# list = [numbers[0]]
#
# for i in range(1, len(numbers)):
#     if numbers[i-1] == numbers[i]:
#         current_run.append(numbers[i])
#     else:
#         list.append(numbers[i])
#
#     if len(current_run) > 1:
#         if current_run[len(current_run)-1] != current_run[len(current_run)-2]:
#             n = current_run[len(current_run)-1]
#             current_run.clear()
#             current_run.append(n)
#             # print(current_run,i)
# # print(len(numbers))
#
# print(list)

# -------------------------------------------------------------
# 7. Compose a program that accepts a command-line argument n, reads from standard
# input n-1 distinct integers between 1 and n, and determines the missing value.

# import sys
# n = int(sys.argv[1])
# store = []
# list = []
# for i in range(n-1):
#     a = int(input(f"Give me a number(from 1 to {n}): "))
#     if 1 > a or a > n:
#         a = int(input(f"(from 1 to {n}): "))
#     store.append(a)
#
# print(f"The number you input is: {store}")
#
# for i in range(1,n+1):
#     list.append(i)
# # print(list)
# for i in range(len(store)):
#     while store[i] in list:
#         list.remove(store[i])
#         # print(store[i])
#
# print(f"The missing value is {list[0]}.")

# -----------------------------------------------
# 8. Compose a program named wordcount.py that reads text from standard input and
# writes to standard output the number of words in the text. For the purpose of this
# exercise, a word is a sequence of non-whitespace characters that is surrounded by
# whitespace. For example, the command python wordcount < tale.txt should write
# 139043.
# Solution: See wordcount.py

# import stdio
# count = 0
#
#
# while not stdio.isEmpty():
#     word = stdio.readString()
#     count += 1
#
# print(f"Number of strings = {count}.")

# ----------------------------------------------------
# 9. Suppose that the file input.txt contains the two strings F and F. What does the
# following command do? See the exercises from Section 1.2 for more information on
# dragon curves. Here is the Python program dragon3.py.
# python dragon3.py < input.txt | python dragon3.py | python dragon3.py

# Answer: repeat strings

# ----------------------------------------------------
# 10. Compose a filter tenperline.py that reads a sequence of integers between 0 and 99
# and writes 10 integers per line, with columns aligned. Then compose a program randomintseq.py
# that takes two command-line arguments m and n and writes n random integers between 0 and m-1.
# Test your programs with the command python randomintseq 100 200 | python tenperline.py.

# import stdio
# import sys
# import random
# count = 0
# m = int(sys.argv[1])
# n = int(sys.argv[2])
# z = int(sys.argv[3])
# numbers = []
# for i in range(z):
#     numbers += [random.randrange(m,n)]
# print(numbers)
# while not stdio.isEmpty():
#     # number = stdio.readInt()
#     stdio.write(numbers)
#     stdio.write(" ")
#     count += 1
#     if count == 10:
#
#         stdio.writeln()
# print(f"Number of numbers = {count}.")