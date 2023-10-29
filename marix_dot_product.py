#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #performs marix operations


# In[2]:


revenue = np.array([[180,200,220],[24,36,40],[12,18,20]])
expenses = np.array([[80,90,100],[10,16,20],[8,10,10]]) #represented as 1st row,2nd row ,3rd row


# In[6]:


#Calculate profit/loss from revenue and expenses


# In[3]:


profit = revenue - expenses
profit #numpy considers each as matrix


# In[4]:


#Calculate total sales from units and price per unit using matrix multiplication


# In[5]:


price_per_unit = np.array([1000,400,1200])
units = np.array([[30,40,50],[5,10,15],[2,5,7]])


# In[7]:


price_per_unit*units


# In[8]:


#array([[30000, 16000, 60000],
#       [ 5000,  4000, 18000],
#       [ 2000,  2000,  8400]])
#In above case numpy is using broadcasting so it expands price_per_unit array from 1 row, 3 columns to 3 row and 3 columns. Correct way to do matrix multiplication is to use dot product as shown below


# In[9]:


np.dot(price_per_unit,units)#for dot product


# In[ ]:




