import pandas as pd

df = pd.read_csv('task3.txt', header=None)
print(df)

i = 0
count = 0
for x in df.values:
    print(x[0])
    if x[0][i] == '#':
        count += 1
    i = (i+3) % 31

print(count)
