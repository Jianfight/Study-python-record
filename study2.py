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


