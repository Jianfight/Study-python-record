#turtle库实例：数字时钟
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