#-*-coding:utf-8-*-
#��try...except...else �ĳ��ԡ�
while True:
	a = raw_input("> ")
	try:
		number = int(a)
	except:
		print "please input interger."
	else:
		print "You input number %d." % number
		break