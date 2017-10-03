
# coding: utf-8

# In[1]:

# Why Did the Cow Cross the Road II


# In[61]:

root = ""
#root = "/home/admin/usaco/"

file_name = 'cowqueue'


# In[62]:

import sys
input = open(root + file_name + ".in")
N = int(input.readline())


# In[63]:

sums = 0
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            if self.y < other.y:
                return True
        return False

nodes = []
for i in range(0, N):
    (x, y) = input.readline().strip().split()
    x = int(x)
    y = int(y)
    node = Node(x, y)
    nodes.append(node)
nodes.sort()


# In[64]:

for node in nodes:
    x = node.x
    y = node.y
    
    if sums < x:
        sums = x + y
    elif sums > x:
        sums += y
    print x, y, sums


# In[65]:

output = open(root + file_name + ".out", "w")
output.write(str(sums) + "\n")


# In[ ]:



