n, h0, a, c, q = map(int, input().split())

heights = [h0]

for i in range(1, n):

    height = (a*heights[i-1] + c) % q

    heights.append(height)

res = 0

skip = 0

numbers = list(range(n))

for i in range(1, n):
    maxim = i
    flag = 1
    for j in numbers[i-1-skip::-1]:
        
        if (flag == 1):
            res += 1
            maxim = j
            
        elif (heights[j] > heights[maxim]):
            maxim = j
            res += 1
            
        else:
            
            skip += 1
            numbers.remove(j)
        
        
        flag = 0
        
print(res)
