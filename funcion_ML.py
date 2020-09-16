#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re 
import string   
import pandas as pd 
import numpy as np 
import math 
import textwrap


# In[2]:


def ML (df_Efficiency,df_GAP,df_SynthesisMethod,df_SubstrateTemp,df_Annealing,
        df_Absorption,Global_Efficiency,Global_GAP,Global_SynthesisMethod,
        Global_SubstrateTemp,Global_Annealing,Global_Absorption):
  
     # Deleting Unnecesary columns 
    Union_Efficiency = pd.concat([df_Efficiency,Global_Efficiency], axis=0)# Connecting Both dataframes into "union"
    del Union_Efficiency['Frequency'] # Deleting "Union" unnecesary columns
    duplicateRows_Efficiency = Union_Efficiency['Word'].duplicated(keep=False)# Finding Duplicate words 
    final_Efficiency = Union_Efficiency[duplicateRows_Efficiency]  # Filtering Dataframe
    final_Efficiency = final_Efficiency.groupby(["Word"]).sum().reset_index()
    len_Efficciency = len(final_Efficiency)  # Finding the number of repeating words
    
    
    
    Union_GAP = pd.concat([df_GAP,Global_GAP], axis=0)
    del Union_GAP['Frequency']
    duplicateRows_GAP = Union_GAP['Word'].duplicated(keep=False) 
    final_GAP = Union_GAP[duplicateRows_GAP]
    final_GAP = final_GAP.groupby(["Word"]).sum().reset_index()
    len_GAP = len(final_GAP)
    

    
    Union_SynthesisMethod = pd.concat([df_SynthesisMethod,Global_SynthesisMethod], axis=0)
    del Union_SynthesisMethod['Frequency']
    duplicateRows_SynthesisMethod = Union_SynthesisMethod['Word'].duplicated(keep=False)
    final_SynthesisMethod = Union_SynthesisMethod[duplicateRows_SynthesisMethod]
    final_SynthesisMethod = final_SynthesisMethod.groupby(["Word"]).sum().reset_index()
    len_SynthesisMethod = len(final_SynthesisMethod)
    
    
    
    Union_SubstrateTemp = pd.concat([df_SubstrateTemp,Global_SubstrateTemp], axis=0)
    del Union_SubstrateTemp['Frequency']
    duplicateRows_SubstrateTemp = Union_SubstrateTemp['Word'].duplicated(keep=False)
    final_SubstrateTemp = Union_SubstrateTemp[duplicateRows_SubstrateTemp]
    final_SubstrateTemp = final_SubstrateTemp.groupby(["Word"]).sum().reset_index()
    len_SubstrateTemp = len(final_SubstrateTemp)
    
    
    
    Union_Annealing = pd.concat([df_Annealing,Global_Annealing], axis=0)
    del Union_Annealing['Frequency']
    duplicateRows_Annealing = Union_Annealing['Word'].duplicated(keep=False) 
    final_Annealing = Union_Annealing[duplicateRows_Annealing]
    final_Annealing = final_Annealing.groupby(["Word"]).sum().reset_index()
    len_Annealing = len(final_Annealing)
    
    
    
    Union_Absorption = pd.concat([df_Absorption,Global_Absorption], axis=0)
    del Union_Absorption['Frequency']
    duplicateRows_Absorption = Union_Absorption['Word'].duplicated(keep=False) 
    final_Absorption = Union_Absorption[duplicateRows_Absorption]
    final_Absorption = final_Absorption.groupby(["Word"]).sum().reset_index()
    len_Absorption = len(final_Absorption)

    return (len_Efficciency,len_GAP,len_SynthesisMethod,len_SubstrateTemp,len_Annealing,len_Absorption)


# In[ ]:





# In[ ]:




