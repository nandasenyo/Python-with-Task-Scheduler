# load library
import numpy as np
import pandas as pd

# random number 0-3 
a=list(np.random.randint(4, size=10))

# random number 0-4
b=list(np.random.randint(5, size=10))

# build dataframe
test28 = pd.DataFrame({'num1':a,'num2':b},columns=['num1','num2'])
test28

# export dataframe to csv file
test28.to_csv('test28.csv',index=False)

print('Done !')