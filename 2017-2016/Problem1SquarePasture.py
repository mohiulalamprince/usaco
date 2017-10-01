
# coding: utf-8

# In[151]:

#Problem 1. Square Pasture


# In[152]:

import math
root = ""
#root = "/Users/mohiulalamprince/usaco/"


# In[153]:

file_name = "square"
file_pointer = open(root + file_name + ".in")

(x1, y1, x2, y2) = map(int, file_pointer.readline().strip().split())


# In[154]:

(x3, y3, x4, y4) = map(int, file_pointer.readline().strip().split())


# In[155]:

p1 = min(x1, x3)
p2 = min(y1, y3)

q1 = max(x2, x4)
q2 = max(y2, y4)

res1 = math.fabs(p1-q1)
res2 = math.fabs(p2-q2)
print res1, res2
res = max(res1, res2) * max(res1, res2)


# In[ ]:




# In[156]:

output = open(root + file_name + ".out", "w")
result = int(res)


# In[157]:

output.write(str(result) + "\n")


# In[ ]:



