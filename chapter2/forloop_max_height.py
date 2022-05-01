height = [ 180, 170, 160, 165, 175 ]

max_num = height[0]

for i in height:
    if max_num < i:
        max_num = i
        print('i: ' + str(max_num))

print('max_sum: ' + str(max_num))
