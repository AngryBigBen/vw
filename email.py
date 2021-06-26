#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import win32com.client as client


# In[4]:


outlook = client.Dispatch('Outlook.Application')


# In[5]:


message = outlook.CreateItem(0)


# In[6]:


message.Display()


# In[7]:


message.To = 'ben_lai@apple.com'


# In[9]:


message.Cc = 'wenbin.lai@postgrad.manchester.ac.uk'


# In[11]:


message.Subject = 'This is a test email for A company'


# In[18]:


message.Body = '''Dear Limited Partners,

We are pleased to provide you with the 1Q2021 Report for your investment in LC healthcare Fund I, L.P.

The attached report includes fund summary, portfolio summary, portfolio update, management update as well as the financial statements for the quarter ended 31/3/2021.


If you have any questions or comments on the report, please feel free to contact our finance team

(LC_Reporting@legendcapital.com.cn).

Thank you for your continuous support.

Best Regards.
LC Reporting
'''


# In[19]:


message.Save()


# In[20]:


message.Send()


# In[ ]:




