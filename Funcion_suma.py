#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


def suma(Union):
    
    #Ordeno alfabeticamente por medio de la columna Word
    Union=Union.sort_values(by=['Word'], ascending=True)

    #Elimino la columna de Interest
    del Union['Interest']
    

    #Elimino los valores NaN
    df1 = Union.apply (pd.to_numeric, errors='coerce')
    df1 = Union.dropna()


    #I detect repeated words 
    #Detecto las palabras repetidas 
    duplicateRows1 = df1['Word'].duplicated(keep=False) 

    final1=df1[duplicateRows1]

    #Sumo las Frecuencias de las palabras repetidas
    Final_frecuencias = final1.groupby(["Word"]).sum().reset_index() #Efficiency
    Final_frecuencias = Final_frecuencias.sort_values(by=['Frequency'], ascending=False)
    
    return(Final_frecuencias)


# In[ ]:




