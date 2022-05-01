height = [ 180, 170, 160, 165, 175 ]

avg_sum = 0

for i in height:
    avg_sum += i
    print('i: ' + str(avg_sum))

avg_sum /= len(height)
print('avg_sum: ' + str(avg_sum))
