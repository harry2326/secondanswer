#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_csv("filedata.csv")
print('filedata')
setosa = data['demark'] == 'demark-1'
print(data[setosa].describe())
print('\ndemark-1')

