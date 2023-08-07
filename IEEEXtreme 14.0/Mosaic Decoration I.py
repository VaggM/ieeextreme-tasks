import math

firstLine = input().split()
x = [int(n) for n in firstLine]

bathrooms = x[0]
costB = x[1]
costP = x[2]

black = 0
pink = 0

for i in range(bathrooms):
    line = input().split()
    y = [int(n) for n in line]

    black = black + y[0]
    pink = pink + y[1]

black10 = black / 10
black10 = math.ceil(black10)

pink10 = pink / 10
pink10 = math.ceil(pink10)

cost_total = costB * black10 + costP * pink10

print(cost_total)
