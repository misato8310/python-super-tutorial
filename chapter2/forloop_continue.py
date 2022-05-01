a = [ 5, 9, 11, 3, 6, 5, 11, 4, 9 ]
for i in a:
    if i % 2 == 1:
        continue
    print('Even: ' + str(i))
