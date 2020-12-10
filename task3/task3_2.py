import pandas as pd
from numpy import product

df = pd.read_csv('task3.txt', header=None)
print(df)

i = [0, 0, 0, 0, 0]
count = [0, 0, 0, 0, 0]
slopes = [1, 3, 5, 7]
even = 0

for x in df.values:
    for y in range(4):
        if x[0][i[y]] == '#':
            count[y] += 1
        i[y] = (i[y] + slopes[y]) % 31

    if x[0][i[4]] == '#' and even == 0:
        count[4] += 1
    even = (even + 1) % 2
    if even == 0:
        i[4] = (i[4] + 1) % 31

print(count)
print(count[0]*count[1]*count[2]*count[3]*count[4])
