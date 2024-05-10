#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


from random import seed


# In[3]:


import string


# In[7]:


# сложение двух строк по модулю (xor)
def xor_text_f(text, key):
    if len(key) != len(text):
        return "Ошибка: ключ и  текст разной длины!"
    xor_text = ''
    for i in range(len(key)):
        # функция ord возвращает целое число — номер из таблицы символов Unicode, представляющий позицию данного символа
        xor_text_symbol = ord(text[i]) ^ ord(key[i])
        xor_text += chr(xor_text_symbol)
    return xor_text


# In[12]:


# ввод исходного текста
text = 'С Новым Годом, друзья!'


# In[13]:


# создание ключа
key = ''
seed(22)
for i in range(len(text)):
    key += random.choice(string.ascii_letters + string.digits)
key


# In[14]:


# получение шифротекста
xor_text = xor_text_f(text, key)
xor_text


# In[15]:


# открытый текст
xor_text_f(xor_text, key)


# In[16]:


# получение ключа
xor_text_f(text, xor_text)

