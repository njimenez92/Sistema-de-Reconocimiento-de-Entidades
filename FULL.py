#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION

# ### The intention of this code is to be used as a tool for automatic extraction of relevant information regarding the construction of a solar panel based on a kesterite structure (Cu2ZnSnS4), based on six variables of interest (Efficiency, GAP, Method of synthesis, Substrate temperature, Annealing and Absorption coefficient) using natural language processing methods (NLTK) and Machine Learning
# 

# # READING MANUAL

# ### This code is divided into different sections, which are represented by a number of functions with a specific task:

# #### [Segmentation Function]: Is responsible for dividing the text into different segments, each with keywords that indicate that a specific parameter of interest is being discussed

# #### [Preprocessing Function]:  It is responsible for eliminating the words that despite having relevance at the time of reading the text, have no syntax value and therefore can be neglected, in addition, it is responsible for filtering the unwanted characters resulting from transforming the document into format .PDF to .TXT

# #### [Data Frequency]: Represents the words in a frequency table, which shows the number of times a word appears within a segment

# #### [Machine Learning]: Compares the table of frequencies obtained from the paper we are analyzing with the table of frequencies of the database with which the training was done

# ###  Once we have obtained a comparison by the machine learning function, we proceed to represent the data obtained in two ways:

# #### [Polygon Diagram or Spider Diagram]: Using the cosine distance and similarity method applied to the result obtained by the machine learning function, it is possible to represent how valuable the extracted information is.

# #### [Output Function]: Represents the segments obtained from the whole process on an excel sheet that has been specially modified with a "Macro" to organize the information in a visually attractive way

# ## Introducing the Path

# #### Please write here the address of your computer where the code is running, also remember that for the program to work properly, the documents that feed the database must also be hosted at this address

# In[1]:


import sys

print("Please insert the directory path: ")
path = input()

sys.path.append(path)


# # Insert the number of documents there are in the Database

# In[2]:


N_Documents = 100;


# ## Introducing the libraries and document to analyze

# #### some of these libraries must be downloaded by the user for the code to work properly. Please verify if your system has the following libraries:

# #### 1.NLTK    2.PANDAS    3.MATPLOTLIB    4.TEXTWRAP    5.IPYNB    6.IMPORT_IPYNB

# In[3]:


import nltk
import re 
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

from nltk.corpus import stopwords 
from nltk import tokenize
from nltk.tokenize import word_tokenize
from tqdm import tqdm 
from nltk import sent_tokenize


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


# In[4]:


stop_words = set(stopwords.words('english')) # No-meaning syntax words


# In[5]:


# PLEASE ENTER HERE THE DOCUMENT YUO WISH TO ANALYZE LOCATED ON THE SAME DIRECTORY WHERE YOU ARE RUNNING THIS PROGRAM
print("Enter the name of the text (.txt) document you wish to analyze: ")
filename = input();
text = open(filename,"r",encoding="utf8",errors='ignore'); # We opened the document's file
text_raw = text.read();# We have the document's text as a RAW-STRING
text_raw = text_raw.lower();


# ## Database Import

# ## Title Extraction 

# In[6]:


Title_Output =[]
Title_Output.append(filename)
Title_Output


# ## Removing unwanted punctuation from the text

# In[7]:


text = text_raw.split("\n\n")

#text= re.split(r'\W\n+', text_raw)
#r'\W\n+'

for i in range(0,len(text)):
    if "\n" in text[i]:
        text[i] = text[i].replace("\n",'') # We removed "\n" from the strings that compose the text


# ## Year extraction

# In[27]:


Year_Output = []

for word in text[0].split():
    if (")" in word):
        Year_Output.append(word)

Year_Output


# ## Segmentation of the document

# #### In this part of the code we will sub-divide the entire document looking up for the respective paragraphs which talk about the desired variables. If there is more than one paragraph that talk about any parameter, they will be combined into one segment

# ###### (If happens to be the case that there is no segment in the document about a desired variabe no segmentation will be made, therefore no output will be generated to that variable)

# ##### Paragraph Segmentation

# In[8]:


segmented_Efficiency,segmented_GAP,segmented_SynthesisMethod,segmented_SubstrateTemp,segmented_Annealing,segmented_Absorption,Compound = segmentation(text) # Asignando cada salida a una variable
Compound = list(dict.fromkeys(Compound)) # Eliminates repeated terms


# ## Cleansing Function

# #### This function works as a first filter, which takes each variable segment and cleanses it to improve presition 

