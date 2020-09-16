#!/usr/bin/env python
# coding: utf-8

# In[1]:


def List_to_String(texto):
    
    string = ' '.join([str(elem) for elem in texto]) #converting the resulting list back into a string
    
    return(string)


# In[3]:


def List_of_lists_to_string(test):

    Output=[]

    for item in test:
        jump = List_to_String(item)
        Output.append(jump)
        
    return(Output)

