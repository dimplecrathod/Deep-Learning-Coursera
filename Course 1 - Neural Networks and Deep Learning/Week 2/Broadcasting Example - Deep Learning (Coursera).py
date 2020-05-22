#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
A = np.array ([[56.0, 0.0, 4.4, 68.0],
             [1.2, 104.0, 52.0, 8.0],
               [1.8, 135.0,99.0,0.9]])
print(A)


# In[2]:


cal = A.sum(axis=0)
print(cal)


# In[3]:


percentage = 100*A/cal.reshape(1,4)
print(percentage)


# In[7]:


a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
print(c.shape)
print(c)


# In[4]:


a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b
print(c.shape)
print(c)


# In[5]:


a = np.random.randn(4, 3) # a.shape = (4, 3)
b = np.random.randn(3, 2) # b.shape = (3, 2)
c = a*b
print(c.shape)
print(c)


# In[6]:


a = np.random.randn(12288, 150) # a.shape = (12288, 150)
b = np.random.randn(150, 45) # b.shape = (150, 45)
c = np.dot(a,b)
print(c.shape)
print(c)


# In[ ]:




