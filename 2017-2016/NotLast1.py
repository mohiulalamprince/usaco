
# coding: utf-8

# In[47]:

#Not last


# In[58]:

root = ""
#root = "/home/admin/usaco/"

file_name = 'notlast'


# In[59]:

import sys
input = open(root + file_name + ".in")
N = int(input.readline())

cows = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

cows_input = {}
for name in cows: cows_input[name] = 0

for i in range(0, N):
    (name, milk) = input.readline().strip().split(' ')
    cows_input[name] += int(milk)
cows_input = sorted(cows_input.items(), key=lambda x:x[1], reverse=False)


# In[60]:

mini = 1000000000
cow_mini = ''
for cow, milk in cows_input:
    if milk < mini: 
        mini = milk
        cow_mini = cow


# In[61]:

maxi_cow = ''
maxi = mini
for key, value in cows_input:
    if value > maxi:
        maxi = value
        maxi_cow = key
        break


# In[62]:

output = open(root + file_name + ".out", "w")
counter = 0
for key, value in cows_input:
    if maxi == value: counter += 1
if counter >= 2:
    output.write("Tie\n")
else:
    output.write(str(maxi_cow) + "\n")


# In[ ]:



