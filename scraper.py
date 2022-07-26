#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Okay, we're going to scrape the bbc

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[2]:


response=requests.get("https://www.bbc.com")
doc = bs(response.text)


# In[8]:


#get the link -- the 
#The code below is looking for classes with a link class a inside
titles = doc.select(".media__title a")
title_url=[title['href'] for title in titles]
title_url


# In[10]:


# get into pandas
rows=[]
for title in titles:
    row={}
    #title
    row['title']=title.text.strip()
    row['url']=title['href']
    
    rows.append(row)

df=pd.DataFrame(rows)
df.head()


# In[12]:


df.to_csv("bbc.csv", index=False)


# In[ ]:




