# -*- coding:utf-8 -*-
# 将文本赋给x
x = "There are %d types of people." % 10
# 将文本binary赋给变量binarty
binary = "binary"
# 将don't赋给变量do_not
do_not = "don't"
#将文本赋给y
y = "Those who know %s and those who %s." % (binary, do_not)
# 输出x
print x 
# 输出 y
print y 
print "I said: %r." % x 
print "I also said: '%s'." % y 
hilarious = False
# 将文本给joke_evaluation 并在末尾追加格式化符号，方便与别的文本进行连接
joke_evaluation = "Isn't that joke so funny?! %r"
# 输出连接两个文本的一种方式
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
# 另一种在输出时连接两个文本的方法
print w + e 