#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
from mplsoccer import Pitch 
import matplotlib.pyplot as plb


# In[30]:


df = pd.read_csv( 'e1.csv')


# In[31]:


df.head(20)


# In[32]:


df = df.loc[df['teamId']=='Manchester United']


# In[33]:


df.head(20)


# In[34]:


df = df.loc[df['type']=='Pass']


# In[35]:


df = df.loc[df['playerId']==10.0].reset_index()


# In[36]:


df.x = df.x*1.2
df.y = df.y*.8
df.endX = df.endX*1.2
df.endY = df.endY*1.2


# In[39]:


df.head()


# In[40]:


df['beginning'] = np.sqrt(np.square(120-df['x']) + np.square(40 - df['y']))
df['end'] = np.sqrt(np.square(120 - df['endX']) + np.square(40 - df['endY']))

df['progressive'] = [(df['end'][x]) / (df['beginning'][x]) < .75 for x in range(len(df.beginning))]


# In[42]:


df = df.loc[df['progressive']==True].reset_index()


# In[43]:


pitch = Pitch(pitch_type='statsbomb')
fig,ax = pitch.draw()

pitch.lines(df.x,df.y,df.endX,df.endY,comet=True,ax=ax)


# In[44]:


df.head()


# In[ ]:




