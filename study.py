#-*- coding: utf-8 -*-
#函数
#内置函数
#number = input("请输入你喜欢的数字，不管其是正是负：");
#numberAbs = abs(int(number));
#print("你输入数字的绝对值为： %f" %numberAbs);
n1 = 255;
n2 = 1000;
print("将255和1000转换为十六进制：%s,%s" %(hex(n1), hex(n2)));

#定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):    #在函数开头添加一个对参数的数据类型的判断，输出相应的错误类型。
        raise TypeError('bad operand type');  #错误的操作数类型。
    if x < 0:
        return -x;
    elif x >= 0:
        return x;
number = input("请输入你喜欢的数字，不管其是正是负：");
numberAbs = my_abs(float(number));
print("你输入数字的绝对值为： %f" %numberAbs);

#定义函数中返回多个值
import math;    #引入数学包
def move(x, y, step, angle=0):
    moveX = x + step * math.cos(math.pi/180*angle);  #角度化弧度的公式为 弧度=π/180*角度
    movey = y + step * math.sin(math.pi/180*angle);
    return moveX, movey;
x, y = move(100, 100, 60, 30);
print ("移动后的坐标为： X = %f, Y = %f" % (x, y));
#练习:解一元二次方程
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type');
    if (b*b - 4*a*c) < 0:
        print("该程序无解。")
    elif (b*b - 4*a*c) >= 0:
        x1 = (-b + math.sqrt(b*b - 4*a*c))/(2 * a);
        x2 = (-b - math.sqrt(b*b - 4*a*c))/(2 * a);
        print ("该一元二次方程的解为：x1 = %.2f, x2 = %.2f" %(x1, x2));
floatA = float(input("请输入一元二次方程的a:"));
floatB = float(input("请输入一元二次方程的b:"));
floatC = float(input("请输入一元二次方程的c:"));
quadratic(floatA, floatB, floatC);

#位置和默认参数
def power(x, n = 2):  #n = 2 的意思为将参数n默认为2，即在调用函数时如果不输入参数n,其就默认为2。
    s = 1;
    while n > 0:
        s = s * x;
        n -= 1;
    return s;
print("2的平方为：%f, 2的三次方为：%f,2的四次方为：%f" %(power(2), power(2, 3), power(2, 4)));
