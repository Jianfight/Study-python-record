#-*- coding:utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
#in_file = open(from_file)
indata = (open(from_file)）.read()

#print "The input file is %d bytes long" % len(indata)  #并没有必要输出文件的字节数

# print "Does the output file exist? %r" % exists(to_file) #如果转出的文件不存在，计算机也会创造一个相应的文件。
#if exists (to_file) == False: # 这个if循环是为了是脚本更加的亲切
# print "Computer will create a new file."

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()