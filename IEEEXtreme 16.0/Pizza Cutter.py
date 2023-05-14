t = int(input())

for test in range(t):

    cuts = input().split()

    edits = []

    for cut in cuts[1:]:

        edit = int(cut) % 360

        if edit >= 180:
            edit -= 180

        if edit not in edits:
            edits.append(edit)

    if len(edits) == 0:
        print(1)

    else:
        print(len(edits) * 2)
