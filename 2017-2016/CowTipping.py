
# coding: utf-8

# In[82]:

#Cow Tipping


# In[90]:

root = ''
#root = "/Users/mohiulalamprince/Downloads/usaco/2017-2016/"


# In[91]:

file_name = 'cowtip'
input = open(root + file_name + ".in")


# In[92]:

N = int(input.readline().strip())


# In[93]:

matrix = [['0' for x in range(0, N)] for y in range(0, N)]
for i in range(0, N):
    line = input.readline().strip()
    for j, x in enumerate(line):
        matrix[i][j] = x


# In[94]:

matrix


# In[95]:

counter = 0
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if matrix[i][j] == '1':
            counter += 1
            for x in range(0, i + 1):
                for y in range(0, j + 1):
                    if matrix[x][y] == '1': 
                        matrix[x][y] = '0'
                    else: 
                        matrix[x][y] = '1'


# In[97]:

output = open(root + file_name + ".out", "w")
output.write(str(counter) + "\n")


# In[ ]:



