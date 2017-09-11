#-*-coding: utf-8 -*-
#name = input("Please enter your name: ");
#print ("Hellow,", name);
#if name == "Jian":
#    print("Yes,you are a good boy.");
#else:
#    print("?????");

#print("""line1: WANG
#Line2: JIAN
#Line3: GOOD""");

#print(3 > 2);
#print(2 > 3);
#print (2 > 3 and 3 > 2);
#print (2 > 3 or 3 > 2);
#print (not False);
#a = 123 ;
#a += 123 ;
#print(a);

n = 123;
f = 456.789;
s1 = "Hellow World.";
s2 = "Hellow \'Jian\'.";
s3 = r'Hellow "Wang".';
s4 = r'''Hellow,
Lisa!''';
print(n, f, s1, s2, s3, s4);

#格式化的学习
a_1 = "World.";
a_2 = 345;
a_3 = 3.1415926;
print ("Hellow, %s. 数字：%2d, %.4f." %(a_1,a_2,a_3));
chengji1 = 72;
chengji2 = 85;
r = ((chengji2 - chengji1) / chengji1) * 100;
print('小明成绩提升的百分点为：%.1f%%' %r);   #%%代表对%字符的转译。

#列表的学习
classmates = ['Ming', 'Tian', 'Zai', 'Jian'];
print(classmates);
print(len(classmates));
for matesName in classmates:
    print(matesName)
print("...................");
n = 0;
length = len(classmates);
while n < length:
    print(classmates[n]);
    n = n + 1;
print ("..................");
tianJia = ['Dan', 'Shi', 'Ming', 'Tian', 'Bu', 'Shang', 'Ban'];
i = 0;
while i < len(tianJia):
    classmates.append(tianJia[i]);  #自动向列表末尾添加元素
    i += 1;
print(classmates);
print("..............................................");
i = 0;
while i < len(tianJia):
    classmates.pop();  #pop函数用于删除列表末尾的元素，pop(x)删除位置为X的元素
    i += 1;
i = 0;
while i < len(tianJia):
    classmates.insert(i,tianJia[i]);  #根据相应的位置向列表中添加元素，如该位置已有元素则原元素向后移动
    i += 1;
print(classmates);
print("..........................................................");
j = 0;
while j < len(tianJia):
    classmates.pop(0);
    j += 1;
classmates.append(tianJia);  #将一个列表添加进另一个列表中，构成一个二维数组
print(len(classmates));
print(classmates[4][3]); #classmates[4]代表的是其包含的tianJia列表，[3]代表的是tianJia列表中的元素
print("............................................................");
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0]);
print(L[1][1]);
print(L[-1][-1]);

#条件判断的学习
s = input("输入你的年薪：（<=5W,<=10W,<=30w）:");
nianXin = int(s);
if 0< nianXin <=50000:
    print("同志请继续努力!!!别忘记你的背后还有你的家庭。");
elif 50000< nianXin <= 100000 :
    print("同志你买房了吗？如果没买，我觉得你可以买了。");
elif 100000 < nianXin <= 300000 :
    print("同志你基本已经实现财务自由了。");
elif nianXin > 300000 :
    print("大腿让我拔根毛。");
elif nianXin == 0:
    print("孩子，请你好好学习。");

#循环
jieCheng = 1;
shu = list(range(101));
shu.pop(0);
print (shu)
for x in shu:    #计算100的阶乘
    jieCheng = jieCheng * x;
print("100的阶乘为：%d." %jieCheng);
print("......................................................")
#使用while循环进行100阶乘的计算
jieCheng = 1;
a = 1;
while a <= 100:
    jieCheng = jieCheng * a;
    a += 1;
print("100的阶乘为：%d." %jieCheng);