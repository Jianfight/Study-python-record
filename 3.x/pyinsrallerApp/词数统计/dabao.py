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

#统计单词的数量
def countWordsNumber(list):
	for i in list:
		for j in i: #采用循环嵌套方法是因为该列表中的元素也为列表
			wordCounts[j] = wordCounts.get(j,0) + 1
			#if i in wordCounts.keys():
			#	wordsCounts[j] += 1
			#else:
			#	wordsCouunts[j] = 1

def main():
	fileName = input('Enter file name:')
	file = open(fileName, 'r')
	for line in file:
		line = line.lower()
		line = replacePunctuation(line)
		lineLis1.append(line.split())
	#print(lineLis1)
	countWordsNumber(lineLis1)
	items = list(wordCounts.items())
	items.sort(key=lambda x:x[1], reverse = True)
	for i in range(printCount):
		print(items[i][0] +'\t'+ str(items[i][1]))

main()