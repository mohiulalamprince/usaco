
# coding: utf-8

# In[1]:

#Problem 3. The Cow-Signal 


# In[55]:

import sys

file_name = "/Users/mohiulalamprince/usaco/Problem3.TheCow-Signal.in"
inf = ""
if file_name:
    inf = open(file_name)
else:
    inf = sys.stdin

A = []
line = inf.readline().strip()
(M, N, K) = map(int, line.split())
for x in range(0, M):
    line = inf.readline().strip()
    A.append(line)


# In[56]:

table = [['0' for x in range(0, N * K)] for y in range(0, M * K)]

def signals(sx, sy, ex, ey, sign):
    for x in range(sx, ex):
        for y in range(sy, ey):
            table[x][y] = sign


# In[57]:

for i in range(0, M):
    for j in range(0, N):
        sx = i * K
        ex = i * K + K
        sy = j * K
        ey = j * K + K
        signals(sx, sy, ex, ey, A[i][j])


# In[58]:

file_pointer = open("/Users/mohiulalamprince/usaco/cowsignal.out", "w")
for x in table:
    file_pointer.write(''.join(x) + "\n")


# In[ ]:



