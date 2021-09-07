#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


data = pd.read_excel('C:\\Users\\vrind\\Downloads\\Directors data.xlsx',usecols="A,B")  #import excel file 
print(data)


# In[3]:


for i in data['Director Name']:
    print(data[data["Director Name"] == i])  # check column with Directors Name 
    print("director name is", i)
    print("--------")


# In[21]:


print(data[data["Director Name"] =='SURESH VENKATACHARI'].head())

