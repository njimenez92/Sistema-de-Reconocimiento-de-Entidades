#!/usr/bin/env python
# coding: utf-8

# In[1]:



import re 
import string   
import pandas as pd 
import numpy as np 
import math 
import textwrap
import pickle


# In[2]:


def preprocess(segmented_Efficiency,segmented_GAP,segmented_SynthesisMethod,segmented_SubstrateTemp,segmented_Annealing,segmented_Absorption): #aca deben entrar todos los segmentos
    
    res_Efficiency = []
    res_GAP = []
    res_SynthesisMethod = []
    res_SubstrateTemp = []
    res_Annealing = []
    res_Absorption = []

  
    
    # 1.) Efficiency
    
    for j in range(len(segmented_Efficiency)):
        for word in segmented_Efficiency[j][0].split():
            if ("http" in word.lower() or "doi" in word.lower() or "ref" in word.lower() or "watt" in word.lower()):
                res_Efficiency.append(segmented_Efficiency[j])
            if ("keywords" in word.lower() or "al" in word.lower() or "et" in word.lower() or "eff." in word.lower()):
                res_Efficiency.append(segmented_Efficiency[j])
       

                break
    
    # 2.) GAP
    
    for j in range(len(segmented_GAP)):
        for word in segmented_GAP[j][0].split():
            if ("http" in word.lower() or "doi" in word.lower() or "ref" in word.lower() or "watt" in word.lower() or "rev" in word.lower()):
                res_GAP.append(segmented_GAP[j])
            if ("keywords" in word.lower() or "al." in word.lower() or "eff." in word.lower() or "fig" in word.lower() or "ed" in word.lower()):
                res_GAP.append(segmented_GAP[j])
       

                break
    
    # 3.) Synthesis Method
    
    for j in range(len(segmented_SynthesisMethod)):
        for word in segmented_SynthesisMethod[j][0].split():
            if ("http" in word or "doi" in word.lower()):
                res_SynthesisMethod.append(segmented_SynthesisMethod[j])
            if (">>" in word.lower() or "//" in word.lower()):
                res_SynthesisMethod.append(segmented_SynthesisMethod[j])
            if ("fig" in word.lower() or "//" in word.lower()):
                res_SynthesisMethod.append(segmented_SynthesisMethod[j])


                break    
    
    #4.) Substrate Temperature
    
    for j in range(len(segmented_SubstrateTemp)):
        for word in segmented_SubstrateTemp[j][0].split():
            if ("http" in word or "doi" in word.lower()):
                res_SubstrateTemp.append(segmented_SubstrateTemp[j])
            if (">>" in word.lower() or "//" in word.lower()):
                res_SubstrateTemp.append(segmented_SubstrateTemp[j])
            if ("'fig" in word.lower()):
                res_Efficiency.append(segmented_Efficiency[j])

                break      
    
    #5.) Annealing
    
    for j in range(len(segmented_Annealing)):
        for word in segmented_Annealing[j][0].split():
            if ("http" in word or "doi" in word.lower()):
                res_Annealing.append(segmented_Annealing[j])
            if (">>" in word.lower() or "//" in word.lower()):
                res_Annealing.append(segmented_Annealing[j])
            if ("'fig" in word.lower()):
                res_Efficiency.append(segmented_Efficiency[j])

                break     
    
    #6.)  Absorption
    
    for j in range(len(segmented_Absorption)):
        for word in segmented_Absorption[j][0].split():
            if ("http" in word.lower() or "doi" in word.lower() or "ref" in word.lower() or "watt" in word.lower() or "rev" in word.lower()):
                res_Absorption.append(segmented_Absorption[j])

  
                break     
    

                
    Efficiency = [i for i in segmented_Efficiency if i not in res_Efficiency]                
    GAP = [i for i in segmented_GAP if i not in res_GAP]                
    SynthesisMethod = [i for i in segmented_SynthesisMethod if i not in res_SynthesisMethod]
    SubstrateTemp = [i for i in segmented_SubstrateTemp if i not in res_SubstrateTemp]
    Annealing = [i for i in segmented_Annealing if i not in res_Annealing]
    Absorption = [i for i in segmented_Absorption if i not in res_Absorption]
    
    return (Efficiency,GAP,SynthesisMethod,SubstrateTemp,Annealing,Absorption)


# In[ ]:




