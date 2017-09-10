#-*- coding:utf-8 -*-
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract (a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTUPLY %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDE %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d,Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That become: ", what,"Can you do it by hand?"

print "result : age + (height - (weight * (iq / 2))) = %d." % (age + (height - (weight * (iq / 2))))

# 使用函数对脚本末尾的进行解答
#def solve (a, b, c, d):
#	print "Formula = d + (c - (b * (a / 2)))"
#	return  d + (c - (b * (a / 2)))

#result = solve (iq, weight, height, age)
#print "Let's us use function to solving problem. Result: %d" % result

# 在脚本运行时由用户输入需要进行算数运算的因子
#addend1 = float(raw_input("Please input addend "))
#addend2 = float(raw_input("P;ease input other addend "))
#add_result = add(addend1, addend2)

#minuend = float(raw_input("Please input minuend "))
#subtrahend = float (raw_input("Please input subtrahend "))
#subtract_result = subtract(minuend, subtrahend)

#multipier1 = float (raw_input("Please input mutipier "))
#multipier2 = float (raw_input("Please input other mutipier "))
#multiply_result = multiply(multipier1, multipier2)

#dividend = float (raw_input("Please input dividend "))
#divisor = float (raw_input("Please input divisor "))
#divide_result = divide(dividend, divisor)

#print "%f %f %f %f" % (add_result, subtract_result, multiply_result, divide_result)
