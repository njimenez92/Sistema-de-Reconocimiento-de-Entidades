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
import glob
import os
import sys

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
from Funcion_Full import *;
from funcion_Classification import *;
from funcion_final import *;


# In[2]:


print("Ingrese el directorio en donde están ubicados los archivos a procesar:")
directorio = input()

def NLTK(directorio):
    
    Total_Dataframe = []

    os.chdir(directorio)
    myFiles = glob.glob('*.txt')

    for file in myFiles:
        Dataframe = NLTK_Classifier(file)
        Total_Dataframe.append(Dataframe)
        
        
    return(Total_Dataframe)

test = NLTK(directorio)


# In[3]:


def multiple_dfs(df_list, sheets, file_name, spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')   
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)   
        row = row + len(dataframe.index) + spaces + 1
    writer.save()
    
    return()


# In[4]:


multiple_dfs(test,'validation','Output.xlsx',1)

