#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a = np.random.randn(5)


# In[2]:


print(a)


# In[3]:


print(a.shape)


# In[4]:


print(a.T)


# In[5]:


print(np.dot(a,a.T))


# In[9]:


a = np.random.randn(5,1)
print(a)


# In[10]:


print(a.T)


# In[11]:


print(np.dot(a,a.T))


# In[ ]:




