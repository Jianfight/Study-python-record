#体育竞技分析IPO模式
#一名运动员的能力值表示为其发球时能赢得该回合比赛的概率
from random import random

def main():
	printIntro() #打印程序的介绍性信息
	probA, probB, n = getInputs() #获取程序运行时所需要的参数
	winsA, winsB = simNGames(n,probA,probB) #利用球员A和B的能力值，模拟N次比赛，并获得结果
	printSummary(winsA, winsB) #输出球员A和B获胜比赛的次数和频率

def printIntro():
	print('This program simulates a game between two.')
	print('There are two players, A and B')
	print('Probability (a number between 0 and 1)is uesd')

def getInputs():
	a = eval(input('What is the prob.player A wins?'))
	b = eval(input('What is the prob.player B wins?'))
	n = eval(input('How many games to simulate?'))
	return a, b, n

def simNGames(n,probA,probB): #核心函数
	winA = 0
	winB = 0
	for i in range(n):
		scoreA,scoreB = simOneGame(probA,probB)#模拟一次比赛
		if scoreA < scoreB:
			winB += 1
		else:
			winA += 1
	return winA,winB

def simOneGame(probA,probB):
	scoreA = 0
	scoreB = 0
	serving = 'A'  #用与表示发球权
	while not gameOver(scoreA,scoreB):
		if serving == 'A':
			if random() < probA: #通过随机数和概率可以确定发球方是否赢得了比分
				scoreA += 1
			else:
				serving = 'B'
		else:
			if random() < probB:
				scoreB += 1
			else:
				serving = 'A'
	return scoreA,scoreB

def gameOver(a,b):
	return a == 15 or b == 15 

def printSummary(winA,winB):
	n = winA + winB
	print('\nGames simulated:%d'%n)
	print('Win for A:{0}({1:0.1%})'.format(winA,winA/n))
	print('Win for B:{0}({1:0.1%})'.format(winB,winB/n))