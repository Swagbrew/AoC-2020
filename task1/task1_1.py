inputs = []
with open('task1.txt', 'r') as f:
    for x in f:
        inputs.append(int(x))

for x in inputs:
    for y in inputs:
        if x != y and x+y == 2020:
            print(x*y)
