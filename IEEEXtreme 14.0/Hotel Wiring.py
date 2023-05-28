tests = int(input())

for i in range(tests):

    # test info
    info = input().split()

    floors = int(info[0])
    rooms = int(info[1])
    off_amount = int(info[2])

    # save on switches for every floor
    switches_on = []

    for j in range(floors):
        switch_on = int(input())
        switches_on.append(switch_on)

    # sort and divide into best on and best off floors
    switches_on.sort()

    rooms_on_best = switches_on[off_amount:]

    rooms_on_worst = switches_on[:off_amount]
    rooms_off = [rooms - switch_on for switch_on in rooms_on_worst]

    max_rooms = sum(rooms_on_best) + sum(rooms_off)

    print(max_rooms)
