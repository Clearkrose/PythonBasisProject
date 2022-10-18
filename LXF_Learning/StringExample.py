#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("I\'m \"OK\"!")
print("I'm 'OK'!")

print("\\\n\\")
print("apple\tpeal\tpencil\nwater\ttree\tswim")

print('\\\t\\')
print(r'\\\t\\')    #默认不转义

print('''line1
line2
line3''')

#空值是Python里一个特殊的值，用None表示。
#None不能理解为0，因为0是有意义的，而None是一个特殊的空值

a = 123
print(a)
a = 'abc'
print(a)
#这种变量本身不固定的语言称之为动态语言，与之对应的是静态语言
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错

PI = 3.14159265359
#Python根本没有任何机制保证PI不会被改变

print( 10 / 3 )
print( 10 // 3 )    #地板除
print( 10.00 // 3.00)

#ASCII、GB2312
#Unicode
#UTF-8：常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
#计算机系统通用的字符编码工作方式：在计算机内存中，统一使用unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码

print(ord("a"))
print(ord("中"))

#b' = byte
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print(len("ABC"))
print(len("中文"))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上：
#!/usr/bin/env python3      为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-     为了告诉Python解释器，按照UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码

print("Hello, %s" % "world")
print("Hi, %s, you have $%d." % ("Michael", 1000000))
# %d    整数
# %f    浮点数
# %s    字符串
# %x    十六进制整数
#当你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换成字符串

print("growth rate: %d %%" %  7)

# format()
print("hello, {0}, 成绩提升了 {1:.2f}%".format("小明", 17.125))

# f-string
r = 2.5
s = PI * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')