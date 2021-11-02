#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


import numpy as np
from scipy.stats import norm
from scipy import stats


# In[6]:


anime = pd.read_csv('/Users/rubenlarrazolo/Downloads/anime.csv')
print(anime)


# In[8]:


anime.head()


# In[9]:


import seaborn as sns


# In[10]:


sns.distplot(anime['aired_from_year'])


# In[11]:


anime.scored_by.hist()


# In[12]:


anime['scored_bySQRT'] = np.sqrt(anime['scored_by'])


# In[13]:


anime['scored_byLOG'] = np.log(anime['scored_by'])


# In[14]:


RuntimeWarning: divide by zero encountered in log


# In[15]:


ValueError: range parameter must be finite.


# In[16]:


anime.dropna(inplace=True)


# In[17]:


anime.scored_byLOG.hist()


# In[18]:


anime['aired_from_yearSQ'] = anime['aired_from_year']**2


# In[19]:


anime.aired_from_yearSQ.hist()


# In[20]:


anime['aired_from_yearCUBE'] = anime['aired_from_year']**3


# In[21]:


anime.aired_from_yearCUBE.hist()


# In[22]:


from scipy import stats
from scipy.stats import boxcox


# In[23]:


anime['scored_byLOG1'] = boxcox(anime['scored_by'],0)


# In[ ]:




