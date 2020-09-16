#!/usr/bin/env python
# coding: utf-8

# In[1]:



import re
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


def opentext(paper):
    
    text = open(paper,"r",encoding="utf8",errors='ignore')
    text = text.read()
    text = text.lower()
    text_seg = text.split('\n\n') # Separates the whole document into paragraphs
    
    
    for i in range(0,len(text_seg)):
        if "\n" in text_seg[i]:
            text_seg[i] = text_seg[i].replace("\n",'') # We removed "\n" from the strings that compose the text
    
    return(text_seg)


# In[ ]:





# In[ ]:




