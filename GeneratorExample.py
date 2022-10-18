# 通过列表生成式，我们可以直接创建一个列表。但是，收到内存的限制，列表容量肯定是有限的
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样我们就不必创建完整的list，从而节省大量的空间
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

g = (x * x for x in range(10))
print(g)

# 一个一个打印
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# generator保存的是算法，每次调用next()，就计算出g的下一个元素的值，知道计算到最后一个元素，没有更多元素时，抛出StopIteration

g = (x * x for x in range(10))
for n in g:
    print(n)

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现

# 斐波拉契数列(Fibonacci)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

# 注意，赋值语句 a, b = b, a + b
# 相当于   t = (b, a + b)  a = t[0]    b = t[1]
fib(6)

# 要把fib函数变成generator函数，只需要把print(b)改为yield b
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(f)

for n in fib(6):
    print(n)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator

def odd():
    print('step 1')
    yield 1
    print('Step 2')
    yield (3)
    print('Step 3')
    yield (5)

o = odd()
next(o)
next(o)
next(o)

# 创建3个完全独立的generator
next(odd())
next(odd())
next(odd())

# 用for循环调用generator时，发现拿不到generator的return语句的返回值
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break