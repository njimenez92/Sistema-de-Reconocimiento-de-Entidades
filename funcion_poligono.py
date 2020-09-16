#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi


# In[5]:


def spider(L1,L2,L3,L4,L5,L6):
    # Set data
    df = pd.DataFrame({
    'group': ['A'],
    'Efficiency': [L1],
    'GAP':[L2],
    'Sythesis Method': [L3],
    'Substrate Temp': [L4],
    'Annealing': [L5],
    'Absorption Coefficient': [L6],    
    })

    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([10,50,60,70,80,90], ["10","50","60","70","80","90"], color="grey", size=1)
    plt.ylim(0,100)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid',color="pink")

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.2,color="fuchsia")
    
    return(ax.plot,ax.fill)


# In[ ]:




