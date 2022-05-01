def my_max(x, y):
    if x < y:
        return y
    elif x > y:
        return x
    else:
        return 'equal'

## 位置引数
print(my_max(10, 100))

## キーワード引数
print(my_max(y=1000, x=100))
