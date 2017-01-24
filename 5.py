#-*- coding:utf-8 -*-
name = 'Zed A. Shaw'
age = 35
height = 74 # 英寸
weight = 180# 英镑
eyes = 'Blue'
teech = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
# 对单位进行了转化
print "He's %-5f inches tall." % (height * 2.54)
# 对单位进行了转化
print "He's %-07f pounds heavy." % round(weight * 0.4535924)
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teech are usually %s depending on the coffee." % teech
# this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)