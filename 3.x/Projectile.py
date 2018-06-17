from math import sin,cos,radians
class Projectile:
	"""docstring for Projectile"""
	def __init__(self, angle, velocity, height):
		#根据给定的发射角度、初始速度和位置创建一个投射体对象
		self.xpos = 0.0
		self.ypos = height
		theta = radians(angle)
		self.xvel = velocity * cos(theta)
		self.yvel = velocity * sin(theta)

	def updata(self, time):
		#更新投射体的状态
		self.xpos = self.xpos + self.xvel*time
		yvel1 = self.yvel - 9.8 * time
		self.ypos = self.ypos + time * (self.yvel + yvel1)/2
		self.yvel = yvel1

	def getY(self):
		return self.ypos

	def getX(self):
		return self.xpos