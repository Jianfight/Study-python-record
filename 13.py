#-*- coding: utf-8 -*-
from sys import argv
#解包，将输入的各项传送给相应的变量。
script, first, second, third = argv
# 尝试：脚本运行时输入（raw_inout）和在执行脚本时输入(import)进行比较
#judge = raw_input ("Are you reading to print?")
#yes = "yes"
#if judge == yes:
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third  
#else :
 #print "I don't print."
 
#从import中输入也是默认为字符串，如果输入数字需要使用int函数进行转换。
#print "They adds equel %d." % (int (first) +int (second) + int(third))