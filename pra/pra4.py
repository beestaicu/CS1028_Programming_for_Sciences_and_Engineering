# ------------------------------------------
# practical 4
# --------------------------------------------
import math
import sys
import random
import stdio
import stdarray
# -------------------------------------------
# 1 Questions for Beginners
# ----------------------------------------------

# 1. Compose a program that creates a one-dimensional array a containing exactly 1000
# integers, and then attempts to access a[1000]. What happens when you run the
# program?

# a = stdarray.create1D(1000,0)
# print((a[1000]))
# IndexError: list index out of range

# -------------------------------------------------
# 2. Given two vectors of length n that are represented with one-dimensional arrays,
# compose a code fragment that computes the Euclidean distance between them (the square
# root of the sum of the squares of the differences between corresponding elements).

# vector1 = [20, 2, 11, 15, 2, 4, 12]
# vector2 = [12, 5, -2, 77, 2, 23, 0]
# n = len(vector1)
# sum = 0
#
# for i in range(n):
#     the_squares_of_differences = (vector1[i] - vector2[i])**2
#     sum += the_squares_of_differences
# root_of_sum = math.sqrt(sum)
# print(root_of_sum)

# ------------------------------------------
# 3. Compose a code fragment that reverses the order of a one-dimensional array of floats.
# Do not create another array to hold the result. Hint: Use the code provided earlier in
# this web page for exchanging two elements.

a = [.1, .2, .3, .4, .5]
n = len(a)
b = n //2
for i in range(b):
    temp = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = temp
print(a)

# --------------------------------------
# 4. What is wrong with the following code fragment?
# a = []
# for i in range(10):
#     a[i] = i * i
# IndexError: list assignment index out of range

# -----------------------------------------
# 5. Compose a code fragment that writes the contents of a two-dimensional array of
# bools, using * to represent True and a space to represent False. Include row and
# column numbers

# a = [[True, False],[True, False]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         row = a[i][j]
#         if row:
#             content = "*"
#         else:
#             content = " "
#         print(f"Row{i},column{j} is {content}.")

# --------------------------------------------------

# 6. What does the following code fragment write?
# It will print out 0123443210 line by line

# --------------------------------------------------
# 7. What is a[] after executing the following code fragment?
# n = 10
# a = [0, 1]
# for i in range(2, n):
#     a += [a[i -1] + a[i-2]]
#     print(a)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ---------------------------------------------------------------
# 8. Compose a program that takes an integer command-line argument n and writes n poker
# hands (five cards each) from a shuffled deck, separated by blank lines.
# n = int(sys.argv[1])
# hand_size = 5
#
# suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#
# cards = []
#
# for suit in suits:
#     for value in values:
#         cards.append([suit, value])
#
#
# random.shuffle(cards)
#
#
# for i in range(n):
#     print(f"hand = {i}", end="\n")
#     for j in range(hand_size):
#         card = cards.pop(0)
#         suit = card[0]
#         value = card[1]
#         print(f"suit={suit}, value={value}.", end="\n")
#     print("")

# ---------------------------------------------------------
# 9. Compose code fragments to create a two-dimensional array b[][] that is a copy of an
# existing two-dimensional array a[][], under each of the following assumptions:
# a is square.
# a is rectangular.
# a may be ragged.

# anwers:

# square = [[1, 2],[3, 4]]
# num_row= len(square)
# num_column = len(square)
# copy = []
# for i in range(num_row):
#     row = []
#     for j in range(num_column):
#         a = square[i][j]
#         row.append(a)
#     copy.append(row)
# print(copy)
#
# rectangular = [[1,2,3],[4,5,6]]
# num_row = len(rectangular)
# num_column = len(rectangular[0])
# copy = []
# for i in range(num_row):
#     row = []
#     for j in range(num_column):
#         a = rectangular[i][j]
#         row.append(a)
#     copy.append(row)
# print(copy)
#
# ragged = [[1],[2,3],[1,2,3,4]]
# copy = []
# for i in range(len(ragged)):
#     row = []
#     for j in range(len(ragged[i])):
#         a = ragged[i][j]
#         row.append(a)
#     copy.append(row)
# print(copy)


# ragged = [[1],[2,3],[1,2,3,4]]
# copy = []
# for i in ragged:
#     row = []
#     for v in i:
#         row.append(v)
#     copy.append(row)
# print(copy)



