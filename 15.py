# -*- coding:utf-8 -*-
# 在执行脚本时引入文件名
from sys import argv

# 解包，将引入的脚本名和文件名，分别赋值给两个变量
script, filename = argv

# 将打开文件将其赋值给变量
txt = open(filename)

# 将文件名打印出来
print "Here's your file %r:" % filename
# 将文件的地址打印出来
#print txt
print txt.read()
txt.close()

# 再一次输入文件的名字，并将其赋值给另一个变量
print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

#print txt_again
print txt_again.read()
txt_again.close()

