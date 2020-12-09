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
    if ((row[0][int(row[2]) - 1] == row[1] or row[0][int(row[3]) - 1] == row[1]) and not (
            row[0][int(row[2]) - 1] == row[1] and row[0][int(row[3]) - 1] == row[1])):
        result.append(row[0])

print(len(result))
