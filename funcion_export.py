#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


def export (Year,Title,Compounds,Efficiency,GAP,SynthesisMethod,SubstrateTemp,Annealing,Absorption,num_GAP,num_Efficiency,num_SM):
            
    
    data = pd.DataFrame({
            
            'AÑO DE PUBLICACIÓN': [Year],
            
            'TITULO': [Title],
        
            'COMPUESTO': [Compounds],
        
            'VALOR NUMÉRICO EFICIENCIA': [num_Efficiency],
        
            'EFICIENCIA': [Efficiency],
        
            'VALOR NUMÉRICO GAP': [num_GAP],
        
            'BAND GAP': [GAP],
             
            'RESUMEN MÉTODO DE SÍNTESIS': [num_SM],
            
            'MÉTODO DE SÍNTESIS': [SynthesisMethod],
        
            'Recocido': [Annealing],
        
            'TEMPERATURA DEL SUSTRATO': [SubstrateTemp],
        
            'COEFICIENTE ABSORCIÓN': [Absorption]
        
        
            })
    return(data)