# -------------------------------------------------
# 10. Compose a code fragment to write the transposition (rows and columns changed) of
# a two-dimensional array. For the example, when given this two-dimensional array of
# integers:

# array = [[99, 85, 98], [98,57,78]]
# num_row = len(array)
# num_column = len(array[0])
# copy = []
#
# for i in range(num_column):
#     row = []
#     for j in range(num_row):
#         a = array[j][i]
#         row.append(a)
#     copy.append(row)
# print(copy)

# -------------------------------------


# -------------------------------------
# 2 Some More Advanced Questions
# --------------------------------------

# -----------------------------------------------
# unsolved
# 1. Longest plateau. Given an array of integers, compose a program that finds the length
# and location of the longest contiguous sequence of equal values where the values of
# the elements just before and just after this sequence are smaller.

# Answer:
# Notion: my code suitable for have one and only have one contiguous sequence.

# way 1:
# location = []
# array = [3,3,3,4]
# n = len(array)
# count = 0
# for i in range(0,n-1):
#     if array[i] == array[i+1] and (array[i-1] != array[i]):
#         location.append(i)
#     elif (array[i] != array[i +1] and array[i] == array[i-1]) or (array[i] == array[i-1] and i == n-1):
#         location.append(i)
# count = location[1] - location[0] + 1
#
# print(location)
# print(count)
# result:   [0,2] 3




# way2:

# list =[]
# location = []
# num = []
# array = [2,3,3,3,2,4,4,4,4,2]
# n = len(array)
# count = 0

# for i in range(0, n-1):
#     if array[i] == array[i+1]:
#         list.append(i)
#         num.append(array[i])
#         count += 1
#     if len(num) > 1:
#         if num[0] != num[1]:
#             num.pop(1)
#             list.pop()
#             count -= 1
#             break
#         else:
#             num.pop(0)
#
# location.append(list[0])
# location.append(list[len(list)-1]+1)
# count += 1
#
# print("-"*8)
# print(num)
# print(list)
# print(location)
# print(count)
#
# print(f"number {num[0]} repeat {count} times in location {location}.")
# # result: number 3 repeat 3 times in location [1, 3].


# --------------------------------------------------
# unsolved
# 2. Empirical shuffle check. Run computational experiments to check that our shuffling
# code works as advertised. Compose a program that takes integer command-line arguments m and n,
# does n shuffles of an array of size m that is initialized with a[i] = i
# before each shuffle, and writes an m-by-m table such that row i gives the number of
# times i wound up in position j for all j. All entries in the array should be close to n/m.
# m = int(sys.argv[1])
# n = int(sys.argv[2])
# a = []      # a[i] = i
# res =[]     # for resit the array as a
#
# for i in range(m):
#     a.append(i) # a[i] = i
# res = a.copy()
#
# for i in range(n):
#     random.shuffle(a)
#     print(a)
#     # i can't understand how to print m-m table that i gives number of times of i wound up
#     # in position j for all j.
#     a = res.copy()
#
# print(n/m)

# ---------------------------------------------------
# 3. Music shuffling. You set your music player to shuffle mode. It plays each of the n
# songs before repeating any. Compose a program to estimate the likelihood that you
# will not hear any sequential pair of songs (that is, song 3 does not follow song 2, song
# 10 does not follow song 9, and so on).
# a= [1,2,3,4,5,6,7,8,9,10]     # n = 9
# res = a.copy()
# count = 0
# win = 0
# m = 10000
# random.shuffle(a)
# print(a)
# print(res)
# for i in range(m):
#     for i in range(len(a)-1):
#         count += 1
#         if a[i] != a[i+1]+1 and a[i] != a[i+1]-1:
#             win += 1
#     a = res.copy()
#     random.shuffle(a)
#
# print(win)
# print(count)
#
# print(win/count)

# ----------------------------------------
# 4. Minima in permutations. Compose a program that takes an integer n from the command line,
# generates a random permutation, writes the permutation, and writes the
# number of left-to-right minima in the permutation (the number of times an element
# is the smallest seen so far). Then compose a program that takes integers m and n
# from the command line, generates m random permutations of size n, and writes the
# average number of left-to-right minima in the permutations generated. Extra credit:
# Formulate a hypothesis about the number of left-to-right minima in a permutation of
# size n, as a function of n.

# n = sys.argv[1]
# a = stdarray.create1D(n,0)