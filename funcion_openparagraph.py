#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd
import matplotlib.pyplot as plt
#%matplotlibinline


# In[3]:


def openparagraph(paper):
    
    text = open(paper,"r",encoding="utf8",errors='ignore')
    text = text.read()
    text = text.lower()
    text_seg = list(filter(lambda x : x != '', text.split('\n\n')))
    

    return(text_seg)

