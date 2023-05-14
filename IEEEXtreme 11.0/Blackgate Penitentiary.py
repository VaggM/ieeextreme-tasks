n = int(input())

members = {}
total = 0

# read members
for i in range(n):

    member = input().split()
    name = member[0]
    height = member[1]
    total = total + 1

    if height not in members.keys():
        members[height] = []

    members[height].append(name)

# print members
position = 1
for key in sorted(members.keys()):
    names = sorted(members[key])
    names_str = " ".join(names)
    pos_min = position
    pos_max = position + len(names) - 1

    out = f"{names_str} {pos_min} {pos_max}"
    print(out)

    position = position + len(names)
