#!/usr/bin/env python
# coding: utf-8

# In[11]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.


# In[8]:


import pandas as pd
df = pd.read_csv('../input/titanic/gender_submission.csv')


# In[9]:


df


# In[10]:


df.to_csv('submission.csv', index=False)


# In[12]:


train = pd.read_csv('../input/titanic/train.csv')
test = pd.read_csv('../input/titanic/test.csv')
gender_submission = pd.read_csv('../input/titanic/gender_submission.csv')


# In[13]:


print (train.shape)


# In[14]:


print (test.shape)
print (gender_submission.shape)


# In[15]:


df.info()


# In[16]:


train.info()


# In[17]:


train.head()


# In[18]:


train.isnull().sum()


# In[19]:


test.isnull().sum()


# In[20]:


df_full = pd.concat([train, test], axis=0, sort=False)


# In[21]:


print (df_full.shape)
df_full.describe()


# In[22]:


import pandas_profiling as pdp
pdp.ProfileReport(train)


# In[23]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.countplot(x='Survived', data=train)
plt.title('count of survived and dead')
plt.xticks([0,1],['dead', 'survived'])
plt.show()

display(train['Survived'].value_counts())
display(train['Survived'].value_counts()/len(train['Survived']))

