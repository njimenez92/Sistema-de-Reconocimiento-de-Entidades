#!/usr/bin/env python
# coding: utf-8

# In[1]:


def segmentation (segmented_text):
    
    # These are the lists of desired variables where will be placed all the desired segments
    segmented_Efficiency = []
    segmented_GAP = []
    segmented_SynthesisMethod = []
    segmented_SubstrateTemp = []
    segmented_Annealing = []
    segmented_Absorption = []
    Compound = []
    
    # This is the list that contains all the paragraphs in lists
    paragraphs = []
    
    # This is the list that contains all the paragraphs in lists separated by words 
    splitted = []
    
    # Creates n lists for n paragraphs present on the text
    for paragraph in range(len(segmented_text)):
        paragraphs.append([])
        
    # Creates n lists for n paragraphs present on the text SPLITTED by words
    for paragraph in range(len(segmented_text)):
        splitted.append([])
        
    # Assignates each list to a paragraph
    for i in range(len(segmented_text)):
        paragraphs[i].append(segmented_text[i])
        
    # Separating the inside-lists into words 
    for j in range(len(paragraphs)):
        for word in paragraphs[j][0].split():
            splitted[j].append(word)
    
     
    #---------------------------------------------------------------------------------------------------#
    
    # Now we will assign the segments depending on the desired variables
    
    # If a paragraph meets all the criteria,it will be added to the output list
    
    # 1.) Efficiency
    #----- Criterio-----#
    k = 0
    CEF = 0; # Contains the Word Efficiency
    CPC = 0; # Contains %
    CPCE = 0; # Cointains the word PCE

    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if ("efficiency"==word or "efﬁciencies"==word or "efficiencies"==word or "efﬁciency"==word or "power conversion efficiency"==word): 
                CEF = 1
            
            if ("pce"==word):
                CPCE = 1
                
            if ("%" == word or "%" in word):
                CPC = 1
            
                
            # If the paragraphs meets the criteria, it will be added to the output list
            if ((CEF==1 or CPCE==1) and CPC ==1 ):
                segmented_Efficiency.append(paragraphs[k])
                CEF=0
                CPCE=0
                CPC=0
                break
    
    # 2.) GAP
    #----- Criteria-----#
    k = 0
    Cgap = 0; # Contains the Word gap
    Cev = 0; # Contains the ev unit
    
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if (word == "bandgap" or word == "gap"): 
                Cgap = 1
                
            if (word == "ev"):
                Cev = 1
                
            # If the paragraphs meets the criteria, it will be added to the output list
            if (Cgap==1 and Cev==1):
                segmented_GAP.append(paragraphs[k])
                Cgap=0
                Cev=0
                break    
    
    
    # 3.) Synthesis Method
    #----- Criteria-----#
    k = 0
    Csyn = 0 # Contains at least one of this synthesis methods
    
    Methods = ["PED","galvanostatically","electrochemical cel","HCl etching","boxplot","dopant profiling","sulfurization of electrodeposited","nanopowders","mechanochemically","photochemical deposition","PCD","doctor-blade coating","silar","chamical bath deposition","CBD","sol-gel","sintering","solid-state reaction","solid state reaction","chalcogenization","sputtering","co-sputtering","thermal-co-evaporation","thermal co-evaporation","pyrolysis","hydrazing","thermal evaporation","sping coating","sping-coating","electro deposition","electro-deposition","phenoxazine","full potential linearized augmented plane wave","FP-LAPW","colloidal hot-injection","hot injection","scherrer"]
    
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if (word.lower() in Methods):
                Csyn = 1
            
            # If the paragraphs meets the criteria, it will be added to the output list
            if (Csyn==1):
                segmented_SynthesisMethod.append(paragraphs[k])
                Csyn = 0
                break 
                
    #segmented_SynthesisMethod=list(dict.fromkeys(segmented_SynthesisMethod))
    
    
    # 4.) Substrate Temperature
    #----- Criteria-----#
    k = 0
    Csub = 0; # Contains the Word substrate
    Cgra = 0; # Contains the °
    
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if ("substrate temperature" == word.lower()): 
                Csub = 1

                           
                
            # If the paragraphs meets the criteria, it will be added to the output list
            if (Csub==1):
                segmented_SubstrateTemp.append(paragraphs[k])
                Csub=0
                Cgra=0
                break 
    
    
    # 5.) Annealing
    #----- Criteria-----#
    k = 0
    Cani = 0; # Contains the Word annealing
    Cane = 0; # Contains the Word annealed
    Cgra = 0; # Contains the °
    
    
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if (word == "annealing"): 
                Cani = 1
            if (word == "annealed"):
                Cane = 1
                
            if (word=="°c"):
                Cgra = 1
                
            # If the paragraphs meets the criteria, it will be added to the output list
            if ((Cani==1 or Cane==1)):
                segmented_Annealing.append(paragraphs[k])
                Cani=0
                Cane=0
                Cgra=0
                break 

    # 6.) Absorption
    
    #----- Criteria-----#
    k = 0
    Cabs = 0; # Contains the Word absorption
    Ccm = 0; # Contains the cm
    
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if (word == "absorption" or word=="coefﬁcient"): 
                Cabs = 1

                
            if ("cm" == word.lower() or "cm" in word.lower()):
                Ccm = 1
                
            # If the paragraphs meets the criteria, it will be added to the output list
            if ((Cabs==1) and (Ccm==1)):
                segmented_Absorption.append(paragraphs[k])
                Cabs=0
                Ccm=0
                break 
                
    # 7.) Compound
    
    compuestos = ["cztse","czts","cztsse","cu2znsns4"]
    for k in range(len(splitted)):
        for word in splitted[k]:
            
            # Determining if the paragraph meets the Criteria
            
            if (word.lower() in compuestos):
                Csyn = 1
            
            # If the paragraphs meets the criteria, it will be added to the output list
            if (Csyn==1):
                Compound.append(word)
                Csyn = 0
                break
    Compound = list(dict.fromkeys(Compound))
    
    return(segmented_Efficiency,segmented_GAP,segmented_SynthesisMethod,segmented_SubstrateTemp,segmented_Annealing,segmented_Absorption,Compound)

