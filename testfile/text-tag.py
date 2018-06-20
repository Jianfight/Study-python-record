'''
from tkinter import *

root = Tk()

text1 = Text(root,width=30,height=5)
text1.pack()

text1.insert(INSERT,'I Love FishC.com!')
#第一个参数为自定义标签的名字
#第二个参数为设置的起始位置，第三个参数为结束位置
#第四个参数为另一个位置
text1.tag_add('tag1','1.7','1.12','1.14')
#用tag_config函数来设置标签的属性
text1.tag_config('tag1',background='yellow',foreground='red')
#新的tag会覆盖旧的tag
mainloop()
'''
'''
from tkinter import *
import webbrowser

root = Tk()

text = Text(root,width=30,height=5)
text.pack()

text.insert(INSERT,"I Love FishC.com!")

text.tag_add('link','1.7','1.16')
text.tag_config('link',foreground='blue',underline=True)

def show_arrow_cursor(event):
     text.config(cursor='arrow')

def show_xterm_cursor(event):
     text.config(cursor='xterm')
def click(event):
     webbrowser.open('http://baidu.com')

text.tag_bind('link','<Enter>',show_arrow_cursor)
text.tag_bind('link','<Leave>',show_xterm_cursor)
text.tag_bind('link','<Button-1>',click)

mainloop()
'''
'''
from tkinter import *
root = Tk()
# 创建两个Label
Label(root,text = '1').grid()
# 在第1行，第11列放置lb2
Label(root,text = '2').grid(row = 0,column = 10)
Label(root,text = '3').grid(row = 0,column = 5)
root.mainloop()
'''
'''
from tkinter import *
root = Tk()
# 创建两个Label
lb1 = Label(root,text = '1')
lb2 = Label(root,text = '2')

# 将lb1和lb2均grid到(0,0)位置
lb1.grid(row = 0,column = 0)
lb2.grid(row = 0,column = 0)

def forgetLabel():
    # grid_slaves返回grid中(0,0)位置的所有组件
    # grid_forget将这个组件从grid中移除（并未删除，可以使用grid再将它显示出来)
    root.grid_slaves(0,0)[0].grid_forget() 

# 我测试时grid_salves返回的第一个值为lb2，最后grid的那一个    
Button(root,text = 'forget last',command = forgetLabel).grid(row = 1)

root.mainloop()
'''

from turtle import *
from datetime import *
 
def Skip(step):
    penup()
    forward(step)
    pendown()
 
def mkHand(name, length):
    #注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm)
 
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo")# 重置Turtle指向北
    #建立三个表针Turtle并初始化
    mkHand("secHand", 125)
    mkHand("minHand",  130)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    #建立输出文字Turtle
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
     
def SetupClock(radius):
    #建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)
         
def Week(t):    
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
def Tick():
    #绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
     
    tracer(False)  
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    tracer(True)
 
    ontimer(Tick, 100)#100ms后继续调用tick
 
def main():
    #tracer(False)
    Init()
    SetupClock(160)
    #tracer(True)
    Tick()
    mainloop()
 
if __name__ == "__main__":       
    main()