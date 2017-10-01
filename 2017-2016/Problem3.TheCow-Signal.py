import sys

file_name = "cowsignal.in"

inf = open(file_name)

A = []
line = inf.readline().strip()
(M, N, K) = map(int, line.split())
for x in range(0, M):
    line = inf.readline().strip()
    A.append(line)

table = [['0' for x in range(0, N * K)] for y in range(0, M * K)]

def signals(sx, sy, ex, ey, sign):
    for x in range(sx, ex):
        for y in range(sy, ey):
            table[x][y] = sign

for i in range(0, M):
    for j in range(0, N):
        sx = i * K
        ex = i * K + K
        sy = j * K
        ey = j * K + K
        signals(sx, sy, ex, ey, A[i][j])

file_pointer = open("cowsignal.out", "w")
for x in table:
    file_pointer.write(''.join(x) + "\n")
