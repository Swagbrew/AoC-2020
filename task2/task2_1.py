import pandas as pd

df = pd.read_csv('task2.txt', header=None, sep=': ', engine='python')
df.columns = ['Rules', 'Passwords']
print(df)

df[['Counts', 'Character']] = df.Rules.str.split(' ', expand=True)

df[['CountL', 'CountH']] = df.Counts.str.split('-', expand=True)

df = df.drop(['Rules', 'Counts'], axis=1)

print(df)
result = []

for row in df.values:
    count = 0
    for i in row[0]:
        if i == row[1]:
            count += 1
    if int(row[2]) <= count <= int(row[3]):
        result.append(row[0])

print(len(result))


