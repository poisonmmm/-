from math import *


# 熵
def entropy(p_list: list):
    H = 0
    for p in p_list:
        s = -(p * log(p))
        H += s
    return H


# 基尼系数
def gini(p_list):
    H = 0
    for p in p_list:
        H += p ** 2
    H = 1 - H
    return H


p = [3/4, 1 / 4]
print(entropy(p))

