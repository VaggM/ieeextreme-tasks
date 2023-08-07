
# example input
# 2
# 3
# Alice 1 Bob
# Chuck 1 Dave
# Dave 1 Eve
# 4
# Alice 2 Bob Chuck
# Chuck 1 Bob
# Dave 2 Alice Bob
# Alice 1 Eve

# expected output
# 2 1
# 4 2


t = int(input())

for i in range(t):

    n = int(input())
    treats = {}

    for j in range(n):

        treat = input().split()
        tr = treat[0]
        price = int(treat[1])
    
        if tr not in treats.keys():
            treats[tr] = 0
            
        treats[tr] += price

        for k in range(price):
            tr = treat[2 + k]
            
            if tr not in treats.keys():
                treats[tr] = 0
            treats[tr] -= 1
                
    treat_nums = 0
    for treat in treats.values():
        if treat > 0:
            treat_nums += treat
                
    print(f"{treat_nums} {max(treats.values())}")
                
