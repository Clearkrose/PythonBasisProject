# 可以直接作用于for循环的对象称为可迭代对象：Iterable

from collections.abc import Iterable
print(isinstance([], Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
from collections.abc import Iterator
print(isinstance([], Iterator))
print(isinstance((x for x in range(10)), Iterator))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# Python的Iterator对象表现的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration
# Iterator的计算是惰性的，只有在需要返回下一个数据时才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数

for x in [1, 2, 3, 4, 5]:
    pass
# 等价于
it = iter([1, 2, 3, 4, 5])
print(it)

while True:
    try:
        x = next(it)
    except StopIteration:
        break