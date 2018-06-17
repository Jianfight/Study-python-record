#list1 = ['o', 'p', 'q', 'r', 's', 't']
#for i in list1:
#	print('Hellow, {}'.format(i))

#for i in range(len(list1)):
#	list1[i] = i
#	print(list1[i])

#list2 = ['q', 'w', 'q', 'a', 'b', 'q']
#for i in range(list2.count('q')):
#	list2.remove('q')
#	print(list2)

#练习3-(4,5,6,7)
'''
list3 = [1, 2, 3, 4, 5]
print(list3)
print('{}无法赴约。'.format(list3.pop(0)))
list3.insert(0,'w')
print(list3)
print('我们找到了一个更大的餐桌，我可以邀请更多的伙伴了，好开心。')
list3.insert(0,'j')
print(list3)
list3.insert(int(len(list3)/2),'k')
print(list3)
list3.append('l')
print(list3)
for i in range(len(list3)):
	if len(list3) > 2:
		temp = list3.pop()
		print('{},是在抱歉由于种种原因，无法邀请您来参加晚宴，实在抱歉。'.format(temp))
	else :
		print('{},欢迎您来参加我的晚宴。'.format(list3[0]))
		print('{},欢迎您来参加我的晚宴。'.format(list3[1]))
		break

#print(list3)
for i in range(len(list3)):
	#print(i)
	del list3[0]

print(list3)
'''
#练习3-(8,9,10)
'''
list4 = [5,3,4,1,2]
print(list4)
print(sorted(list4))
print(list4)
print(sorted(list4,reverse=True))
print(list4)
list4.reverse()
print(list4)
list4.reverse()
print(list4)
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
#列表的复制
list5 = ['a', 'b', 'c', 'd', 'e', 'f']
list6 = list5 #使用该方式复制列表是错误的，该方法是将两个变量名同时指向一个列表，而并非是两个变量名自对应一个列表

list5.append('g')
list6.append('h')

print(list5)
print('\n')
print(list6)
'''

#练习4-(10，11，12)
'''
text = 'The first three items in the list are:'
listTemp = text.split()
print(listTemp)
print('\n')
print(listTemp[:3])
print('\n')
print(listTemp[3:6])
print('\n')
print(listTemp[-3:])
'''

#类
'''
class Car():
	"""一次模拟汽车的简单尝试"""

	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 #里程表，添加一个具有默认值的属性

	def get_descriptive_name(self):
		"""返回整洁的描述信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车旅程的消息"""
		print('This car has ' + str(self.odometer_reading) + ' miles on it.')


class ElectricCar(Car):
	"""电动汽车的独特之处(使用继承创建一个子类)"""

	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery = Battery() #将一个类的实例作为属性。

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""

	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶的属性"""
		print('This car has a ' + str(self.battery_size) + '-KWh battery.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', "model's", 2016)
print('\n' + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() #将一个类的实例作为属性后调用者个实例下方法的形式
'''

#文件
'''
with open('pi_digits.txt') as file_object:
	contents = file_object.read()

print(contents)
'''

#json库
'''
import json

filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input('What is your name? ')
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print("We'll remember you when you come back, " + username + "!")
else:
	print("Welcome back, " + username + "!")
'''
#对以上代码进行重构
import json

def get_stored_username():
	"""如果存储了用户名，就获取它"""
	filename = 'username.json'
	try :
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else :
		return username 

def get_new_username():
	"""提示用户输入用户名"""
	username = input('What is your name? ')
	filename = 'username.json'
	with open(filename,'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_username()
	if username :
		print("Welcome back, " + username + '!')
	else :
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()