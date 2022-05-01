a = 1
def test():
    global a
    a = 10

test()
print(a)
