#-*-coding:utf-8-*-
people = 30
cars = 40
buses = 15

#如果小汽车的数量大于人的数量并且小汽车的数量小于公交车的数量则说明我们应该开小汽车
if cars > people and cars < buses:
	print "We should take the cars."
elif cars < people : #当以上条件不成立时，如果小汽车的数量小于人的数量则说明我们不应该开车
	print "We should not take the cars."
else: #否则说明我们不能决定
	print "We can't decide."

#如果公交车的数量多于小汽车的数量或者人的数量大于公交车的数量
if buses > cars or people > buses:
	print "That's too many buses." #
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
#如果人的数量大于公交车的数量则说明我们应该乘坐公交车
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stsy home then."