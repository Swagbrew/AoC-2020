inputs = []
with open('task1_1.txt', 'r') as f:
    for x in f:
        inputs.append(int(x))

for x in inputs:
    for y in inputs:
        for z in inputs:
            if x != y and x != z and y != z and x+y+z == 2020:
                print(x*y*z)
