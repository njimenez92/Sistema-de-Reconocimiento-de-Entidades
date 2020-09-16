#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import re 
import string   
import numpy as np 
import math 
import textwrap
#%matplotlibinline


# In[1]:


def DOI(document):
    
    List_Text = [] # Here we will put the document's text into a separated list
    wanted_DOI = [] # Here will be placed the paper's DOI
    DOI_List = [] # This is the list of DOI's in the document
    
    for word in textwrap.wrap(document,50):
        List_Text.append(word)
    
    for word in List_Text:
        if "doi.org" in word.lower():
            DOI_List.append(word)
        elif "ddi.org" in word.lower():
            DOI_List.append(word)
        elif "ddi.drg" in word.lower():
            DOI_List.append(word)
        elif "doiiorg" in word.lower():
            DOI_List.append(word)
        elif "dxldoilorg" in word.lower():
            DOI_List.append(word)
        elif "dxdoloxg" in word.lower():
            DOI_List.append(word)
        elif "dxrdoirorg" in word.lower():
            DOI_List.append(word)
        elif "dxdoilorg" in word.lower():
            DOI_List.append(word)
        elif "dotorg" in word.lower():
            DOI_List.append(word)
        elif "doilorg" in word.lower():
            DOI_List.append(word)
    
    wanted_DOI.append(DOI_List[0])
    
    return(wanted_DOI)


# In[ ]:





# In[ ]:




