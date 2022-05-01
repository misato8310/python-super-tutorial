a = [ 5, 9, 11, 3, 6, 5, 11, 4, 9 ]
has_even = False

for i in a:
        print('checking: ' + str(i))
        if i % 2 == 0:
            has_even = True
            break

print('has even: ' + str(has_even))