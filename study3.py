#函数式编程
#函数名是指向函数的变量，如果将函数名指向其他对象，在调用该函数时会出现错误
def add(x, y, f):  #高阶函数：一个函数可以接收另一个函数做为参数。
    return f(x) + f(y);
print("高阶函数：%d" %add(5, -6, abs));
