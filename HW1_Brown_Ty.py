#!/usr/bin/env python
# coding: utf-8

# In[43]:


QOneList = list (range(30,65,5))
print(QOneList)

QOneList.sort(reverse=1)
print(QOneList)

QOneList.insert(0,65)
print(QOneList)


# In[62]:


QTwoList = []
QTwoList.append(0)
QTwoList.append(1)
QTwoList.append(2)
QTwoList.append(3)
QTwoList.append(4)
QTwoList.append(5)
QTwoList.append(6)
QTwoList.append(7)
QTwoList.append(8)
QTwoList.append(9)
QTwoList.append(10)
print(QTwoList)

QTwoList.remove(0)
print(QTwoList)

print(len(QTwoList))
print(max(QTwoList))
print(min(QTwoList))

sum(QTwoList)


# In[41]:


QThreeDict = {"sunny":"play","rainy":"watch TV","cloudy":"walk"}
print(QThreeDict)
QThreeDict.update({ "snowy" : "ski" })
print(QThreeDict)


# In[ ]:





# In[60]:


testlist = []
newguy = 0
if newguy<20:
    newguy = newguy + 1
    testlist.append(newguy)
else:
    newguy = 0
print(newguy)
print(testlist)


# In[ ]:




