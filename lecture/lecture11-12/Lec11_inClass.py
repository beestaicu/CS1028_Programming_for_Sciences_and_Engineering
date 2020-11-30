# 2019-10-24

# Daniel Vogel
# CS1028 Programming for Science and Engineering
# University of Aberdeen
#-------------------------------------------------------------------

# Lecture 11
# these are my code scribblings in class 

#%%



#%% 
# input arbitrarily many numbers:
# first version, 
numbers = []
a = int(input("Give me a number: "))
numbers = numbers + [a]

a_str = input("Give me a number: ")
while a_str != '':
    a = int(a_str)
    numbers = numbers + [a]
    a_str = input("Give me a number: ")
    


#%%
# better version: exception handling:
# Note: This is not the version on the slides. 
# In an community effort during class, the latter was changed to this version,
# which just ignores non-integer input (rather than stopping to read in)  . 

numbers = []
a_str = input("Give me a number (or simply 'Enter' to end reading) : ")

while a_str != '':
    try:
        a = int(a_str)
        numbers = numbers + [a]
    except ValueError:
        print("Last input was not a number. I ignore the input.")
    a_str = input("Give me a number (or simply 'Enter' to end reading) : ")


#%%
# make up your own data    
    
import random    

# this always gives the same results    
random.seed(24102019)
rN = []
for i in range(10):
    r = random.random()
    rN = rN + [r] 
print(rN)


#%%
# sometimes you want integers:
# this produces 20 random integers from the range 0 to 10 (boundaries included)
# (drawn from a discrete uniform distribution)

import random    
    
rN = []
for i in range(20):
    r = random.randint(0,10)
    rN = rN + [r] 
print(rN)


#%%
#write to file

import numpy as np
import matplotlib.pyplot as plt


#%% 
# writes the numbers in scientific notation
np.savetxt(fname="someNumbers.txt",X=rN)

#%%

# some formatting (exactly 12 digits after the decimal point)
np.savetxt(fname="someNumbers.txt",X=rN,fmt="%15.12f")

# this just saves zeros: (d meaning "integer", this apparently rounds)
#np.savetxt(fname="someNumbers2.txt",X=rN,fmt="%d")


#%%
# reading the numbers back in 
Data_arr = np.loadtxt("someNumbers.txt")
Data = list(Data_arr)



#%%
# the slightly more sophisticated example:
# put the file "AberdeenDyce.txt" in the current working directory
# or add the path to fileName
import numpy as np
import matplotlib.pyplot as plt

fileName = "AberdeenDyce.txt"
Data_arr = np.loadtxt(fileName,skiprows=1)

ColNames_arr = \
np.genfromtxt(fileName,dtype="str",skip_footer=12,delimiter='\t')
colNames = list(ColNames_arr)

#%%


month = list(Data_arr[:,0])
maxTemp = list(Data_arr[:,1])
minTemp = list(Data_arr[:,2])

rain = list(Data_arr[:,5])
sun = list(Data_arr[:,4])

plt.figure()
plt.plot(month,maxTemp)
plt.plot(month,minTemp)


#%%
# another plot: sunshine hours vs rainy days
plt.figure()
plt.plot(month,rain)
plt.plot(month,sun)





