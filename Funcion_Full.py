#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import os,glob
import string   
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import re

from math import pi

import math 
import string
import textwrap
import import_ipynb


from funcion_doi import *;
from funcion_segmentacion import *;
from funcion_preprocesamiento import *;
from Funcion_frecuencia import *;
from funcion_opentext import *;
from dataframe2 import *;
from Funcion_suma import *;
from funcion_Cleanse import *;
from funcion_ML import *;
from funcion_poligono import *;
from funcion_export import *;
from funcion_listtostring import *;
from Funcion_Compare import *;

from funcion_Classification import *;
from funcion_final import *;


# In[2]:


def NLTK_Classifier(filename):

    N_Documents = 100;
    text = open(filename,"r",encoding="utf8",errors='ignore'); # We opened the document's file
    text_raw = text.read();# We have the document's text as a RAW-STRING
    text_raw = text_raw.lower();

    
    Title_Output =[]
    Title_Output.append(filename)
    Title_Output

    text = text_raw.split("\n\n")

    #text= re.split(r'\W\n+', text_raw)
    #r'\W\n+'

    for i in range(0,len(text)):
        if "\n" in text[i]:
            text[i] = text[i].replace("\n",'') # We removed "\n" from the strings that compose the text

    Year_Output = []

    for word in text[0].split():
        if (")" in word):
            Year_Output.append(word)

    Year_Output
    
    
    
    segmented_Efficiency,segmented_GAP,segmented_SynthesisMethod,segmented_SubstrateTemp,segmented_Annealing,segmented_Absorption,Compound = segmentation(text) # Asignando cada salida a una variable
    Compound = list(dict.fromkeys(Compound)) # Eliminates repeated terms


    segmented_Efficiency,segmented_Absorption,segmented_Annealing,segmented_GAP,segmented_SynthesisMethod = cleansing(segmented_Efficiency,segmented_Absorption,segmented_Annealing,segmented_GAP,segmented_SynthesisMethod)

    Cleansed_Efficiency = List_of_lists_to_string(segmented_Efficiency)
    Cleansed_GAP = List_of_lists_to_string(segmented_GAP)
    Cleansed_Annealing = List_of_lists_to_string(segmented_Annealing)
    Cleansed_Absorption = List_of_lists_to_string(segmented_Absorption)
    Cleansed_SynthesisMethod = List_of_lists_to_string(segmented_SynthesisMethod)

    Good_Efficiency= Classification('classifier_Efficiency.pickle','tiv_Efficiency.pickle',Cleansed_Efficiency)
    Good_GAP= Classification('classifier_GAP.pickle','tiv_GAP.pickle',Cleansed_GAP)
    Good_Annealing= Classification('classifier_Annealing.pickle','tiv_Annealing.pickle',Cleansed_Annealing)
    Good_SynthesisMethod= Classification('classifier_SM.pickle','tiv_SM.pickle',Cleansed_SynthesisMethod)
    Good_Absorption= Classification('classifier_Absorption.pickle','tiv_Absorption.pickle',Cleansed_Absorption)
    Good_SubstrateTemp = segmented_SubstrateTemp

    if (len(Cleansed_Efficiency) == 0):
        PUT_Efficiency = 0;
    else:
        PUT_Efficiency = 100*(len(Good_Efficiency)/len(Cleansed_Efficiency));


    if (len(Cleansed_GAP) == 0):
        PUT_GAP = 0;
    else:
        PUT_GAP = 100*(len(Good_GAP)/len(Cleansed_GAP))


    if (len(Cleansed_Annealing) == 0):
        PUT_Annealing = 0;
    else:    
        PUT_Annealing = 100*(len(Good_Annealing)/len(Cleansed_Annealing))


    if (len(Cleansed_SynthesisMethod) == 0):    
        PUT_SynthesisMethod = 0;
    else:    
        PUT_SynthesisMethod = 100*(len(Good_SynthesisMethod)/len(Cleansed_SynthesisMethod))


    if (len(Cleansed_Absorption) == 0):     
        PUT_Absorption = 0;
    else:
        PUT_Absorption = 100*(len(Good_Absorption)/len(Cleansed_Absorption))


    if (len(segmented_SubstrateTemp) == 0):      
        PUT_SubstrateTemp = 0;
    else:
        PUT_SubstrateTemp = 100*(len(Good_SubstrateTemp)/len(segmented_SubstrateTemp))
    
    
    print ("The total useful percentage for the efficiency variable was of:", PUT_Efficiency,"%" )
    print ("The total useful percentage for the band gap variable was of:", PUT_GAP,"%" )
    print ("The total useful percentage for the Annealing variable was of:", PUT_Annealing,"%" )
    print ("The total useful percentage for the Absorption Coefficient variable was of:", PUT_Absorption,"%" )
    print ("The total useful percentage for the substrate temperature variable was of:", PUT_SubstrateTemp,"%" )
    print ("The total useful percentage for the synthesis method variable was of:", PUT_SynthesisMethod,"%" )

    OUT_Efficiency,OUT_GAP,OUT_SynthesisMethod,num_GAP,num_Efficiency,num_SM = results(Good_Efficiency,Good_GAP,Good_SynthesisMethod)

    def lt_ltoflt(lst): 
        return [[el] for el in lst] 

    OUT_Efficiency = lt_ltoflt(OUT_Efficiency)
    OUT_GAP = lt_ltoflt(OUT_GAP)
    OUT_SynthesisMethod = lt_ltoflt(OUT_SynthesisMethod)
    OUT_Annealing = lt_ltoflt(Good_Annealing)
    OUT_Absorption = lt_ltoflt(Good_Absorption)

    data=export(Year_Output,Title_Output,Compound,OUT_Efficiency,OUT_GAP,OUT_SynthesisMethod,Good_SubstrateTemp,Good_Annealing,Good_Absorption,num_GAP,num_Efficiency,num_SM)

    return(data)


# In[ ]:




