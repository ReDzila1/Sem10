import random
import pandas as pd
import numpy as np
lst = ['robot'] * 10
lst += ['human'] * 10
data = pd.DataFrame({'whoAmI':lst}).to_numpy()
#data.head()
#print(data)
#data['tmp'] = 1
#data.set_index([data.index, 'whoAmI'], inplace=True)
#data = data.unstack(level=-1, fill_value = 0).astype(int)
#data.columns = data.columns.droplevel()
#data.columns.name = None


A = [[0, "robot", "human"],
     [1,0,0], 
     [2,0,0], 
     [3,0,0], 
     [4,0,0],
     [5,0,0], 
     [6,0,0], 
     [7,0,0], 
     [8,0,0], 
     [9,0,0], 
     [10,0,0], 
     [11,0,0], 
     [12,0,0], 
     [13,0,0], 
     [14,0,0], 
     [15,0,0], 
     [16,0,0], 
     [17,0,0], 
     [18,0,0], 
     [19,0,0], 
     [20,0,0]]

n = 0
b = 0
c = 1

for i in range(0, len(data)):
    if data[i][0] == "robot":
        A[c][1] += 1
    elif data[i][0] == "human":
        A[c][2] += 1

    c += 1

data = pd.DataFrame({'RobOrHum':A})

for i in range(0, len(A)):
    print(A[i][0], A[i][1], A[i][2], end='\n')


