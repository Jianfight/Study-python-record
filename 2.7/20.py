#-*- coding:utf-8 -*-
# 调用sys模块中的参数变量功能
from sys import argv
# 对参数变量进行解包，并将其赋予变量
script, input_file = argv

#定义函数
def print_all(f):
	print f.read()

# f.seek的功能是将文件的读取指针调到指定的位置
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

 print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)