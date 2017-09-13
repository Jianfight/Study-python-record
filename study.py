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
#可变参数
def calc(*number):   #在参数名前添加*表示可变参数
    sum = 0;
    for n in number:
        sum = sum + n*n;
    return sum;
list1 = [1, 2, 3];
print ("结果为：%d" %calc(*list1));  #在参数位置输入列表或者元组名并且在其前添加*号，表示将该列表或者元组中的每个元素都当作参数传入函数中。
#关键字参数
def person(name, age, **kw):   #**kw代表一个关键字参数。
    print("name:", name,"age:", age,"other:", kw);
extra = {'city': 'BeiJing', 'job': 'Engineer'};
person('Jian', 25,city = extra['city'], job = extra['job']);
#命名关键字参数
def person(name, age, *, city, job):    # *,代表一个特殊分隔符，其告诉解释器 *,后面的参数为命名关键字参数。
    print("name:", name,"age:", age,"other:", city, job);
person('Jian', 25,city = extra['city'], job = extra['job']);   #在调用有命名关键字的函数时，必须传入参数名，否则解释器会将其默认为位置参数，导致程序出错。但当命名关键字参数有默认值时，调用函数时可以不输入参数名，直接使用默认值。
