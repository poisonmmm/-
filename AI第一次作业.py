import math


def tanh(x):
    result = (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
    return result


x = int(input("输入变量x:"))
print(tanh(x))


