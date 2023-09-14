#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

import matplotlib.pyplot as plt
import seaborn as sns

import os
import time 
import re

import warnings
warnings.filterwarnings('ignore')


# In[10]:


# Loading the data
data = pd.read_excel('news_share_data.xlsx')
data


# In[11]:


df = data.copy()


# In[12]:


df.shape


# In[15]:


#data processing

'Pune, Maharashtra, India'.split(',')[2].strip()


# In[17]:


df['Location'].apply(lambda x: x.split(',')[2].strip())
df['Location'].apply(lambda x: x.split(',')[0].strip())


# In[18]:


# Extracting State and Country separately from the Location Column
df['City'] = df['Location'].apply(lambda x: x.split(',')[0].lower().strip())
df['State'] = df['Location'].apply(lambda x: x.split(',')[1].lower().strip())
df['Country'] = df['Location'].apply(lambda x: x.split(',')[2].lower().strip())
df.head(3)


# In[ ]:




