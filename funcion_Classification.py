#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pickle
import numpy as np
import sklearn
import sys


# In[9]:


def Classification(classifier,tiv,segment):
    

    
    
    Output = []
    
    if (len(segment)==0):
        
        Output = segment
    else:
        #uppickling the classifier
        with open(classifier, 'rb') as f:
            clf=pickle.load(f)

        #uppickling the vestorizer
        with open(tiv, 'rb') as f:
            tfidf=pickle.load(f)  


        segment_new = segment
        segment_new = tfidf.transform(segment_new).toarray()

        pred=clf.predict(segment_new )
        type(pred)

        a=pred.tolist()

        for i in range(len(segment)):

            if (a[i] == 1):
                Output.append(segment[i])
            
    
    return(Output)

