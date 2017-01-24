#-*-coding:utf-8-*-
# 定义一个函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# 调用函数，直接给定数字充当函数的参数
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# 在脚本中定义变量，调用函数，用定义的变量充当函数的参数
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 调用函数，通过数学运算的方式给函数的参数赋值
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# 在调用函数，通过对原有变量再一次进行数学运算，对函数的参数进行赋值
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print "We can input amount of cheese and cracker."
input_amound_of_cheese = raw_input ("Input amound of cheeses! ")
input_amonnd_of_cracker = raw_input ("Input amound of crackers! ")
cheese_and_crackers(int(input_amound_of_cheese), int(input_amonnd_of_cracker))

# 待完善
#print "We use a file to recording amound of cheeses and crackers."
#input_filename = raw_input ("Input file name! ")
#into_filname = open(input_filename,'w').write(cheese_and_crackers(int(input_amound_of_cheese), int(input_amonnd_of_cracker)))
#into_filname.close