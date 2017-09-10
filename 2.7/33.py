#-*-coding:utf-8-*-
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i 
	numbers.append(i)
	
	i += 1
	print "Nunber now: " , numbers
	print "At the bottom i is %d" % i 
	
print "The numbers: "

for num in numbers:
	print num 

	

def while_function(number_stop):
	i = 0
	numbers = []

	while i < int(number_stop):
		print "At the top i is %d" % i 
		numbers.append(i)
		
		i += int(scan)
		print "Nunber now: " , numbers
		print "At the bottom i is %d" % i 
		
number_stop = raw_input("Please input termination number> ")
scan = raw_input("Please input scan> ")
while_function(number_stop)


j = 0
numbers = []
for j in range (6):
	print "At the top j is %d" % j
	numbers.append(j)
	print "Nunber now: " , numbers
	print "At the bottom j is %d" % j