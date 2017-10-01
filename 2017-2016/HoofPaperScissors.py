
# coding: utf-8

# In[54]:

#Hoof, Paper, Scissors 

root = ''
#root = '/Users/mohiulalamprince/Downloads/usaco/2017-2016/'
file_name = 'hps'


# In[115]:

input = open(root + file_name + ".in")
N = int(input.readline())


# In[116]:

map = {}
map[3] = 2
map[2] = 1
map[1] = 3

map2 = {}
map2[2] = 3
map2[1] = 2
map2[3] = 1

counter1 = 0
counter2 = 0
for i in range(0, N):
    (c1, c2) = input.readline().strip().split()
    c1 = int(c1)
    c2 = int(c2)
    print c1, c2
    if map.has_key(c1):
        if map[c1] == c2:
            counter1 += 1
    if map2.has_key(c1):
        if map2[c1] == c2:
            counter2 += 1
counter = max(counter1, counter2)


# In[117]:

output = open(root + file_name + ".out", "w")
output.write(str(counter) + "\n")


# In[ ]:



