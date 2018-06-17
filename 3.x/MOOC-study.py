#温度转化（摄氏度C，华氏度F）公式：C = (F - 32) / 1.8  F = C *1.8 + 32
'''
Val = input ("请输入带有温度标识符的温度值（例如：0C 或者 32F）： ")
if Val[-1] in ['c','C'] :
	f = 1.8 * eval(Val[0:-1]) + 32
	print("您输入的摄氏温度为：" + Val +",其对应的华氏温度为：%.2fF" %f)
elif Val[-1] in ['f','F']:
	c = (eval(Val[0:-1]) - 32) / 1.8
	print("您输入的华氏温度为：" + Val +",其对应的摄氏温度为：%.2fC" %c)
else :
	print("输入有误！")
'''

#平均数
'''
num1 = input('please input one number: ')
num2 = input('please input two number: ')
avg_num = (float(num1) + float(num2)) / 2
print("Average is :%f." %avg_num)
'''

#整数序列求和
'''
N = input("请输入整数N： ")
sum = 0
for i in range(int(N) + 1):
	sum = sum + i;
print("从1到N的整数和为：%i" %sum)
'''

#九九乘法表
'''
for i in range(1, 10):
	for j in range(1, i + 1):
		jieguo = i * j
		print('{} * {} = {:2}' .format(j, i, jieguo) ,end = " ")
	print(" ")
'''

#阶乘计算
'''
N = input("请输入整数N：")
sum, tmp = 0, 1   #多变量赋值
for i in range(1, int(N) + 1):
	tmp = tmp * i
	sum = sum + tmp
print ("运算结果为：%i" %sum)
'''

#猴子摘桃
'''
sum = 1 
for i in range(5):
	sum = (sum + 1) * 2
print ("猴子第一天一共摘了%i个桃"%sum)
#第二种方法(没想明白？？？)
n = 1
for i in range(5, 0, -1):
	n = (n + 1) << 1
print(n)
'''

#画蛇
'''
import turtle  #引入turtle库
def DrawSnake(rad, angle, len, neckrad):
	color = ['yellow', 'blue', 'black', 'red', 'green']
	for i in range(len):
		turtle.pencolor(color[i])
		turtle.circle(rad, angle)
		turtle.circle(-rad, angle)

	turtle.circle(rad, angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1, 180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300, 800, 0, 0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor("yellow")
	turtle.seth(-40)
	DrawSnake(40,80,5,pythonsize/2)

main()
'''

#画等边三角形(仿写)
'''
import turtle
def DrawThreeAngle (len, angle,distance):
	for i in range(len):
		turtle.forward(distance)
		turtle.left(angle)

def DrawThreeAngle1 (distance, steps):
	turtle.circle(distance, None, steps)

def main():
	turtle.setup(1200, 800, 0, 0)
	turtle.pencolor("red")
	turtle.pensize(10)
	turtle.seth(0)
	#DrawThreeAngle(3, 120, 100)
	DrawThreeAngle1(100,3)

main()
'''

#健康食谱
'''
diet = ['西红柿', '黄瓜', '土豆', '西葫芦', '冬瓜']
for x in range(0,5):
	for y in range(0,5):
		if not(x == y):
			print('{},{}'.format(diet[x], diet[y]))
'''

#五角星的绘制
'''
import turtle
turtle.fillcolor("red")
turtle.begin_fill()
while True:
	turtle.fd(200)
	turtle.right(144)
	if abs(turtle.pos()) < 1 :
		break
turtle.end_fill()
color = turtle.fillcolor() #试验fillcolor函数的返回
print(color)
'''

#太阳花的绘制
'''
import turtle
turtle.color("red", "yellow")
turtle.begin_fill()
while True:
	turtle.fd(200)
	turtle.left(170)
	if abs(turtle.pos()) < 1:
		break
turtle.end_fill()
turtle.done()
'''

#螺旋线的绘制
'''
import turtle
import time
turtle.speed('fastest')
turtle.pensize(2)
for x in range(100):
	turtle.fd(2 * x)
	turtle.right(90)
time.sleep(3)
'''

#彩色螺旋线的绘制
'''
import turtle
import time
turtle.pensize(2)
turtle.bgcolor("black")
colors = ['red', 'yellow', 'purple', 'blue']
turtle.tracer(False)
for x in range(400):
	turtle.fd(2 * x)
	turtle.color(colors[x % 4])
	turtle.left(91)
turtle.tracer(True)
time.sleep(3)
'''

#输入月份转换为其英文缩写
'''
mouths = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份（1-12）： ")
pos = (int(n)-1) * 3
print("该月份对应的英文缩写为：" + mouths[pos: pos + 3] + ".")
'''
#输入数字转换为相应的中文星期
'''
days = "星期一星期二星期三星期四星期五星期六星期日"
n = input("请输入星期几（1-7）：")
pos = (int(n) - 1) * 3
print("其对应的中文星期为：" + days[pos : pos + 3] + ".")
'''

#使用蒙特卡洛法（其属于随机抽样统计实验法）计算π的值，蒙特卡洛方法提供了使用计算机中的随机数和随机试验来解决现实中无法通过公式来解决的问题的思路
'''
原理：构建一个单位正方形，并在正方形中构建四分之一圆，然后随机向其中抛洒大量的点，
当抛洒点的数量达到一定程度时，园内的点将构成圆的面积,全部抛洒点将构成矩形的面积，
用园内的点数量除以矩形内点的数量，为面积比，即为π/4。
IPO：输入：抛入点的数量
	 处理：对于每个抛洒点计算其到圆心的距离，通过距离统计园内点的个数
	 输出：计算π的值
'''
'''
import math
import random
import time
DARTS = int(math.pow(2,20))
hits = 0
time.clock()
for i in range(1, DARTS):
	x, y = random.random(), random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance <= 1:
		hits += 1
pi = (hits / DARTS) * 4
print("π的值为：%s" %pi)
print("程序的运行时间是：%-5.5ss" %time.clock())
'''

#.format()的<格式控制标记>应用形式
'''
s = "python"
print('{0:30}'.format(s))  #空格填充
print('{0:>30}'.format(s)) #空格填充，右对齐
print('{0:-^30}'.format(s)) #符号填充，居中对齐
print('{0:3}'.format(s))
#千位分隔符
print('{0:-^20}'.format(1234567890))
print('{0:-^20,}'.format(1234567890))
print('{0:-^20,}'.format(12345.67890))
#<.精度>
print('{0:.2f}'.format(1234.56789))
print('{0:H^20.3f}'.format(1234.56789))
print('{0:.4}'.format(s))
#<类型>
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425))
print('{0:e},{0:E},{0:f},{0:%}'.format(3.14))
print('{0:.2e},{0:.2E},{0:.2f},{0:.2%}'.format(3.14))
'''

#空气质量(练习分支结构)
'''
def main():
	PM = eval(input("请输入空气中PM2.5的浓度："))
	if PM <= 35:
		print("空气质量：优")
	elif PM > 35 and PM <= 75 :
		print("空气质量：良")
	elif PM > 75 and PM <= 115 :
		print("空气质量：轻度污染")
	elif PM > 115 and PM <= 150 :
		print("空气质量：中度污染")
	elif PM > 150 and PM <= 250 :
		print("空气质量：重度污染")
	elif PM > 250 and PM <= 500 :
		print("空气质量：严重污染")
	elif PM > 500 :
		print("您输入的PM2.5浓度超限，我劝您赶跑吧！！！")
	else :
		print("请输入正确的浓度值。")
main()
'''

#一元二次方程求解
'''
import math
def main():
	a, b, c = eval(input("请输入一元二次方程的系数a, b, c: "))
	delta = b * b - 4 * a * c                                 #delta 是希腊字母δ的意思
	if a == 0:
		x = -c / b
		print("该程序的解为：(The solutions are:)", x)
	elif delta < 0:   
		print("该程序无解。（The equation has not real root.）")
	elif delta == 0:
		discRoot = math.sqrt(delta)
		root = (-b + discRoot) / (2 * a)
		print("该程序的解为：(The solutions are:)", root)
	else:
		discRoot = math.sqrt(delta)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("该程序的解为：(The solutions are:)", root1, root2)
main()
'''
#采用异常处理的方式，求解一元二次方程
'''
import math
def main():
	try:
		a, b, c = eval(input("请输入一元二次方程的系数a, b, c: "))
		discRoot = math.sqrt(b * b - 4 * a * c )
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("该程序的解为：(The solutions are:)", root1, root2)
	except ValueError as excObj:
		if str(excObj) == 'math domain error':
			print("该程序无解。（The equation has not real root.）")
		else:
			print("You didn't give me the right number of coefficients.")
	except NameError:
		print("You didn't enter three numbers.")
	except TypeError:
		print("Your input were not all number.")
	except SyntaxError:
		print("Your input was not in the correct form.Missing comma?")
	except:
		print("Soming went wrong, sorry!")
main()
'''

#异常处理
'''
while True:
	try:
		x = int(input("请输入一个数字：（Please enter a number.）"))
	except ValueError:
		print("哎呦！这不是一个有效的数字，请重新输入：（Oops! That was no valid number. Try again...）")
	else :
		print ('Else.')
		break
	finally :
		print("finally.")
'''
'''
def main():
	try :
		number1, number2 = eval(input("Enter two number, separated by a comma: "))
		result = number1 / number2

	except ZeroDivisionError:  #零作为除数的错误错误
		print('Division by zero!')
	except SyntaxError:  #无效的表达式
		print("A comma may be missing in the input.")
	except:
		print("Soming wrong in the input.")
	else:
		print("No exception, the result is", result)
	finally:
		print("Executing the final clause.")
main()
'''
#求三者最大值
'''
#方法一：通盘比较
x1, x2, x3 = eval(input("请输入三个数值，每个数值用逗号隔开："))
if x1 >= x2 and x1 >= x3:
	maxNumber = x1
elif x2 >= x1 and x2 >= x3 :
	maxNumber = x3
else:
	maxNumber = x3
print("三者中最大值为：{:-^20}".format(maxNumber))
'''
#方法二：决策树(第一个决策分析有多种可能，每一个可能性又可以产生另外一种决策。)（优点：避免冗余比较。例如：通盘中的x1和x2比较了两次）
'''
x1, x2, x3 = eval(input("请输入三个数值，每个数值用逗号隔开："))
if x1 >= x2 :
	if x1 >= x3 :
		maxNumber = x1
	else:
		maxNumber = x3
else:
	if x2 >= x3 :
		maxNumber = x2
	else:
		maxNumber = x3
print("三者中最大值为：{:-^20}".format(maxNumber))
'''
#方法三：顺序处理
'''
x1, x2, x3 = eval(input("请输入三个数值，每个数值用逗号隔开："))
maxNumber = x1
if x2 > maxNumber :
	maxNumber = x2
if x3 > maxNumber :
	maxNumber = x3
print("三者中最大值为：{:-^20}".format(maxNumber))
'''
#求四者最大数（决策树）
'''
x1, x2, x3, x4 = eval(input("请输入四个数值，每个数值用逗号隔开："))
if x1 >= x2 and x1 >= x3:
	if x1 >= x4 :
		maxNumber = x1
	else:
		maxNumber = x4
else:
	if x2 >= x3 and x2 >= x4:
		maxNumber = x2
	else:
		if x3 >= x4 :
			maxNumber = x3
		else:
			maxNumber = x4
print("四者中最大值为：{:-^20}".format(maxNumber))
'''
#寻找一组数中的最大值
'''
def main():
	n = eval(input("哪里有多少个数字：（How many numbers are there?）"))
	maxNumber = eval(input("请输入一个数字：(Enter a nomber)"))
	for i in range(n-1):
		x = eval(input("请输入一个数字：(Enter a nomber)"))
		if x > maxNumber:
			maxNumber = x
		print("最大值为(The largest value is:)：{:-^20}".format(maxNumber))
main()
'''
#终极方法调用python的max()函数
'''
def main():
	x1, x2, x3 = eval(input("请输入三个数值，每个数值用逗号隔开："))
	print("三者中最大值为：{:-^20}".format(max(x1,x2,x3)))
main()
'''

#for循环的应用：计算一些字符串
'''
words = ['cat', 'window', 'defensestrate']
for i in words:
	print(i, len(i))
'''
#for循环的应用：求平均值
'''
n = eval(input('请输入该组数字的个数：'))
sum = 0
for i in range(n):
	x = eval(input("请输入数字："))
	sum += x
print("该组数的平均值为(The average is)：{:-^10.2f}".format(sum/n))
'''

#while循环
'''
i = 0
while i <= 10:
	print(i)
	i += 1
'''
#for/while中break用法
'''
sum = 0
number = 0
while number <= 20:
	number += 1
	sum += number
	if sum >= 100:
		break
print("The number is :",number)
print("The sum is :",sum)
'''
#for/while中continue的用法
'''
for i in range(2,10):
	if i % 2 == 0:
		print("Found an even number:", i)
		continue
	print("Found a number:", i)
'''
#for/while中else,的用法
'''
for i in range(2,10):
	for j in range(2,i):
		if i % j == 0:
			print(i, 'equals', j, '*', i//j)
			break
	else:
		print(i, 'is a prime number.')
'''

#交互式循环
'''
def mian():
	sum = 0
	count = 0
	moreData = 'yes'
	while moreData == 'yes':
		x = eval(input('请输入需要计算平均值的基本数字：'))
		sum += x
		count += 1
		moreData = input('是否还有更多的数字需要参与计算？（yes/no）')
	print("该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''

#哨兵循环（执行循环，直到遇到特定的值循环语句才终止循环的结构设计方法）
'''
def main():
	sum = 0
	count = 0
	x = eval(input('请输入需要计算平均值的基本数字：（输入负数退出）'))
	while x >= 0:
		sum += x
		count += 1
		x = eval(input('请输入需要计算平均值的基本数字：（输入负数退出）'))
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''
#哨兵循环2.0版本（执行循环，直到遇到特定的值循环语句才终止循环的结构设计方法）
'''
def main():
	sum = 0
	count = 0
	xStr = input('请输入需要计算平均值的基本数字(Enter a number )：（输入空退出<Enter> to quit）')
	while xStr != "":
		x = eval(xStr)
		sum += x
		count += 1
		xStr = input('请输入需要计算平均值的基本数字：（输入空退出）')
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''

#文件循环(假设文件中每行只有一个数据)
#for循环模式
'''
def main():
	fileName = input("请输入文件的地址：(What file are the number in?)")
	infile = open(fileName,'r')
	sum = 0
	count = 0
	for line in infile:
		if line != '\n':
			x = eval(line)
			sum += x
			count += 1
		else:
			continue
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main() 
'''
#while循环模式
'''
def main():
	fileName = input("请输入文件的地址：(What file are the number in?)")
	infile = open(fileName,'r')
	line = infile.readline()
	sum = 0 
	count = 0 
	while line != '':
		if line != '\n':
			x = eval(line)
			sum += x
			count += 1
			line = infile.readline()
		else:
			line = infile.readline()
		
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''

#循环嵌套模式(一行有多个数据，且使用逗号隔开)
'''
def main():
	fileName = input("请输入文件的地址：(What file are the number in?)")
	infile = open(fileName,'r')
	line = infile.readline()
	sum = 0 
	count = 0 
	while line != "":
		
		#for xStr in line.split(","):
		#		sum += eval(xStr)
		#		count += 1
		#line = infile.readline()
		
		if line != '\n':
			for xStr in line.split(","):
				sum += eval(xStr)
				count += 1
			line = infile.readline()
		else:
			line = infile.readline()
		
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''
#改进
'''
def main():
	fileName = input("请输入文件的地址：(What file are the number in?)")
	infile = open(fileName,'r')
	line = infile.readline()
	sum = 0 
	count = 0 
	while line != "":
		if line != '\n':
			for xStr in line.split(","):
				if xStr != '':                  #添加一个判断，以防止数据中两个逗号之间为空的情况
					sum += eval(xStr)
					count += 1
				else:
					continue
			line = infile.readline()
		else:
			line = infile.readline()
		
	print("\n该组数的总和为{:-^10}，其平均数为：{:*^10.2f}".format(sum, sum/count))
main()
'''

#死循环的特定用法：保证用户输入一个符合要求的数据
'''
while True:
	try:
		x = int(input("Please enter a number:"))
		#break
	except ValueError:
		print('Oop, that was no valid number. Try again....')
	else:
		print('.......')
		break
	finally:
		print('Number is ', x)
'''

#后测循环（python中并没有后测循环语句，我们可以使用while True: 和 if <condition> : break的方式来组建后测循环）
#输入一个非负数
'''
while True:
	x = eval(input("Enter a posotive number.(请输入一个正数。): "))
	if x >= 0:
		break 
	else:
		print('The number you enter was not positive.(您输入的不是一个正数。)')
'''

#布尔表达式
#规则1：只要一个选手比赛成绩达到15分比赛结束，或者一方打了7分而另一方1分未得比赛结束
#a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)
#规则2：一个团队分数达到15分且领先对手2分以上比赛结束
#(a >= 15 and a-b >= 2) or (b >= 15 and b-a >= 2)
#(a >= 15 or b >= 15) and abs(a-b) >= 2	

#身体质量指数（BMI）
'''
high = eval(input("请输入您的身高（以m为单位）："))
weight = eval(input("请输入您的体重（以kg为单位）："))
BMI = weight / (high * high)
if BMI < 18.5:
	EvaluationDomestic ,EvaluationInternation = '偏瘦','偏瘦'
elif BMI > 18.5 and BMI < 25 :
	if BMI > 24:
		EvaluationDomestic = '偏胖'
		EvaluationInternation = '正常'
	else:
		EvaluationDomestic = '正常'
		EvaluationInternation = '正常'
elif BMI >= 25 and BMI < 30:
	if BMI >= 28:
		EvaluationDomestic = '肥胖'
		EvaluationInternation = '偏胖'
	else:
		EvaluationDomestic = '偏胖'
		EvaluationInternation = '偏胖'
else:
	EvaluationDomestic = '肥胖'
	EvaluationInternation = '肥胖'
print("您的BMI指数为：{:-^10.2f},您的体型在国际标准中属于'{}'，在国内标准中属于'{}'。".format(BMI, EvaluationInternation, EvaluationDomestic))
'''

#函数
#生日快乐歌
'''
name = input("请输入寿星的名字：")

def happyBirthday(name):
	words = 'Happy Birthday to you!'
	print(words + '\n'+words+ '\n' +words[0:14]+',dear '+ name + '!'+ '\n' + words)
happyBirthday(name)

def happy():
	print('Happy Birthday to you!')
def sing(name):
	happy()
	happy()
	print('Happy Birthday ' + ',dear ' + name +'!')
	happy()
sing(name)
'''

#计算两点之间的距离
'''
import math
def square(x):
	y = x * x
	return y
def distance():
	dis = math.sqrt(square(x1-x2) + square(y1-y2))
	return dis 
def main():
	x1, y1 = eval(input("请输入第一点的二维坐标（X, Y）："))
	x2, y2 = eval(input("请输入第二点的二维坐标（X, Y）: "))
	distance = distance()
	print(distance)
main()
'''
#计算三角形的周长
'''
import math
def square(x):
	y = x * x
	return y
def distance(x1, y1, x2, y2):
	dis = math.sqrt(square(x1-x2) + square(y1-y2))
	return dis 
def isTriangle(x1, y1, x2, y2, x3, y3):
	flag = ((x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)) != 0
	return flag
def main():
	print("请按照顺序输入三个点的坐标：【Please enter (x,y) of three points in turn:】")
	x1, y1 = eval(input("请输入第一点的二维坐标（X, Y）：【Point1 :(x,y) = 】"))
	x2, y2 = eval(input("请输入第二点的二维坐标（X, Y）: 【Point2 :(x,y) = 】"))
	x3, y3 = eval(input("请输入第三点的二维坐标（X, Y）: 【Point3 :(x,y) = 】"))
	if isTriangle(x1,y1,x2,y2,x3,y3):
		l1 = distance(x1,y1,x2,y2)
		l2 = distance(x2,y2,x3,y3)
		l3 = distance(x3,y3,x1,y1)
		L =l1 + l2 + l3
		print("该三角形的周长为：{0:-^.2f}【The perimeter of the triangle is: {0:-^.2f}】".format(L))
	else:
		print('该三点无法构成三角形！【kidding me! This is not a triangle.】')
main()
'''
#计算两个数的加法和减法(函数可以同时返回多个值)
'''
def sumDiff(x, y):
	sum = x + y
	diff = x - y 
	return sum, diff 
def main():
	x, y = eval(input('Please enter two number (num1, num2): '))
	s, d = sumDiff(x, y)
	print('The sum is {0:*^10}, The difference is {1:*^10}'.format(s,d))
main()
'''
#通过利率更新银行账户余额
'''
def addInterest(balance, rate):
	newBalance = balance * (1 + rate)
	return newBalance
def main():
	amount, rate = eval(input('请输入本金和利率（之间使用逗号隔开）：'))
	amount = addInterest(amount, rate)
	print(amount)
main()
'''
#处理多个银行账户的程序
'''
def addInterest(balance, rate):
	for i in range(len(balance)):
		balance[i] = balance[i] * (1 + rate)
def main():
	amount = [1000, 105, 3500, 739]
	rate = 0.05
	addInterest(amount, rate)
	print(amount)
main()
'''

#十年投资的增长
'''
print('该程序绘制投资的十年增长。(This program plots the growth of a 10-years inverstment.)')
#输入本金和利率
principal = eval(input('请输入初始本金：(Enter the initial principal.)'))
apr = eval(input('请输入年化利率：(Enter the annualized interest rate.)'))
#建立一个图表，绘制每一年银行账户的增长数据
for year in range(1, 11):
	principal = principal * (1 + apr)
	print('%2d' %year, end = "")
	#计算星号的数量
	total = int(principal*4/1000)
	print('*' * total)
print("0.0K  2.5K  5.0K  7.5K  10.0K")
'''
#将上面的例子进行模块化
'''
def createTable(principal, apr):
	#为每一年绘制星号增长图
	for year in range(1, 11):
		principal = principal * (1 + apr)
		print('%2d' %year,'年：', end = '')
		total = caculateNum(principal)
		print(principal,'*' * total)
	print("0.0K  2.5K  5.0K  7.5K  10.0K")
def caculateNum(principal):
	#计算星号数量
	total = int(principal*4/1000)
	return total
def main():
	print('该程序绘制投资的十年增长。(This program plots the growth of a 10-years inverstment.)')
	#输入本金和利率
	principal = eval(input('请输入初始本金：(Enter the initial principal.)'))
	apr = eval(input('请输入年化利率：(Enter the annualized interest rate.)'))
	#建立一个图表，绘制每一年银行账户的增长数据
	createTable(principal, apr)
main()
'''

#递归函数
'''
#阶乘
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
n = eval(input("Enter number 'n'."))
print('其阶乘为{}'.format(factorial(n)))
#字符串的反转
def reverse(s):
	if s == '':
		return s
	else:
		return reverse(s[1:]) + s[0]
text = input("请输入一个字符串：")
textReverse = reverse(text)
print(text,'反转',textReverse)
'''

#函数的实例设计
#树的绘制（宽度优先绘制法）思考深度优先绘制法
'''
from turtle import Turtle, mainloop
import time

def tree(plist, l, a, f):
	#plist is list of pen
	#l is length of branch
	#a is half of the angle between 2 branch
	#f is factor by which branch is shortened from level to level
	if l > 5:
	 	lis = []
	 	for p in plist:
	 	 	p.forward(l)
	 	 	q = p.clone()
	 	 	p.left(a)
	 	 	q.right(a)
	 	 	lis.append(p)
	 	 	lis.append(q)
	 	tree(lis, l*f, a, f)

def makeTree(x,y):
	p = Turtle()
	p.color('green')
	p.pensize(5)
	#p.setundobuffer(None)
	p.hideturtle()
	p.speed(10)
	#p.getscreen().tracer(1,0)
	p.left(90)  #因为原画笔默认朝向东
	p.penup()   
	p.goto(x,y)
	p.pendown()   #以上三条语句完成画笔的移动且不在画布上留下痕迹
	t = tree([p], 110, 65, 0.6375)
	time.sleep(2)
	print('画笔的数量为：{}'.format(len(p.getscreen().turtles())))

def main():
	makeTree(0,-200)
	makeTree(0,0)
	makeTree(300,-200)
main()
'''

#七段数码管显示日期
'''
import turtle
import time

def forwardRight():
	turtle.fd(30)
	turtle.right(90)

def forwardLeft():
	turtle.fd(30)
	turtle.left(90)

def drawNumber(number):
	if number == 1 or number == 4:
		turtle.penup()
		coordinate = turtle.position()
		turtle.goto(coordinate[0] + 30,coordinate[1])
		turtle.pendown()

	if number == 0:
		forwardRight()
		turtle.fd(30)
		forwardRight()
		forwardRight()
		turtle.fd(30)
		turtle.fd(30)
	elif number == 1:
		#
		turtle.right(90)
		turtle.fd(30)
		turtle.fd(30)
	elif number == 2:
		forwardRight()
		forwardRight()
		forwardLeft()
		forwardLeft()
		turtle.fd(30)
	elif number == 3:
		forwardRight()
		forwardRight()
		turtle.fd(30)
		turtle.bk(30)
		turtle.left(90)
		forwardRight()
		turtle.fd(30)
	elif number == 4:
		#
		turtle.right(90)
		turtle.fd(30)
		turtle.fd(30)
		turtle.bk(30)
		turtle.right(90)
		forwardRight()
		turtle.fd(30)
	elif number == 5:
		turtle.fd(30)
		turtle.bk(30)
		turtle.right(90)
		forwardLeft()
		forwardRight()
		forwardRight()
		turtle.fd(30)
	elif number == 6:
		turtle.fd(30)
		turtle.bk(30)
		turtle.right(90)
		turtle.fd(30)
		forwardLeft()
		forwardLeft()
		forwardLeft()
		turtle.fd(30)
	elif number == 7:
		turtle.fd(30)
		turtle.right(90)
		turtle.fd(30)
		turtle.fd(30)
	elif number == 8:
		forwardRight()
		turtle.fd(30)
		forwardRight()
		forwardRight()
		forwardRight()
		turtle.fd(30)
		turtle.bk(30)
		turtle.left(90)
		turtle.fd(30)
	elif number == 9:
		forwardRight()
		turtle.fd(30)
		turtle.fd(30)
		turtle.bk(30)
		turtle.right(90)
		forwardRight()
		turtle.fd(30)

def getNowTime():
	shijian = time.localtime(time.time())
	year = shijian[0]
	month = shijian[1]
	day = shijian[2]
	hour = shijian[3]
	minute = shijian[4]
	second = shijian[5]
	return year,month,day

def swith(number):
	#将获取的时间转换为列表
	lis = list(map(int,str(number)))
	if len(lis) < 2:     #给只用单个数字的列表，在0位添加数字0 	
		lis.insert(0,0)
	return lis 

def sevenNixieLight(lis):
	for i in range(0,len(lis)):
		drawNumber(lis[i])
		turtle.penup()
		turtle.goto(40*(i+1),0)
		turtle.setheading(0)
		turtle.pendown()

def main():
	year, month, day = getNowTime()
	yearlis = swith(year)
	monthlis = swith(month)
	daylis =swith(day)
	timelis = yearlis + monthlis + daylis
	
	#turtle.setup(900,500,-120,15)
	turtle.pensize(5)
	turtle.pencolor('black')
	turtle.hideturtle()
	#turtle.dot(3,'red') #在编写时用于检测画笔在进行1或者4的绘制时，是否产生了移动
	sevenNixieLight(timelis)
	time.sleep(2)
main()
'''

#读操作
'''
def main():#read()
	fname = input("Enter filename:")
	infile = open(fname,'r')
	data = infile.read()
	print(data)
#readline()
fname = input("Enter filename:")
infile = open(fname,'r')
for i in range(5):
	data = infile.readline()
	print(data[:-1])
'''

#写入操作
'''
outfile = open('outfile.txt','w')
outfile.writelines(['Hellow', ' ', 'world'])
outfile.close()
infile = open('outfile.txt', 'r')
data = infile.read()
print(data)
'''

#文件的拷贝
'''
def main():
	#用户输入文件名
	f1 = input('Enter a souce file:').strip()
	f2 = input('Enter a souce file:').strip()

	#打开文件
	infile = open(f1,'r')
	outfile = open(f2,'w')

	#拷贝数据
	countLines = countChars = 0
	for line in infile:
		countLines += 1
		countChars += len(line)
		outfile.write(line)
	print(countLines, 'lines and', countChars, 'chars copied.')

	infile.close()
	outfile.close()

main()
'''

#数据驱动的文件读取实例
#根据data.txt中的数据，使用turtle来动态绘制图形路径
#元素1：路径前进的像素数；元素2：转动方向：0为左，1为右；元素3：转动角度；元素4-6：绘制颜色的rgb值
'''
import turtle
import time

def main():
	#设置窗口信息
	turtle.title('数据驱动的动态路径绘制')
	turtle.setup(800, 600, 0, 0)
	#设置画笔
	pen = turtle.Turtle()
	pen.color('red')
	pen.width(5)
	pen.shape('turtle')
	pen.speed(5)

	#读取文件
	result = []
	file = open('data.txt','r')
	for line in file:
		result.append(list(map(float, line.split(','))))
	for i in range(len(result)):
		print(result[i],'/n')
	

	#动态绘制
	for i in range(len(result)):
		pen.color(result[i][3],result[i][4],result[i][5])
		pen.fd(result[i][0])
		if result[i][1] :
			pen.right(result[i][2])
		else:
			pen.left(result[i][2])
	pen.goto(0,0)
	time.sleep(2)
if __name__ == '__main__':
	main()
'''

#合并文件地址簿（多文件操作）
'''
ftele1 = open('TeleAddressBook.txt', 'rb')   #为防止中文出错，采用读取二进制的形式
ftele2 = open('EmainAddressBook.txt', 'rb')

ftele1.readline() #跳过第一行
ftele2.readline() #跳过第一行
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

list1Name = []
list1Tele = []
list2Name = []
list2Email = []
#读取TeleAddresSBook文件
for line in lines1:
	elements = line.split()
	list1Name.append(str(elements[0].decode('gbk')))
	list1Tele.append(str(elements[1].decode('gbk')))
#读取EmailAddressBook文件
for line in lines2:
	elements = line.split()
	list2Name.append(str(elements[0].decode('gbk')))
	list2Email.append(str(elements[1].decode('gbk')))

#生成新的列表
lines = []
lines.append('姓名\t   电话  \t  邮箱\n')  #创建文件表头
#按照索引方式遍历姓名列表1
for i in range(len(list1Name)):
	s = ''
	if list1Name[i] in list2Name:
		a = list2Name.index(list1Name[i])
		s = '\t'.join([list1Name[i],list1Tele[i],list2Email[a]])
		s += '\n'
	else:
		s = '\t'.join([list1Name[i],list1Tele[i],str('  -----  ')])
		s += '\n'
	lines.append(s)
#处理姓名列表2中剩余的姓名
for i in range(len(list2Name)):
	s = ''
	if list2Name[i] not in list1Name:
		s = '\t'.join([list2Name[i], str('  -----  '),list2Email[i]])
		s += '\n'
	lines.append(s)
#将新生成的合并数据文件写入新的文件中
ftele3 = open('AddressBook.txt','w')
ftele3.writelines(lines)
#关闭文件
ftele1.close()
ftele2.close()
ftele3.close()
print('The addressBooks are merged!')
'''

#字典的实例
#统计词频（英文文章）<字典的键为单词，字典的值为单词出现的频率>
'''
import turtle
import time

##定义全局变量##
#词频排列显示个数
count = 10
#单词频率数组-作为y轴数据
data = []
#单词数组-作为x轴数据
words = []
#y轴显示放大倍数-可以根据词频数量进行调节
yScale = 6
#x轴显示放大倍数-可以根据count数量进行调节
xScale = 30
#从点（x1,y1）到点（x2,y2）绘制线段
def drawLine(t, x1, y1, x2, y2):
	t.penup()
	t.goto(x1,y1)
	t.pendown()
	t.goto(x2,y2)

#在坐标（x,y）处写字
def drawText(t, x, y, text):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.write(text)

#绘制一个柱体
def drawRectangle(t, x, y):
	x = x * xScale
	y = y * yScale
	drawLine(t, x-5, 0, x-5, y)
	drawLine(t, x-5, y, x+5, y)
	drawLine(t, x+5, y, x+5, 0)
	drawLine(t, x+5, 0, x-5, 0)

#绘制多个柱体
def drawBar(t):
	for i in range(count):
		drawRectangle(t, i+1, data[i])

def drawGraph(t):
	#绘制x\y轴线
	drawLine(t, 0, 0, 360, 0)
	drawLine(t, 0, 0, 0, 360)

	#x轴：坐标及描述
	for x in range(count):
		x = x + 1  #向右移动一位，为了不画在原点上
		drawText(t, x*xScale-4, -20, (words[x-1]))
		drawText(t, x*xScale-4, data[x-1]*yScale+10, data[x-1])
	drawBar(t)	
#####################################Turtle End############################################

def processLine(line, wordsCounts):
	#使用空格替换标点符号
	line = replacePunctuations(line)
	#从每一行获取每个词
	words = line.split()
	for word in words:
		if word in wordsCounts:
			wordsCounts[word] += 1
		else:
			wordsCounts[word] = 1   #否则为字典增加新的一项
#使用空格替换标点
def replacePunctuations(line):
	for ch in line:
		if ch in '~@#$%^&*()_-+=<>?/,.:;{}[]|\'"':
			line = line.replace(ch, '')
	return line

def main():
	#用户输入一个文件名
	fileName = input('Enter a filename:').strip()
	infile = open(fileName, 'r')

	#建立用于计算词频的空字典
	wordCounts = {}
	for line in infile:
		processLine(line.lower(), wordCounts)

	#从字典中获取数据对
	pairs = list(wordCounts.items())
	#列表中的数据对交换位置，数据对排序
	items = [[x,y] for (y,x) in pairs]
	items.sort()

	#输出count个数词频结果
	for i in range(len(items)-1, len(items)-count-1, -1):
		print(items[i][1]+"\t"+str(items[i][0]))
		data.append(items[i][0])
		words.append(items[i][1])

	#根据词频结果绘制柱状图
	turtle.title('词频结果柱状图')
	turtle.setup(900, 750, 0, 0)
	t = turtle.Turtle()
	t.hideturtle()
	t.width(3)
	drawGraph(t)
	turtle.done()
main()
#time.sleep(8)
'''
#字典实例二，使用字典改进多文件操作
'''
ftele1 = open('TeleAddressBook.txt', 'rb')   #为防止中文出错，采用读取二进制的形式
ftele2 = open('EmainAddressBook.txt', 'rb')

ftele1.readline() #跳过第一行
ftele2.readline() #跳过第一行
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

#定义字典
dic1 = {}
dic2 = {}

for line in lines1:
	elements = line.split()
	#将文本读出来的bytes转换为str类型
	dic1[elements[0]] = str(elements[1].decode('gbk'))

for line in lines2:
	elements = line.split()
	dic2[elements[0]] = str(elements[1].decode('gbk'))

lines = []
lines.append('姓名：\t    电话：   \t   邮箱：\n')

for key in dic1:
	s = ''
	if key in dic2.keys():
		s = '\t'.join([str(key.decode('gbk')), dic1[key], dic2[key]])
		s += '\n'
	else:
		s = '\t'.join([str(key.decode('gbk')), dic1[key], str('   -----   ')])
		s += '\n'
	lines.append(s)

for key in dic2:
	s = ''
	if key not in dic1.keys():
		s = '\t'.join([str(key.decode('gbk')), str('   -----   '), dic2[key]])
		s += '\n'
	lines.append(s)
ftele3 = open('AddressBook.txt','w')
ftele3.writelines(lines)
#关闭文件
ftele1.close()
ftele2.close()
ftele3.close()
print('The addressBooks are merged!')
'''

#6周课后练习1
'''
file = open('test.txt', 'r')
print(file.read())

file = open('test.txt', 'br')
print(file.read())
'''
#练习3哈姆雷特,词频统计
'''
#自己思考编写版
#定义全局变量
wordCounts = {}
lineLis1 = []
printCount = 10

#符号替换函数
def replacePunctuation(line):
	for element in line:
		if element in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~': 
			line = line.replace(element,' ')
	return line

#统计单词的数量
def countWordsNumber(list):
	for i in list:
		for j in i: #采用循环嵌套方法是因为该列表中的元素也为列表
			wordCounts[j] = wordCounts.get(j,0) + 1
			#if i in wordCounts.keys():
			#	wordsCounts[j] += 1
			#else:
			#	wordsCouunts[j] = 1

def main():
	file = open('hamlet.txt', 'r')
	for line in file:
		line = line.lower()
		line = replacePunctuation(line)
		lineLis1.append(line.split())
	#print(lineLis1)
	countWordsNumber(lineLis1)
	items = list(wordCounts.items())
	items.sort(key=lambda x:x[1], reverse = True)
	for i in range(printCount):
		print(items[i][0] +'\t'+ str(items[i][1]))

main()
'''
#课后练习给出的答案
'''
def getText():
	txt = open('hamlet.txt', 'r').read()
	txt = txt.lower()
	for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
		txt = txt.replace(ch, ' ')
	return txt
hamletText = getText()
words = hamletText.split()
#print(words)
counts = {}
for word in words:
	counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse = True)
for i in range(10):
	word, count = items[i]
	print('{0:<10}{1:>5}'.format(word, count))
'''
'''
#添加了一个冠词，连词，代词的库
excludes = ['also', 'and', 'too', 'another', 'first', 'second', 'third', 'now', 'than', 'before', 'after', 'afterwards', 'earlier', 'later', 'immediately', 'soon', 'next', 'gradually', 'suddenly', 'finally', 'to', 'from', 'behind', 'beside', 'beyond', 'above', 'below', 'around', 'outside', 'but', 'yet', 'however', 'nevertheless', 'although', 'because', 'since', 'so', 'therefore', 'furthermore', 'otherwise', 'indeed', 'surely', 'necessarily', 'certainly', 'a', 'an', 'the', 'i', 'you', 'he', 'she', 'they', 'we', 'me', 'him', 'her', 'them', 'us', 'my', 'his', 'your', 'their', 'that', 'those', 'myself', 'himself', 'yourself', 'themselves', 'who', 'what', 'which', 'some', 'many', 'both', 'any', 'whom', 'whose', 'whatever', 'whichever', 'whoever', 'whomever', 'one', 'of', 'in', 'on', 'up', 'down', 'is', 'are', 'it','this','for', 'as', 'not', 'have', 'will', 'do', 'no', 'with', 'be', 'all', 'our', 'by', 'or', 'if']
#自己思考编写版
#定义全局变量
wordCounts = {}
lineLis1 = []
printCount = 10

#符号替换函数
def replacePunctuation(line):
	for element in line:
		if element in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~': 
			line = line.replace(element,' ')
	return line#统计单词的数量


def countWordsNumber(list):
	for i in list:
		for j in i: #采用循环嵌套方法是因为该列表中的元素也为列表
			if j in excludes:
				continue
			else:
				wordCounts[j] = wordCounts.get(j,0) + 1
			#if i in wordCounts.keys():
			#	wordsCounts[j] += 1
			#else:
			#	wordsCouunts[j] = 1

def main():
	file = open('hamlet.txt', 'r')
	for line in file:
		line = line.lower()
		line = replacePunctuation(line)
		lineLis1.append(line.split())
	#print(lineLis1)
	countWordsNumber(lineLis1)
	items = list(wordCounts.items())
	items.sort(key=lambda x:x[1], reverse = True)
	for i in range(printCount):
		print(items[i][0] +'\t'+ str(items[i][1]))

main()
'''

#体育竞技分析IPO模式
#一名运动员的能力值表示为其发球时能赢得该回合比赛的概率
'''
from random import random

def main():
	printIntro() #打印程序的介绍性信息
	probA, probB, n = getInputs() #获取程序运行时所需要的参数
	winsA, winsB = simNGames(n,probA,probB) #利用球员A和B的能力值，模拟N次比赛，并获得结果
	printSummary(winsA, winsB) #输出球员A和B获胜比赛的次数和频率

def printIntro():
	print('This program simulates a game between two.')
	print('There are two players, A and B')
	print('Probability (a number between 0 and 1)is uesd')

def getInputs():
	a = eval(input('What is the prob.player A wins?'))
	b = eval(input('What is the prob.player B wins?'))
	n = eval(input('How many games to simulate?'))
	return a, b, n

def simNGames(n,probA,probB): #核心函数
	winA = 0
	winB = 0
	for i in range(n):
		scoreA,scoreB = simOneGame(probA,probB)#模拟一次比赛
		if scoreA < scoreB:
			winB += 1
		else:
			winA += 1
	return winA,winB

def simOneGame(probA,probB):
	scoreA = 0
	scoreB = 0
	serving = 'A'  #用与表示发球权
	while not gameOver(scoreA,scoreB):
		if serving == 'A':
			if random() < probA: #通过随机数和概率可以确定发球方是否赢得了比分
				scoreA += 1
			else:
				serving = 'B'
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = 'A'
	return scoreA,scoreB

def gameOver(a,b):
	return a == 15 or b == 15 

def printSummary(winA,winB):
	n = winA + winB
	print('\nGames simulated:%d'%n)
	print('Win for A:{0}({1:0.1%})'.format(winA,winA/n))
	print('Win for B:{0}({1:0.1%})'.format(winB,winB/n))
'''

#面向过程的程序设计
#抛铅球问题，忽略空气阻力
'''
from math import sin,cos,pi,radians

angle = eval(input("Enter the launch angle (in degrees):"))
vel = eval(input('Enter the initial velocity (in meters/sec):'))
h0 = eval(input('Enter the initial height (in meters):'))
time = eval(input('Enter the time interval:'))

xpos = 0 
ypos = h0

theta = radians(angle)
xvel = vel * cos(theta)
yvel = vel * sin(theta)

while ypos >= 0:
	xpos = xpos + xvel*time 
	yvel1 = yvel - 9.8 * time 
	ypos = ypos + (yvel + yvel1)/2
	yvel = yvel1
print('\nDistance traveled:{0:0.1f}meters'.format(xpos))
'''
#模块化流程
'''
from math import sin,cos,radians

def main():
	angle,vel,h0,time = getInputs()
	xpos, ypos = 0,h0 
	xvel, yvel = getXYComponent(vel, angle)
	while ypos >= 0:
		xpos,ypos,yvel = updataPosition(time,xpos,ypos,xvel,yvel)
	print('\nDistance traveled:{0:0.1f}meters'.format(xpos))

def getInputs():
	angle = eval(input("Enter the launch angle (in degrees):"))
	vel = eval(input('Enter the initial velocity (in meters/sec):'))
	h0 = eval(input('Enter the initial height (in meters):'))
	time = eval(input('Enter the time interval:'))
	return angle,vel,h0,time

def getXYComponent(vel,angle):
	theta = radians(angle)
	xvel = vel * cos(theta)
	yvel = vel * sin(theta)
	return xvel,yvel

def updataPosition(time,xpos,ypos,xvel,yvel):
	xpos = xpos + xvel*time 
	yvel1 = yvel - 9.8 * time 
	ypos = ypos + (yvel + yvel1)/2
	return xpos,ypos,yvel1

main()
'''

#面向对象的程序设计
#类的定义
#学生成绩计算，找到平均GPA最高的学生
'''
class Student:
	"""docstring for Student"""
	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)

	def getName(self):
		return self.name

	def getHours(self):
		return self.hours

	def getQPoints(self):
		return self.qpoints

	def gpa(self):
		return self.qpoints/self.hours

def makeStudent(infoStr):
	name, hours, qpoints = infoStr.split('\t')
	return Student(name, hours, qpoints)

def main():
	fileName = input('Enter name the grade file:')
	infile = open(fileName,'r')

	best = makeStudent(infile.readline())

	for line in infile:
		s = makeStudent(line)
		if s.gpa() > best.gpa():
			best = s
	infile.close()

	print('The best student is :', best.getName())
	print('Hours:',best.getHours())
	print('GPA:',best.gpa())

main()		
'''
#使用面向对象的方法重构抛铅球问题
#单独定义了一个Projectile类的一个文件
'''
from Projectile import *

def getInput():
	angle = eval(input("Enter the launch angle (in degrees):"))
	vel = eval(input('Enter the initial velocity (in meters/sec):'))
	h0 = eval(input('Enter the initial height (in meters):'))
	time = eval(input('Enter the time interval:'))
	return angle,vel,h0,time

def main():
	angle, vel, h0, time = getInput()
	shot = Projectile(angle, vel, h0)
	while shot.getY() >= 0:
		shot.updata(time)
	print('\nDistance traveled:{0:0.1f}meters'.format(shot.getX()))

main()
'''

#graphics库的使用
'''
from graphics import *
from time  import sleep
#p1 = Point(100,100)
#p2 = Point(150,80)
#circ = Circle(Point(100,100),30)

win = GraphWin()
#p1.draw(win)
#p2.draw(win)
#circ.draw(win)

#使用这种方式画出来的其实为右眼，因为两个变量表示同一个对象更改一个变量的内容，另一个变量也随之更改了
#leftEye = Circle(Point(80,80),5)
#leftEye.setFill('yellow')
#leftEye.setOutline('red')
#rightEye = leftEye
#rightEye.move(40,0)
#Circle(Point(120,80),5)
#leftEye.draw(win)

face = Circle(Point(100,95), 50)
leftEye = Circle(Point(80,80),5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = Circle(Point(120,80),5)
rightEye.setFill('yellow')
rightEye.setOutline('red')
mouth = Line(Point(80,110),Point(120,110))

face.draw(win)
mouth.draw(win)
leftEye.draw(win)
rightEye.draw(win)

time.sleep(8)
'''

#连续点击10次鼠标返回坐标值
'''
from graphics import *

def main():
	win = GraphWin('Click Me!')
	for i in range(10):
		p = win.getMouse()
		print('You click at:', p.getX(),p.getY())

if __name__ == '__main__':
	main()
'''

#交互式绘制五边形
'''
from graphics import *

def main():
	win = GraphWin('Draw a polygon.',300,300)
	win.setCoords(0,0,300,300)
	message = Text(Point(150,20), 'Click on five points.')
	message.draw(win)
	#获得多边形的5个点
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)
	p4 = win.getMouse()
	p4.draw(win)
	p5 = win.getMouse()
	p5.draw(win)
	#使用Ploygon对象绘制多边形
	polygon = Polygon(p1,p2,p3,p4,p5)
	polygon.setFill('peachpuff')
	polygon.setOutline('black')
	polygon.draw(win)
	#等待响应鼠标事件，退出程序
	message.setText('Click anywhere to quit.')
	win.getMouse()

if __name__ == '__main__':
	main()
'''

#温度转换程序
'''
from graphics import *

win = GraphWin('Celsius Converter', 400, 300)
win.setCoords(0, 0, 3.0, 4.0)
#绘制接口
Text(Point(1,3),'Celsius Temperature:').draw(win)
Text(Point(1,1),'Fahrenheit Temperature:').draw(win)

input1 = Entry(Point(2,3),5)
input1.setText('0.0')
input1.draw(win)

output1 = Entry(Point(2,1),5)
output1.draw(win)

button = Text(Point(1.5,2.0),'Covert It')  #一个假的按钮
button.draw(win)

Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

win.getMouse()

celsius = eval(input1.getText())
fahrenheit = 9.0/5.0  * celsius + 32

output1.setText(fahrenheit)
button.setText('Quit')

win.getMouse()
win.close()
'''

#TK库的简单GUI示例
'''
from tkinter import *

#tk = Tk()
#label = Label(tk, text = 'Welcome to Pyton TKinter')
#button = Button(tk, text = 'Click me')
#label.pack()
#button.pack()
#tk.mainloop()

def processOk(): #定义了按钮的回调函数
	print('OK button is clicked.')

def processCancel():
	print('Cancel button is clicked.')

def main():
	tk = Tk()
	btnOK = Button(tk, text = 'OK', fg = 'red', command = processOk)   #command:指令;在这里设置回调函数
	btnCancel = Button(tk, text = 'Cancel', bg = 'yellow', command = processCancel)
	btnOK.pack()
	btnCancel.pack()
	tk.mainloop()
main()
'''
'''
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 200, height = 200)
canvas.pack()
canvas.create_text(100, 40, text = 'Welcome to Tkinter', fill = 'blue', font = ('Times', 16))
myImage = PhotoImage(file = 'python_logo.gif') #只支持gif格式的图片
canvas.create_image(10, 70, anchor = NW, image = myImage)
canvas.create_rectangle(10, 70, 190, 130)

tk.mainloop()
'''
'''
from tkinter import *

def main():
	tk = Tk()
	canvas = Canvas(tk, width = 400, height = 400)
	canvas.pack()

	def moveRectangle(event):
		if event.keysym == 'Up':
			canvas.move(1,0,-5)
		elif event.keysym == 'Down':
			canvas.move(1,0,5)
		elif event.keysym == 'Left':
			canvas.move(1,-5,0)
		elif event.keysym == 'Right':
			canvas.move(1,5,0)

	canvas.create_rectangle(180, 180, 220, 220, fill = 'red')
	canvas.bind_all('<KeyPress-Up>',moveRectangle)
	canvas.bind_all('<KeyPress-Down>',moveRectangle)
	canvas.bind_all('<KeyPress-Left>',moveRectangle)
	canvas.bind_all('<KeyPress-Right>',moveRectangle)
	tk.mainloop()

main()
'''
#变色版温度转换程序
'''
from graphics import *

def convert(input):
	celsius = eval(input.getText())
	fahrenheit = 9.0/5.0  * celsius + 32
	return fahrenheit

def colorChange(win,input):
	cnum = eval(input.getText())
	weight = cnum / 100
	newColor = color_rgb(int(255*weight), int(66+150*(1-weight)), int(255*(1-weight)))
	win.setBackground(newColor)

def main():
	win = GraphWin('Celsius Converter', 400, 300)
	win.setCoords(0, 0, 3.0, 4.0)
	#绘制接口
	Text(Point(1,3),'Celsius Temperature:').draw(win)
	Text(Point(1,1),'Fahrenheit Temperature:').draw(win)

	input1 = Entry(Point(2,3),5)
	input1.setText('0.0')
	input1.draw(win)

	output1 = Entry(Point(2,1),5)
	output1.draw(win)

	button = Text(Point(1.5,2.0),'Covert It')  #一个假的按钮
	button.draw(win)

	Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

	win.getMouse()

	result = convert(input1)
	output1.setText(result)

	colorChange(win,input1)

	button.setText('Quit')

	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()
'''
#turtle库的温习
'''
import turtle 

def main():
	turtle.pensize(3)
	turtle.penup()
	turtle.goto(-200,-50)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color('red')
	turtle.circle(40,steps = 3)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(-100,-50)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color('blue')
	turtle.circle(40,steps = 4)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(0,-50)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color('yellow')
	turtle.circle(40,steps = 5)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(100,-50)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color('green')
	turtle.circle(40,steps = 6)
	turtle.end_fill()

	turtle.penup()
	turtle.goto(200,-50)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color('purple')
	turtle.circle(40)
	turtle.end_fill()

	turtle.color('blue')
	turtle.penup()
	turtle.goto(-100,50)
	turtle.pendown()
	turtle.write('Cool colorful shapes',font = ('Times', 18, 'bold'))
	turtle.hideturtle()

	turtle.done()

if __name__ == '__main__':
	main()
'''

#TKinter实例：聊天界面
'''
from tkinter import *
import time

def main():
	def sendMsg():
		strMsg = '我' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
		txtMsgList.insert(END, strMsg, 'greencolor')
		txtMsgList.insert(END, txtMsg.get('0.0', END))
		txtMsg.delete('0.0', END)

	def sendMsgEvent(event):
		if event.keysym == 'Up':
			sendMsg()

	def cancelMsg():
		txtMsg.delete('0.0', END) #0.0代表文本内容的开始，END代表文本内容的结束

	#创建窗口
	tk = Tk()
	tk.title('与python聊天中')

	#创建frame容器
	frmLT = Frame(widt = 500, height = 320, bg = 'white')
	frmLC = Frame(widt = 500, height = 150, bg = 'white')
	frmLB = Frame(widt = 500, height = 30)
	frmRT = Frame(widt = 200, height = 500)

	#创建控件
	txtMsgList = Text(frmLT)
	txtMsgList.tag_config('greencolor', foreground = '#008C00')
	txtMsg = Text(frmLC)
	txtMsg.bind('<KeyPress-Up>', sendMsgEvent)
	btnSend = Button(frmLB, text = '发送', width = 8, command = sendMsg)
	btnCancel = Button(frmLB, text = '取消', width = 8, command = cancelMsg)
	imgInfo = PhotoImage(file = 'python.gif')
	lblImage = Label(frmRT, image = imgInfo)
	lblImage.image = imgInfo

	#窗口布局
	frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
	frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
	frmLB.grid(row=2, column=0, columnspan=2)
	frmRT.grid(row=0, column=2, rowspan=3)

	#固定大小
	frmLT.grid_propagate(0)
	frmLC.grid_propagate(0)
	frmLB.grid_propagate(0)
	frmRT.grid_propagate(0)

	btnSend.grid(row=2, column=0)
	btnCancel.grid(row=2, column=1)
	lblImage.grid()
	txtMsg.grid()
	txtMsgList.grid()

	#主事件循环
	tk.mainloop()

if __name__ == '__main__':
	main()
'''

#turtle库实例：数字时钟
'''
from turtle import *
from datetime import *

def Skip(step):
	penup()
	fd(step)
	pendown()

def mkHand(name, length):
	#注册表针形状，建立表针turtle
	reset()
	Skip(-length*0.1)
	begin_poly()
	fd(length*1.1)
	end_poly()
	handForm = get_poly()
	register_shape(name, handForm)

def Init():
	global secHand, minHand, hurHand, printer
	#重置turtle，指向北
	mode('logo')
	#建立三个表针对象并初始化
	mkHand('secHand', 125)
	mkHand('minHand', 130)
	mkHand('hurHand', 90)
	secHand = Turtle()
	secHand.shape('secHand')
	minHand = Turtle()
	minHand.shape('minHand')
	hurHand = Turtle()
	hurHand.shape('hurHand')
	#设置指针的拉伸系数和指针对象的画笔速度
	for hand in secHand, minHand, hurHand:
		hand.shapesize(1, 1, 3)
		hand.speed(0)

	#设置输出文本的Turtle
	printer = Turtle()
	printer.hideturtle()
	printer.penup()

def SetupClock(radians):
	#建立表的外框
	reset()
	pensize(7)
	for i in range(60):
		Skip(radians)
		if i % 5 == 0:
			fd(20)
			Skip(-radians-20)
		else:
			dot(5)
			Skip(-radians)
		right(6)

def Week(t):
	week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
	return week[t.weekday()]

def Date(t):
	y = t.year
	m = t.month
	d = t.day
	return '%s %d %d' % (y, m, d)

def Tick():
	t = datetime.today()
	second = t.second + t.microsecond*0.000001
	minute = t.minute + second/60
	hour = t.hour + minute/60
	secHand.setheading(6*second)
	minHand.setheading(6*minute)
	hurHand.setheading(30*hour)

	tracer(False)
	printer.fd(65)
	printer.write(Week(t), align = 'center', font = ('Courier', 14, 'bold'))
	printer.back(130)
	printer.write(Date(t), align = 'center', font = ('Courier', 14, 'bold'))
	printer.home()
	tracer(True)
	
	#100ms后继续调用tick
	ontimer(Tick, 100)

def main():
	tracer(False)
	Init()
	SetupClock(160)
	tracer(True)
	Tick()
	mainloop()

if __name__ == '__main__':
	main()
'''

#turtle 艺术
'''
from turtle import *
from random import *

def main():
	setup(800, 600, 0, 0)
	#tracer(False)
	bgcolor('black')
	snow()
	ground()
	#tracer(True)
	mainloop()

def snow():
	hideturtle()
	pensize(2)
	speed(100)
	for i in range(100):
		r = random()
		g = random()
		b = random()
		pencolor(r, g, b)
		penup()
		setx(randint(-350,350))
		sety(randint(1,270))
		pendown()
		#雪花的花瓣数
		dens = randint(8, 12)
		snowsize = randint(10,14)
		for j in range(dens):
			fd(snowsize)
			backward(snowsize)
			right(360/dens)

def ground():
	hideturtle()
	speed(100)
	for i in range(400):
		pensize(randint(5,10))
		x = randint(-400,350)
		y = randint(-280,-1)
		r = -y/280
		g = -y/280
		b = -y/280
		pencolor(r, g, b)
		penup()
		goto(x,y)
		pendown()
		forward(randint(40,100))

if __name__ == '__main__':
	main()
'''
#画彩虹
'''
from turtle import *

#色彩转换算法，将HSV模式下的色相转换为RGB模式下的色相
def HSB2RGB(hues):
	hues = hues * 3.59 #100转成359范围
	rgb=[0.0,0.0,0.0]
	i = int(hues/60)%6
	f = hues/60 -i
	if i == 0:
	    rgb[0] = 1; rgb[1] = f; rgb[2] = 0
	elif i == 1:
	    rgb[0] = 1-f; rgb[1] = 1; rgb[2] = 0
	elif i == 2:
	    rgb[0] = 0; rgb[1] = 1; rgb[2] = f
	elif i == 3:
	    rgb[0] = 0; rgb[1] = 1-f; rgb[2] = 1
	elif i == 4:
	    rgb[0] = f; rgb[1] = 0; rgb[2] = 1
	elif i == 5:
	    rgb[0] = 1; rgb[1] = 0; rgb[2] = 1-f
	return rgb

def rainbow():
	hues = 0.0
	color(1,0,0)
	#绘制彩虹
	hideturtle()
	speed(100)
	pensize(3)
	penup()
	goto(-400,-300)
	pendown()
	right(110)
	for i in range(100):
		circle(1000)
		right(0.13)
		hues = hues + 1
		rgb = HSB2RGB(hues)
		color(rgb[0], rgb[1], rgb[2])
	penup()

def main():
	setup(800, 600, 0, 0)
	bgcolor((0.8,0.8,0.9))
	#tracer(False)
	rainbow()
	#输出文字
	goto(100,-100)
	pendown()
	color('red')
	write('Rainbow', align = 'center', font = ('Script MT Bold', 80, 'bold'))
	#tracer(True)

	mainloop()

if __name__ == '__main__':
	main()
'''

#os平台编程
#打印一个目录下的全部文件\
'''
import os

path = input('请输入路径：')
for root, dirs, files in os.walk(path):
	for file in files:
		print(os.path.join(root,file))
'''
#将文件夹下所有文件名字后增加一个字符串
'''
import os 

path = input('请输入路径名称：')
for root, dirs, files in os.walk(path):
	for name in files:
		fname, fext = os.path.splitext(name)
		os.rename(os.path.join(root, name), os.path.join(root, fname + 'py' + fext))
'''

#sched库的介绍
'''
import sched, time

def print_time(msg = 'default'):
	print('当前时间', time.time(), msg)

s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(5, 1, print_time, argument=('延迟5秒，优先级1',))
s.enter(3, 2, print_time, argument=('延迟3秒，优先级2',))
s.enter(3, 1, print_time, argument=('延迟3秒，优先级1',))
s.run()
print(time.time())
'''

#NumPy库的实例
#GPS定位技术原理实现（不考虑各种改正）
'''
from numpy import *

i = 1
c = 0.299792458 #定义光速
x = zeros((6,4)) #存储6个卫星的x,y,z,t的值

while i <= 6:
	print('%s,%d' % ('please input (x,y,z,t) of group',i))
	temp = input()
	x[i-1] = temp.split()
	j = 0
	while j < 4:
		x[i-1][j] = float(x[i-1][j])
		j += 1
	i += 1
a = zeros((4,4)) #定义一个系数矩阵
b = zeros((4,1)) #定义一个常数矩阵
j = 0
while j < 4:
	a[j][0] = 2 * (x[5][0] - x[j][0])
	a[j][1] = 2 * (x[5][1] - x[j][1])
	a[j][2] = 2 * (x[5][2] - x[j][2])
	a[j][3] = 2 * c*c  * (x[j][3] - x[5][3])
	b[j][0] = x[5][0]*x[5][0] - x[j][0]*x[j][0] + \
			  x[5][1]*x[5][1] - x[j][1]*x[j][1] + \
			  x[5][2]*x[5][2] - x[j][2]*x[j][2] + \
			  c*c * (x[j][3]*x[j][3] - x[5][3]*x[5][3])
	j += 1 
a = linalg.inv(a) #对矩阵a进行求逆
print(dot(a, b))
print('........................................')
print(x)
print('........................................')
print(a)
print('........................................')
print(b)
'''

#Matplotlib库的实例
#散点图绘制
'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6], 'ro')
plt.ylabel('Description of y value.')
plt.show()
'''

#三角函数图的绘制
'''
import numpy as np
from matplotlib.pyplot import *

x = np.linspace(-np.pi, np.pi, 256, endpoint=True) #生成从-π到π等间隔的256个值的数组
#print(x)
c, s = np.cos(x*x), np.sin(x)
plot(x,c,'ro',label='sin(x)')
plot(x,s,label='$cos(x^2)$')
xlabel('xlabel')
ylabel('ylabel')
legend()
title('This is Title')
show()
'''
#一图表多子图显示
'''
from matplotlib.pyplot import *

subplot(221)
subplot(222)
#subplot(121)
subplot(224)
show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

def f(t):
	return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
'''
#直方图的绘制
'''
import numpy as np 
import matplotlib.pyplot as plt
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
plt.hist(x, 50, normed = 1, facecolor = 'b')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, 0.025, r'$\mu = 100,\  \sigma = 15$')  #在指定位置添加文本标识
plt.axis([40, 160, 0, 0.03])
plt.show()
'''
#k-means应用实例(经典的聚类算法，其本质是将n个数据对象划分为k个聚类，使同一个聚类中的数据对象相似度较高，不同聚类中的数据对象相似度较小)
#其基本思想为：以空间中k个点为中心，进行聚类，对最靠近他们的对象归类。通过迭代的方法，逐次更新各聚类中心的值，直到得到最好的聚类结果
import numpy as np
import matplotlib.pyplot as plt

def main():
	##step 1:load dataSet
	print('setp 1: loading data.....')
	dataSet = []
	dataSetFile = open('./testSet.txt')
	for line in dataSetFile:
		lineArr = line.strip().split('\t')
		#print(lineArr)
		dataSet.append([float(lineArr[0]), float(lineArr[1])])
	#print(dataSet)

	#step 2:clustering...
	print('step 2: clustering...')
	dataSet = np.mat(dataSet)
	print(dataSet)

	k = 4 #设定聚类中心的个数
	centers_result, clusterAssignment_result = kmeans(dataSet, k, 100)  #设置100为最大迭代次数

	#step 3:show the result
	print('show the result...')
	showCluster(dataSet, k, centers_result, clusterAssignment_result)

#设置初始聚类中心
def initCenters(dataSet, k):
	numSamples, dim = dataSet.shape 
	centers = np.zeros((k, dim))
	for i in range(k):
		index = int(np.random.uniform(0, numSamples))  #通过随机选取一个行数来定义初始化聚类中心,这两行代码的意思是在0到样本矩阵总行数之间选取一个随机整字index，将样本矩阵中index行的数据赋值到初始中心矩阵中
		centers[i,:] = dataSet[index,:]
	print(centers)
	return centers

#计算样本点到聚类中心的距离
def dist2Centers(sample, centers):
	k = centers.shape[0]
	dis2Centers = np.zeros(k)
	for i in range(k):
		dis2Centers[i] = np.sqrt(np.sum(np.power(sample - centers[i,:], 2)))
	return dis2Centers

def kmeans(dataSet, k, iterNum):
	numSamples = dataSet.shape[0]
	iterCount = 0

	#clusterAssignment stores which cluster this sample belongs to,
	clusterAssignment = np.zeros(numSamples)
	clusterChanged = True

	#step 1:initialize centers
	centers = initCenters(dataSet, k)
	while clusterChanged and iterCount < iterNum :
		clusterChanged = False
		iterCount += 1

		##step 2:for each sample
		for i in range(numSamples):
			dis2Cent = dist2Centers(dataSet[i,:], centers) #计算样本数据与聚类中心的距离，返回应该为一个列矩阵
			minIndex = np.argmin(dis2Cent) #选出该样本点到那个聚类中心最段，并返回该聚类中心的索引值（就是第几个聚类中心）

			##step 3:update its belonged cluster
			if clusterAssignment[i] != minIndex: #如果该样本点对应的聚类中心并不是其最短距离的聚类中心，则更新归类矩阵
				clusterChanged = True
				clusterAssignment[i] = minIndex

		#step 4:update centers		
		for j in range(k):
			pointsInCluster = dataSet[np.nonzero(clusterAssignment[:] == j)[0]] #返回该类下的所有样本数据
			centers[j,:] = np.mean(pointsInCluster, axis=0) #对该类下的所有样本数据取均值，并用该均值重新定义聚类中心
		print('Congratulations, Cluster Achieved!')
	return centers, clusterAssignment

#对聚类后的样本数据，分颜色处理
def showCluster(dataSet, k, centers, clusterAssignment):
	numSamples, dim = dataSet.shape

	mark = ['or', 'ob', 'og', 'om']


	# draw all samples
	for i in range(numSamples):
		markIndex = int(clusterAssignment[i])
		plt.plot(dataSet[i,0], dataSet[i,1], mark[markIndex])

	mark = ['Dr', 'Db', 'Dg', 'Dm']
	#draw the centers
	for i in range(k):
		plt.plot(centers[i,0], centers[i,1], mark[i], markersize = 17)

	plt.show()

main()
