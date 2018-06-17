#自己思考编写版
#定义全局变量
wordCounts = {}
lineLis1 = []
printCount = 10

#符号替换函数
def replacePunctuation(line):
	for element in line:
		if element in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~': 
			line = line.replace(element,' ')
	return line

line = open('hamlet.txt', 'r').read()
line = line.lower()
line = replacePunctuation(line)
lineLis1 = line.split()

#print(lineLis1)

file = open('ceshiziji.txt', 'w')
for word in lineLis1:
	file.write(word +'|')