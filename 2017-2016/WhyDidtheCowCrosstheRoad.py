
# coding: utf-8

# In[11]:

root = ''
#root = "/Users/mohiulalamprince/Downloads/usaco/2017-2016/"

file_name = 'crossroad'
input = open(root + file_name + ".in")

N = int(input.readline().strip())


# In[12]:

table = [-1 for x in range(0, N + 1)]


# In[13]:

counter = 0
for x in range(0, N):
    (cid, side) = input.readline().strip().split()
    cid = int(cid)
    side = int(side)
    if table[cid] == -1: table[cid] = side
    elif table[cid] != side:
    	table[cid] = side
        counter += 1


# In[14]:

output = open("crossroad.out", "w")
output.write(str(counter) + "\n")


# In[ ]:



