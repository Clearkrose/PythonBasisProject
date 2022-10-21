def now():
    print("2020-10-21")

f = now
f()

print(now.__name__)
print(f.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称为"装饰器"
# 本质上，decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2022-10-21')

now()

# 如果decorator本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print("2")

now()

