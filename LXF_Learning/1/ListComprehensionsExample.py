n = list(range(1, 11))
print(n)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

I = [x * x for x in range(1, 11)]
print(I)

O = [x * x for x in range(1, 11) if x % 2 == 0]
print(O)

P = [m + n for m in 'ABC' for n in 'XYZ']
print(P)

# 运用列表生成器，可以写出非常简洁的代码

# 列出当前目录下的所有文件和目录名
import os
Q = [d for d in os.listdir('.')]
print(Q)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
D = [k + '=' + v for k, v in d.items()]
print(D)

B = ['Hello', 'World', 'IBM', 'Apple']
C = [b.lower() for b in B]
print(C)


# if...else
A = [x for x in range(1, 11) if x % 2 == 0]
B = [x if x % 2 == 0 else -x for x in range(1, 11)]
# for前面的部分是一个表达式，它必须根据x计算出一个结果
# 因此，考察表达式x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else

print(A)
print(B)