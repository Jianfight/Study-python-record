# -*- coding:utf-8 -*-
#python的高级特性
#切片
l = ["Michael", "Sarah", "Tracy", "Bob", "Jack",];  #在最后一个元素后面添加一个，号，使该列表最后有一个空元素
print (l[0:3]);   #表示从索引0开始，到索引3结束，但是不包括索引3
a = ["Michael", "Sarah"]
print (a [:2]);    #第一个索引是0的可以省略，这次输出中原列表中并没有索引为2的元素，但是程序不报错，代表输出的元素并不包括索引2
print (l[-1:0]);     #表示从倒数第一个元素输出
#将切片功能应用于元组中
tuple1 = (1, 2, 3, 4, 5, 6, 7, );
print(tuple1[1:4]);
#将切片功能应用于字符串中
string1 = "nizainalikanjianguota";
print (string1[1:9]);
#[star:over:间隔]
list1 = list(range(100));
print(list1[::4]);
print(list1);

#迭代（for循环），迭代的对象可以是列表，元组，字典等。
#检查该对象是否可以迭代可以用到collections模块中的iterable(可迭代的)类型进行判断
from collections import Iterable;
print(isinstance(l,Iterable));
#在python中将for循环转化为类似C#中的for循环可以使用内置函数enumerate将一个列表转化为索引-元素对
for i, value in enumerate(list1):
    print(i, value);

#列表生成式
list2 = [x * x for x in range(1,11)];  
list3 = [x * x for x in range(1,11) if x%2 == 0]; #对x值进行数值要求,表示在列表生成器中可以对元素的选取进行要求
list4 = [m + n for m in "ABC" for n in "XYZ"]; #使用两层循环，生成全排列
# import os;
# list5 = [d for d in os.listdir(',')];
d = {'x':'A', 'y':'B', 'z':'C'};
list6 = [k + '=' + v for k,v in d.items()];
list7 = ['Hellow', 'World', 18, 'Apple', None];
list8 = [s.lower() for s in list7 if isinstance(s, str)];
print(list2, list3, list4, list6, list8);

#生成器（generator）
#将列表生成式中的[]修改为(),即可产生一个生成器，其效果是将列表元素按照某种算法推算出来,生成器也是可以迭代的。
g = (x * x for x in range(10));
# i = 0;
# while i < 10:
#     print(next(g)); #生成器保存的是算法，每次调用next(g)就计算出下一个元素值，没有更多元素时，就会抛出StopIteration的错误。
#     i += 1;
for n in g:
    print(n);
#斐波拉契数列（Fibonacci）
# def fib(max):
#     n, a, b = 0, 0, 1;
#     while n < max:
#         print(b);
#         a, b = b, a + b;   #多变量式赋值语句
#         n +=1;
#     return 'done'
#使用生成器的方式构建斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1;
    while n < max:
        yield b
        a, b = b, a + b;   #多变量式赋值语句
        n +=1;
    return'done'
f = fib(9);
for i in f:
    print(i)
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():   #示例函数,来检验使用函数模式建立的生成器的执行方案
    print('step 1');
    yield 1;
    print('step 2');
    yield(3);
    print('step 3')
    yield(5);
for i in fib(9): #使用循环的方式输出生成器
    print(i);
while True:
    try:
        x = next(f);
        print('g:', x);
    except StopIteration as e:
        print ('Generator return value:' , value);
        break;

#迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。iter()函数用来生成迭代器其参数应该为可迭代的对象。
# Python的for循环本质上就是通过不断调用next()函数实现的
