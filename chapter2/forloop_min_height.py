height = [ 180, 170, 160, 165, 175 ]

min_num = height[0]

for i in height:
    if min_num > i:
        min_num = i
        print('i: ' + str(min_num))

print('min_num: ' + str(min_num))
