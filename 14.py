# -*- coding:utf-8 -*-
from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s? " % user_name
likes = raw_input(prompt)

#进行一个判断尝试，当用户的回答是“yes”时，程序继续进行
#Yes = "yes"
#if likes == Yes :
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
#当用户说他不喜欢我时，哦，你真是一个无趣的人。
#else:
# print "Oh,my gad!!! You are not an interesting person."