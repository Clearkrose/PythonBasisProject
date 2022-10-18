print(abs(-20.11))
print(max(1, 3, 19, -44))
print(int('123'))
print(str(1.23))
print(bool(''))

# 变量a指向abs函数
a = abs
print(a(-1))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
# return None可以简写为return
print(my_abs(-9))

# 定义一个什么事都不做的空函数
def nop():
    pass
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来

# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# （自己定义的函数）但是如果参数类型不对，Python解释器就无法帮我们检查（my_abs和abs的差别）

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)
# 返回值是一个tuple

#位置参数
def power(x):
    return x * x
# 对与power函数，参数x就是一个位置参数

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
# 默认参数可以简化函数的调用
# 设置默认参数的注意点
#   1. 必选参数在前，默认参数在后，否则Python的解释器会报错
#   2. 如何设置默认参数：当函数有多个参数时，把变化大的参数放浅面，变化小的参数放后面，变化小的参数就可以作为默认参数
#   3. 默认参数必须指向不变对象
def add_end(L = []):
    L.append("END")
    return L
l = add_end()
print(l)
l = add_end()
print(l)

def add_end2(N = None):
    if N is None:
        N = []
    N.append("END")
    return N
n = add_end2()
print(n)
n = add_end2()
print(n)

# 可变参数：传入的参数个数是可变的
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 3, 6, 7, 2, 1))

nums = [1, 2, 3]
print(calc(*nums))

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')

extra = {'city': 'Beijing', 'job':'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

person('Jack', 24, **extra)

# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='doctor')

# 如果函数定义中已经有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('AMAO', 22, [2, 4, 5], city='suzhou', job='doctor')
# 命名关键字参数必须传入参数名，如果没有传入参数名，调用将报错


# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num -1, num * product)