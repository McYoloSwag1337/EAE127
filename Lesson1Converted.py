# %%
#innformation
name="Ephraim Aung"
city="Gilroy"
SSN=1234

#Print individual
print("Name=", name)
print("City=",city)
print("SSN=", SSN)

#Print together
print("I'm {}, I'm from {}, and my SSN is {}". format(name,city,SSN))

# %%
# ID Arrays, for loops, and conditional statements

Info=[name,city,SSN]
#print(Info[0], Info [1], Info[2])
print(type(name))


# For loop
#for i in Info:
#    print(i)
    
for i in range(0,3): #range(starting index, amount of indexes to go through)
    if type(Info[i]) == str:
        print(Info[i])

# %%
# Numpy library

import numpy as np

x=np.linspace(0,5,6) #linspace(start value, end value, amount of elements)
print(x)
y=np.zeros(11) #zeros (amount of elements)
#print(y)
#z=np.arange(0,5,0.5) #arange(start value, end value, difference in value between step) (end elements will not be included unless you dont add extra step)
z=np.arange(0,5+0.5,0.5)
#print(z)

print(x[0:2]) #this will print the first two entries in the list (Index 0 and 1)
print(x[:-2]) #this will print all but the last two values of the list (Index 4 and 5)
print(x[1:]) #this will pring all but the first value of the list (Index 0)

# %%
# 2D Arrays

X=np.meshgrid(x,x)
#print(X[0])
X=X[0]
print(X)
#print(X[0])
#print((X[0])[1])

from tabulate import tabulate 
#print(tabulate(X))

showRow=[
    ['Row 1', X[0]],
    ['Row 2', X[1]],
    ['Row 3', X[2]],
    ['Row 4', X[3]],
    ['Row 5', X[4]],
    ['Row 6', X[5]],
]

#print(tabulate(showRow))

column=[(X[0])[0],(X[1])[0],(X[2])[0],(X[3])[0],(X[4])[0],(X[5])[0]]

def getColumn(two_array, column_num):
    amount_column = len(two_array)
    temp_column = np.zeros(amount_column)
    for i in range(0,6):
        temp_column[i]=X[i][column_num]
    return temp_column

showCol=[
    ['Column 1', getColumn(X,0)],
    ['Column 2', getColumn(X,1)],
    ['Column 3', getColumn(X,2)],
    ['Column 4', getColumn(X,3)],
    ['Column 5', getColumn(X,4)],
    ['Column 6', getColumn(X,5)],
]

print(tabulate(showCol))

np.append()

# %%
#graph airfoil need airfoil naca csv
#on graph vertical is y but in data it is z
import pandas as pd 
filename = 
foil0012=pd.read_csv(filename, delim_whitespace=True, skiprows-1, name=['x','z'])
foilx= foil0012['x']
foilz= foil0012['z']


import matplotlib.pyplot as graph

graph.figure()
graph.plot(x,z)
graph.title("NACA 0012 Geometry")
graph.xlabel("x/c")
graph.ylabel("z/c")
graph.legend(['0012 airfoil'])
graph.axis("equal")
graph.xlim([0,1])
graph.show()




