#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import matplotlib.pyplot as plt
import import_ipynb
import re

from funcion_doi import *;
from funcion_segmentacion import *;
from funcion_preprocesamiento import *;
from Funcion_frecuencia import *;
from funcion_opentext import *;
from dataframe2 import *;
from Funcion_suma import *;
from validacion2 import *;
from funcion_Cleanse import *;
from funcion_ML import *;
from funcion_poligono import *;
from funcion_export import *;
from funcion_listtostring import *;
from Funcion_Compare import *;


# In[2]:


num_papers = 100

names = []
files = []

segmented_Efficiency = []
segmented_GAP = []
segmented_SynthesisMethod = []
segmented_SubstrateTemp = []
segmented_Annealing = []
segmented_Absorption = []

cleansed_Efficiency = []
cleansed_GAP = []
cleansed_SynthesisMethod = []
cleansed_SubstrateTemp = []
cleansed_Annealing = []
cleansed_Absorption = []

# Classification

Efficiency_good = []
Efficiency_bad = []
  
GAP_good = []
GAP_bad = []
    
Annealing_good = []
Annealing_bad = []
    
Absorption_good = []
Absorption_bad = []

    


# Creating the Lists which will be used to execute the functions

for k in range(0,num_papers): # number of papers


    # Opening the Documents
    string = ('P' + str(k) +'.txt') # name of the documents we want to open
    names.append(string) # Save the names into a list
    file = ('file' + str(k))
    files.append(file)




# 1. segment lists

    segmented_ef = ('Segmented_Efficiency' + str(k))
    segmented_ga = ('Segmented_GAP' + str(k))
    segmented_sm = ('Segmented_SynthesisMethod' + str(k))
    segmented_st = ('Segmented_SubstrateTemp' + str(k))
    segmented_an = ('Segmented_Annealing' + str(k))
    segmented_ab = ('Segmented_Absorption' + str(k))

    segmented_Efficiency.append(segmented_ef)
    segmented_GAP.append(segmented_ga)
    segmented_SynthesisMethod.append(segmented_sm)
    segmented_SubstrateTemp.append(segmented_st)
    segmented_Annealing.append(segmented_an)
    segmented_Absorption.append(segmented_ab)

# 2. cleanse lists

    cleansed_ef = ('cleanse_Efficiency' + str(k))
    cleansed_ga = ('cleanse_GAP' + str(k))
    cleansed_sm = ('cleanse_SynthesisMethod' + str(k))
    cleansed_st = ('cleanse_SubstrateTemp' + str(k))
    cleansed_an = ('cleanse_Annealing' + str(k))
    cleansed_ab = ('cleanse_Absorption' + str(k))

    cleansed_Efficiency.append(cleansed_ef)
    cleansed_GAP.append(cleansed_ga)
    cleansed_SynthesisMethod.append(cleansed_sm)
    cleansed_SubstrateTemp.append(cleansed_st)
    cleansed_Annealing.append(cleansed_an)
    cleansed_Absorption.append(cleansed_ab)



# Executing the Functions    

for k in range(0,num_papers): # Iterates each document inside a list and opens it

    # 1.) opening the documents

    files[k] = opentext(names[k]) # List that contains all the documents opened

    # 2.) segmentation of the document

    segmented_Efficiency[k],segmented_GAP[k],segmented_SynthesisMethod[k],segmented_SubstrateTemp[k],segmented_Annealing[k],segmented_Absorption[k],c = segmentation(files[k])

    
    # 3.) cleansing function

    cleansed_Efficiency[k],cleansed_Absorption[k],cleansed_Annealing[k],cleansed_GAP[k],cleansed_SynthesisMethod = cleansing(segmented_Efficiency[k],segmented_Absorption[k],segmented_Annealing[k],segmented_GAP[k],segmented_SynthesisMethod[k])


for k in range (0,num_papers):

    # For to iterate evey cleansed list in order to determine which ones are useful and which ones are not.

    for lst in cleansed_Efficiency[k]: #Each list inside the list of cleased
        
        for string in lst: # Each string inside the list
            
            if( ("keywords" in string) or ("12.6" in string)    ): # If a black condition is given
                
                Efficiency_bad.append(lst) # Add the list to the black list
                
            
            
            
    
    # Whithin the two groups, convert each one to dataframes.
    
    

              