# In[9]:


segmented_Efficiency,segmented_Absorption,segmented_Annealing,segmented_GAP,segmented_SynthesisMethod = cleansing(segmented_Efficiency,segmented_Absorption,segmented_Annealing,segmented_GAP,segmented_SynthesisMethod)


# #### Converting a list of lists into a list of strings 

# In[10]:


Cleansed_Efficiency = List_of_lists_to_string(segmented_Efficiency)
Cleansed_GAP = List_of_lists_to_string(segmented_GAP)
Cleansed_Annealing = List_of_lists_to_string(segmented_Annealing)
Cleansed_Absorption = List_of_lists_to_string(segmented_Absorption)
Cleansed_SynthesisMethod = List_of_lists_to_string(segmented_SynthesisMethod)


# # First Machine Learning

# #### In this part of the code, we will determine wether the segment is useful for our purpose or we should discard it

# #### Logistic Regresion Algorithms were used

# #### Binary Output is used: "Good" for an useful segment or "Bad" for a discardable segment

# In[11]:


Good_Efficiency= Classification('classifier_Efficiency.pickle','tiv_Efficiency.pickle',Cleansed_Efficiency)
Good_GAP= Classification('classifier_GAP.pickle','tiv_GAP.pickle',Cleansed_GAP)
Good_Annealing= Classification('classifier_Annealing.pickle','tiv_Annealing.pickle',Cleansed_Annealing)
Good_SynthesisMethod= Classification('classifier_SM.pickle','tiv_SM.pickle',Cleansed_SynthesisMethod)
Good_Absorption= Classification('classifier_Absorption.pickle','tiv_Absorption.pickle',Cleansed_Absorption)
Good_SubstrateTemp = segmented_SubstrateTemp


# # Results

# #### Graphical representation of the Total Useful Percentage gives a reference on the percentage of segments which are useful for our purpose using a poligonal diagram

# #### PUT is calculated with the following equation: PUT = 100* (Number of useful segments) / (Total number of segments)

# #### To give a correct interpretation of the polygonal diagram, please analyze it as follows: As the polygon shown gets closer to the limit of the circle, it means that more segments belong to the "good" category for each variable

# In[12]:


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


# In[13]:


AP,AF = spider(PUT_Efficiency,PUT_GAP,PUT_SynthesisMethod,PUT_SubstrateTemp,PUT_Annealing,PUT_Absorption)


# In[14]:


print ("The total useful percentage for the efficiency variable was of:", PUT_Efficiency,"%" )


# In[15]:


print ("The total useful percentage for the band gap variable was of:", PUT_GAP,"%" )


# In[16]:


print ("The total useful percentage for the Annealing variable was of:", PUT_Annealing,"%" )


# In[17]:


print ("The total useful percentage for the Absorption Coefficient variable was of:", PUT_Absorption,"%" )


# In[18]:


print ("The total useful percentage for the substrate temperature variable was of:", PUT_SubstrateTemp,"%" )


# In[19]:


print ("The total useful percentage for the synthesis method variable was of:", PUT_SynthesisMethod,"%" )


# ## Organizing the results

# In[20]:


OUT_Efficiency,OUT_GAP,OUT_SynthesisMethod,num_GAP,num_Efficiency,num_SM = results(Good_Efficiency,Good_GAP,Good_SynthesisMethod)


# In[21]:


def lt_ltoflt(lst): 
    return [[el] for el in lst] 


# In[22]:


OUT_Efficiency = lt_ltoflt(OUT_Efficiency)
OUT_GAP = lt_ltoflt(OUT_GAP)
OUT_SynthesisMethod = lt_ltoflt(OUT_SynthesisMethod)
OUT_Annealing = lt_ltoflt(Good_Annealing)
OUT_Absorption = lt_ltoflt(Good_Absorption)


# ## Output

# #### After the extraction of the information on the paper, there must be a list for every variable of interest which contains all the data

# In[28]:


data=export(Year_Output,Title_Output,Compound,OUT_Efficiency,OUT_GAP,OUT_SynthesisMethod,Good_SubstrateTemp,Good_Annealing,Good_Absorption,num_GAP,num_Efficiency,num_SM)


# In[29]:


datatoexcel = pd.ExcelWriter("Output.xlsx",engine='xlsxwriter')
data.to_excel(datatoexcel, sheet_name='Output', index=False)
datatoexcel.save()


# In[30]:


type(data)

