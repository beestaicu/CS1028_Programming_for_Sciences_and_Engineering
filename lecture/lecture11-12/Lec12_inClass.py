# Friday 2019-10-25

# Daniel Vogel
# CS1028 Programming for Science and Engineering
# University of Aberdeen
#-------------------------------------------------------------------

# Lecture 12
# these are my code scribblings in class 

#%%


import numpy as np
import matplotlib.pyplot as plt


#%%

# put the .txt file in the current working directory
Data_arr = np.loadtxt("AberdeenDyce.txt",skiprows=1)
month = list(Data_arr[:,0])
maxTemp = list(Data_arr[:,1])

plt.figure()
plt.plot(month,maxTemp)


#%%

minTemp = list(Data_arr[:,2])

plt.figure()
fontText = {'family': 'serif', 'size': 18}
fontTitle = {'family': 'serif', 'size': 26}
plt.rc('font', **fontText)
ax = plt.axes()
ax.xaxis.set_major_locator\
(plt.FixedLocator([1,2,3,4,\
5,6,7,8,9,10,11,12]))
ax.xaxis.set_major_formatter\
(plt.FixedFormatter(["Jan","Feb"\
,"Mar","Apr","May","Jun","Jul",\
"Aug","Sep","Oct","Nov","Dec"]))
ax.grid()
plt.plot(month,maxTemp,"r-o",label="max")
plt.plot(month,minTemp,"b-o",label="min")
plt.legend()
plt.xlim(0,13)
plt.ylim(-4,24)
plt.ylabel('Temperature (°C)')
plt.title('Monthly temperatures at Aberdeen Dyce',fontdict=fontTitle)
plt.show()

#%%

# lists

L = [3,4,17]
K = [3,4,"cheese",[45,"rter"]]
#
# L[3]

#%%
# basic list functions

R = list(range(1,10))
len(R)

#%%
# list slicing

print(R[0:4])
print(R[4:-2])



#%%
# aliasing

S = R
R[0] = "hello"
print(S)



