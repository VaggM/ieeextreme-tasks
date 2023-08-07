# W x H wall
# A x B tiles
# M dollars per 10 tiles
# C dollars per cut inch

# example input
# 8 5 3 2 100 3

# expected output
# 139

import math

W, H, A, B, M, C = map(int, input().split())

horizontal = math.ceil(W/A)
vertical = math.ceil(H/B)

tot_tiles = vertical * horizontal

hoff = W % A
voff = H % B

cut_inches = 0

if hoff > 0:
    cut_inches += H
    
if voff > 0:
    cut_inches += W

total_price = M * math.ceil( tot_tiles / 10 ) + C * cut_inches

print(total_price)
