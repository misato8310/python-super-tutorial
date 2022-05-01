def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return print('FizzBuzz')
    elif x % 3 == 0:
        return print('Fizz')
    elif x % 5 == 0:
        return print('Buzz')
    else:
        return print('nothing')

fizzbuzz(15)
