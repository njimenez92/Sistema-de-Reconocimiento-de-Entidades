#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def compare (Data,Reference):
    
    if (Data==0):
        Percentage = 0
    else:
        Percentage = (Data/Reference)*100
    return(Percentage)

