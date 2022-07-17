#!/usr/bin/env python
# coding: utf-8

# In[18]:



import numpy as np
a = ([1,6],[2,8],[3,11],[3,10], [1,7])

mean_a =np.mean(a)
print(mean_a)


# In[9]:


a_centred = a - mean_a
print(a_centred)


# In[31]:


a_centred_sp = a_centred.T[0] @ a_centred.T[1]
print(a_centred_sp)


# In[14]:


a_centred_sp/(a_centred[0] - 1)


# In[16]:


m = np.transpose(a)
m_cov = np.cov(m)
print(m_cov)


# In[21]:


import pandas as pd
authors = pd.DataFrame({'author_id':[1,2,3],'author_name':['Тургенев', 'Чехов', 'Островский']},columns = ['author_id','author_name'])
print(authors)


# In[23]:


import pandas as pd
authors = pd.DataFrame({'author_id':[1,2,3],'author_name':['Тургенев', 'Чехов', 'Островский']},columns = ['author_id','author_name'])
print(authors)


# In[25]:


authors_price = pd.merge(authors, books, on = 'author_id', how = 'outer')
print(authors_price)


# In[26]:


top5 = authors_price.nlargest(5,'price')
print(top5)


# In[27]:


authors_stat = authors_price.value_counts()
print(authors_stat)


# In[28]:


authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'] 
print(authors_price)


# In[29]:


book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
book_info['мягкая'] = book_info['мягкая'].fillna(0)
book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)


# In[ ]:




