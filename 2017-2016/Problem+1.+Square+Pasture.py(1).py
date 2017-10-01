
# coding: utf-8

# In[102]:

#Problem 1. Square Pasture


# In[103]:

import math
root = ""
#root = "/Users/mohiulalamprince/usaco/"


# In[104]:

file_name = "square"
file_pointer = open(root + file_name + ".in")

(x1, y1, x2, y2) = map(int, file_pointer.readline().strip().split())


# In[105]:

(x3, y3, x4, y4) = map(int, file_pointer.readline().strip().split())


# In[106]:

res1 = math.fabs(x1-x2) * math.fabs(y1-y2)


# In[107]:

res2 = math.fabs(x3-x4) * math.fabs(y3-y4)


# In[108]:

output = open(root + file_name + ".out", "w")
result = int((res1 + res2) * (res1 + res2))


# In[109]:

output.write(str(result) + "\n")


# In[ ]:



