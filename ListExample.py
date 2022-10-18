#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0])
print(classmates[-2])

classmates.append("Adam")
print(classmates)

classmates.insert(1, "Jack")
print(classmates)

classmates.pop()    #删除末尾的元素
print(classmates)

print(classmates.pop(1))
# classmates.pop(1)
print(classmates)

classmates[1] = "Sarah"
print(classmates)

L = ["apple", 123, True]
print(len(L))

S = ["python", "java", ["asp", "php"], "scheme"]
print(S[2][1])

# 另一种有序列表叫元组：tuple
# tuple和List非常相似，但是tuple一旦初始化就不能修改
students = ("Michael", "Bob", "Tracy")
# 因为tuple不可变，所以代码更安全
# 如果可能，能用tuple代替list就尽量用tuple

#定义只有一个元素的tuple
t = (1)
print(t)

u = (1,)
print(u)

# "可变的"tuple
r = ("a", "b", ["C", "D"])
r[2][1] = "R"
print(r)