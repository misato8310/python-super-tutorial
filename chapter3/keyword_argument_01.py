def test(arg1, arg2, arg3):
    print(str(arg1), str(arg2), str(arg3))

## 位置引数
test(1, 2, 3)

## キーワード引数
test(arg2='a', arg1='b', arg3='c')
