# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）
# for key in dict:
# for value in dict.values()
# for k, v in dict.items()

# 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)