#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import import_ipynb
#%matplotlibinline
from funcion_preprocesamiento import *
from Funcion_frecuencia import *
from funcion_opentext import *
from Funcion_suma import *
stop_words = set(stopwords.words('english')) # No-meaning syntax words 


# In[4]:


def fun_df (df_Efficiency,df_GAP,df_SynthesisMethod,df_SubstrateTemp,df_Annealing,df_Absorption):

    #Merge dataframe on "axis 0", which represents the rows
    Union1 = pd.concat(df_Efficiency)
    Union2 = pd.concat(df_GAP)
    Union3 = pd.concat(df_SynthesisMethod)
    Union4 = pd.concat(df_SubstrateTemp)
    Union5 = pd.concat(df_Annealing)
    Union6 = pd.concat(df_Absorption)

    Validacion1 = suma(Union1) #Efficiency
    Validacion2 = suma(Union2) #GAP
    Validacion3 = suma(Union3) #SynthesisMethod
    Validacion4 = suma(Union4) #SubstrateTemp
    Validacion5 = suma(Union5) #Annealing
    Validacion6 = suma(Union6) #Absorption
    
    return (Validacion1,Validacion2,Validacion3,Validacion4,Validacion5,Validacion6)

