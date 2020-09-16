#!/usr/bin/env python
# coding: utf-8

# In[2]:


def cleansing (segmented_Efficiency,segmented_Absorption,segmented_Annealing,segmented_GAP,segmented_SynthesisMethod):
    
    
    cleansed_Efficiency = []
    cleansed_Absorption = []
    cleansed_Annealing = []
    cleansed_GAP = []
    
    for segmento in segmented_Efficiency:
        for string in segmento:
            if (("efﬁciency" in string) or("efﬁcient" in string)) and ("%" in string):
                cleansed_Efficiency.append(segmento)
    
    
    for segmento in segmented_Absorption:
        for string in segmento:
            if ("cm" in string) and (  ("coefﬁcient" in string) or ("absorption" in string)      ):
                cleansed_Absorption.append(segmento)
                
    for segmento in segmented_Annealing:
        for string in segmento:
            if ("°c" in string) or ("° c" in string):  
                cleansed_Annealing.append(segmento)
    
    for segmento in segmented_GAP:
        for string in segmento:
            if ("ev" in string) and ("gap" in string):  
                cleansed_GAP.append(segmento)
                
    cleansed_SynthesisMethod = segmented_SynthesisMethod
 
    
    return(cleansed_Efficiency,cleansed_Absorption,cleansed_Annealing,cleansed_GAP,cleansed_SynthesisMethod)


# In[ ]:





# In[ ]:




