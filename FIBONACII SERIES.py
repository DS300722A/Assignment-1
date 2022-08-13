#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WAP IN python to print FIBONACII SERIES

num=int(input("enter the number : "))
num1=0
num2=1
#print(num2)
for i in range(2,num):
    num3=num1
    num1=num2
    print(num2)
    num2=num3+num2
   # print(num2)


# In[ ]:




