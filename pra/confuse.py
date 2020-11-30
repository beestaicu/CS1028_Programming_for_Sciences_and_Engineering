# binary.py     (misunderstand)
# factors.py    (understand a bit)
# gambler.py    (misunderstand)
# sqrt.py       (misunderstand)
# stdio.py      (misunderstand)




# -----------------------------------------------------------------------
# pra3
# -----------------------------------------------------------------------
# 6.(misunderstand)
# for j in range(0, 10):
#     print(j)
#     j += j
#     print(j)    # 18
# ------------------------------------------------------------------------
# 7.(misunderstand)
# for i in range(1000,2000):
#     print(i, end= " ")    # print a space after the number
#     if i % 5 == 4:  # 1004,1009,1014, etc.
#         print("")   # print a newline only
# -------------------------------------------------------------------------
# advance 3.(understand)(hard)
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
# ----------------
all_prime = []
candidate = 10
for divisor in all_prime:
    if divisor > candidate //2+1:
        break
    print(divisor)