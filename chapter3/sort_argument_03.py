a = [ 5, -7, 0, 9, -3]
def my_abs(x):
    if x < 0:
        x * -1
    return x

print(sorted(a, key=my_abs, reverse=True))
