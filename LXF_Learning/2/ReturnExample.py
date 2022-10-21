# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为"闭包(Closure)"

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count():
    def f(j):
        def g():
            return j*j
        return g()
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

# 使用闭包，就是内层函数应用了外层函数的局部变量
# 如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
# 但是，如果对外层变量赋值，由于Python解释器会把x当做函数fn()的局部变量，它会报错