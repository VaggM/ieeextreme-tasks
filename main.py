n = int(input())

vilains = {}

for i in range(n):

    vilain = input().split()

    name = vilain[0]
    height = vilain[1]

    if height not in vilains.keys():
        vilains[height] = []

    vilains[height].append(name)

for key in vilains.keys():
    print(vilains[key])
