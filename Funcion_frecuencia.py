#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
#%matplotlibinline
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) # No-meaning syntax words


# In[1]:


def Freq (Efficiency,GAP,SynthesisMethod,SubstrateTemp,Annealing,Absorption):

    Freq_Efficiency = {}
    Freq_GAP = {}
    Freq_SynthesisMethod = {}
    Freq_SubstrateTemp = {}
    Freq_Annealing = {}
    Freq_Absorption = {}


    # Obtaining the Frequency table of Efficiency

    for Global in Efficiency:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_Efficiency:
                        Freq_Efficiency[word]=0
                    Freq_Efficiency[word]+=1

     # Obtaining the Frequency table of GAP

    for Global in GAP:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_GAP:
                        Freq_GAP[word]=0
                    Freq_GAP[word]+=1


    # Obtaining the Frequency table of SynthesisMethod

    for Global in SynthesisMethod:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_SynthesisMethod:
                        Freq_SynthesisMethod[word]=0
                    Freq_SynthesisMethod[word]+=1       

    # Obtaining the Frequency table of Substrate Temperature

    for Global in SubstrateTemp:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_SubstrateTemp:
                        Freq_SubstrateTemp[word]=0
                    Freq_SubstrateTemp[word]+=1


    # Obtaining the Frequency table of Annealing

    for Global in Annealing:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_Annealing:
                        Freq_Annealing[word]=0
                    Freq_Annealing[word]+=1

    # Obtaining the Frequency table of Absorption

    for Global in Absorption:
        for st in Global:
            for word in st.split():
                if word.lower() not in stop_words:
                    if word not in Freq_Absorption:
                        Freq_Absorption[word]=0
                    Freq_Absorption[word]+=1

    # Organizing the Frequency tables in Dataframes using Pandas

    df_Efficiency = pd.DataFrame([[key, Freq_Efficiency[key]] for key in Freq_Efficiency.keys()], columns=['Word', 'Frequency'])
    df_GAP = pd.DataFrame([[key, Freq_GAP[key]] for key in Freq_GAP.keys()], columns=['Word', 'Frequency'])
    df_SynthesisMethod = pd.DataFrame([[key, Freq_SynthesisMethod[key]] for key in Freq_SynthesisMethod.keys()], columns=['Word', 'Frequency'])
    df_SubstrateTemp = pd.DataFrame([[key, Freq_SubstrateTemp[key]] for key in Freq_SubstrateTemp.keys()], columns=['Word', 'Frequency'])
    df_Annealing = pd.DataFrame([[key, Freq_Annealing[key]] for key in Freq_Annealing.keys()], columns=['Word', 'Frequency'])
    df_Absorption = pd.DataFrame([[key, Freq_Absorption[key]] for key in Freq_Absorption.keys()], columns=['Word', 'Frequency'])


    # Sorting The Dataframes in descending order (Most repeated term come first)

    df_Efficiency = df_Efficiency.sort_values(by='Frequency',ascending=False)
    df_GAP = df_GAP.sort_values(by='Frequency',ascending=False)
    df_SynthesisMethod = df_SynthesisMethod.sort_values(by='Frequency',ascending=False)
    df_SubstrateTemp = df_SubstrateTemp.sort_values(by='Frequency',ascending=False)
    df_Annealing = df_Annealing.sort_values(by='Frequency',ascending=False)
    df_Absorption = df_Absorption.sort_values(by='Frequency',ascending=False)

    # Binning the Dataframes (Organizing the terms that repeat the lowest)
    # Binning es diferente para cada variable
    # We will organize the Frequency of the terms in two Categories:
    # Low Interest: Repeats less than three times 
    # High Interest: Repeats more than five times


    Bin_Names = ["Low Interest","High Interest"]
    Bins = [1,3,5] 

    df_Efficiency['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)
    df_GAP['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)
    df_SynthesisMethod['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)
    df_SubstrateTemp['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)
    df_Annealing['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)
    df_Absorption['Interest'] = pd.cut(df_Absorption['Frequency'], Bins, labels = Bin_Names)


    # Deleting the terms that we have no interest in
    # (hay que determinar el criterio para descartar) el 3 no sirve
    df_Efficiency = df_Efficiency.drop(df_Efficiency[df_Efficiency.Frequency < 0].index)
    df_GAP = df_GAP.drop(df_GAP[df_GAP.Frequency < 0].index)
    df_SynthesisMethod = df_SynthesisMethod.drop(df_SynthesisMethod[df_SynthesisMethod.Frequency < 0].index)
    df_SubstrateTemp = df_SubstrateTemp.drop(df_SubstrateTemp[df_SubstrateTemp.Frequency < 0].index)
    df_Annealing = df_Annealing.drop(df_Annealing[df_Annealing.Frequency < 0].index)
    df_Absorption = df_Absorption.drop(df_Absorption[df_Absorption.Frequency < 0].index)
 

    
    # The Result from this process shows up the most relevant terms in the segment
    
    
    return (df_Efficiency,df_GAP,df_SynthesisMethod,df_SubstrateTemp,df_Annealing,df_Absorption)


# In[ ]:




