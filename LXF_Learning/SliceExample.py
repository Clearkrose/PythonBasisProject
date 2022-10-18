L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])

N = list(range(100))
# 前10个数，每两个取一个
print(N[:10:2])
# 所有数，每5个取一个
print(N[::5])
# 什么都不写，只写[:]就可以原样复制一个list
print(N[:])

# tuple也是一种list
U = (0, 1, 2, 3, 5)
print(U[:3])

print("ABCDEFG"[:3])