#!/usr/bin/env python
# coding: utf-8

# In[1]:


def duplicates (LT):
    # Removes Duplicates
    res = [] 
    for i in LT: 
        if i not in res: 
            res.append(i) 
    return(res)


# In[2]:


def List_to_String(texto):
    
    string = ' '.join([str(elem) for elem in texto]) #converting the resulting list back into a string
    
    return(string)


# In[4]:


def results(Good_Efficiency,Good_GAP,Good_SM):
    
    Result_Efficiency = []
    Result_GAP = []
    Result_SM = []
    
    # Efficiency display

    for sentence in Good_Efficiency:
        for word in sentence.split():
            if "%" in word:
                Result_Efficiency.append(word)
                
    # Gap display

    Result_GAP = []
    abecedario = ['1','2','3','4','5','6','7','8','9','0']

    for sentence in Good_GAP:
        for word in sentence.split():
            for letter in word:

                if letter in abecedario:
                    if "(" not in word:
                        if "[" not in word:
                            if "—" not in word:
                                Result_GAP.append(word)
                                
    
    # Synthesis Method Display
    
    Methods = ["PED","galvanostatically","electrochemical cel","HCl etching","boxplot","dopant profiling","sulfurization of electrodeposited","nanopowders","mechanochemically","photochemical deposition","PCD","doctor-blade coating","silar","chamical bath deposition","CBD","sol-gel","sintering","solid-state reaction","solid state reaction","chalcogenization","sputtering","co-sputtering","thermal-co-evaporation","thermal co-evaporation","pyrolysis","hydrazing","thermal evaporation","sping coating","sping-coating","electro deposition","electro-deposition","phenoxazine","full potential linearized augmented plane wave","FP-LAPW","colloidal hot-injection","hot injection","scherrer"]
    
    for sentence in Good_SM:
        for word in sentence.split():
            if word in Methods:
                Result_SM.append(word)
            
    
    
    Result_Efficiency = duplicates(Result_Efficiency)
    Result_GAP = duplicates(Result_GAP)
    Result_SM = duplicates(Result_SM)
    
    #converting Results_List to string
    
    A = List_to_String(Result_Efficiency)
    B = List_to_String(Result_GAP) 
    C = List_to_String(Result_SM)
    
    
    output_Efficiency = []
    output_GAP = []
    output_SM = []
    
    
    
    
    output_Efficiency.append(A)
    for i in range(len(Good_Efficiency)):
        output_Efficiency.append(Good_Efficiency[i])
        
    output_GAP.append(B)
    for i in range(len(Good_GAP)):
        output_GAP.append(Good_GAP[i])
        
    output_SM.append(C)
    for i in range(len(Good_SM)):
        output_SM.append(Good_SM[i])
        
    num_GAP = []
    num_Efficiency = []
    num_SM = []
    
    
    if (len(output_GAP)!= 0 ):
        num_GAP.append(output_GAP[0])
        #output_GAP.pop(0)
        
    if (len(output_Efficiency)!= 0 ):
        num_Efficiency.append(output_Efficiency[0])
        output_Efficiency.pop(0)
        
    if (len(output_SM)!= 0 ):
        num_SM.append(output_SM[0])
        output_SM.pop(0)
        
    
    return(output_Efficiency,output_GAP,output_SM,num_GAP,num_Efficiency,num_SM)


# In[ ]:




