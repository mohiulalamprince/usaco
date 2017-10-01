
# coding: utf-8

# In[28]:

#Hoof, Paper, Scissors 


# In[49]:

root = ''
#root = '/Users/mohiulalamprince/usaco/'
file_name = 'hps'


# In[50]:

input = open(root + file_name + ".in")
N = int(input.readline())


# In[51]:

map = {}
map[3] = 2
map[2] = 1
map[1] = 3

counter = 0
for i in range(0, N):
    (c1, c2) = input.readline().strip().split()
    c1 = int(c1)
    c2 = int(c2)
    if map.has_key(c1):
        if map[c1] == c2:
            counter += 1


# In[53]:

output = open(root + file_name + ".out", "w")
output.write(str(counter) + "\n")


# In[ ]:



