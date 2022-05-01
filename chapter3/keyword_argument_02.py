def test(arg1, arg2=2, arg3=3):
    print(str(arg1) + str(arg2) + str(arg3))

test(1, 'B', 'C')
test(1)
test(1, arg3='C')
