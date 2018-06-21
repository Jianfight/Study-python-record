# 二分查找算法
# region Description
# 二分查找必须已有序的数据结构作为数据源，不然会出现奇怪的结果。
# 二分查找所需要的查找次数为log已2为底n 次
# # 定义二分查找算法
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = int((low + high) / 2)
#         guess = list[mid]
#
#         if guess == item:
#             return mid
#         if guess < item:
#             low = mid + 1
#         else :
#             high = mid - 1
#     return None
#
# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 3))
#
# # import random
# # my_list = list(range(70,500))
# # my_item = random.randint(70,500)
# # print(my_list)
# # print(my_item)
# # print(binary_search(my_list, my_item))
# endregion


# # 选择排序算法
# region Description
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest :
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest_index = findSmallest(arr)
#         newArr.append(arr.pop(smallest_index))
#     return newArr
#
# # 测试代码
# import random
#
# def randomList(list_length):
#     list = []
#     for i in range(list_length):
#         list.append(random.randint(0, list_length))
#     return list
#
# test_number = eval(input("Please input length of array: "))
# my_list = randomList(test_number)
# print(my_list)
# print(selectionSort(my_list))
# endregion


# 递归
# region Description
# # 计算阶乘的递归函数
# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         if x == 1:
#             return 1
#         else :
#             return x * factorial(x-1)
#
# n = eval(input("计算n的阶乘，n = :"))
# print(factorial(n))

# 使用递归来对列表求和
# def sum_list(list, sum, index):
#     # 以递归的方式求和
#     if index == len(list):
#         return sum
#     else :
#         sum += list[index]
#         index += 1
#         return sum_list(list, sum, index)
# # 书籍中给出的答案
# def sum_recursion(list):
#     if list == []:
#         return 0
#     return list[0] + sum_recursion(list[1:])

# def sum_list_circulate(list):
#     sum_circulate = 0
#     for i in range(len(list)):
#         sum_circulate += list[i]
#     return sum_circulate
#
# # 使用递归找最大值
# def max_recursion(list, max_number,index):
#     if index == len(list):
#         return max_number
#     else:
#         if (max_number - list[index]) < 0:
#             max_number = list[index]
#             index += 1
#             return max_recursion(list, max_number, index)
#         else :
#             index += 1
#             return max_recursion(list, max_number, index)
# # 书籍中给出的答案
# def max_recusion_2(list):
#     if len(list) == 2:
#         return list[0] if list[0] > list[1] else list[1]
#     sub_max = max_recusion_2(list[1:])
#     return list[0] if list[0] > sub_max else sub_max

# # 测试代码
# import random
#
# def randomList(list_length):
#     list = []
#     for i in range(list_length):
#         list.append(random.randint(0, list_length))
#     return list
#
# test_number = eval(input("Please input length of array: "))
# my_list = randomList(test_number)
# print(my_list)
#
# sum_a = 0
# index_a = 0
# print('递归求和为：{0}'.format(sum_list(my_list,sum_a,index_a)))
#
# print('循环求和为：{0}'.format(sum_list_circulate(my_list)))
# # 递归求最大值
# print('递归求最大值：{0}'.format(max_recursion(my_list, sum_a, index_a)))
# print(max(my_list))
# endregion


# 快速排序
# region Description
#
# def quickSort(array):
# #     if len(array) < 2: # 基线条件：数组内没有元素或者只包含一个元素时，不用对其进行排序
# #         return array
# #     else :
# #         pivot = array[0] # 在选择基准值上还有待改进
# #         less = [i for i in array[1:] if i <= pivot]
# #         greater = [j for j in array[1:] if j > pivot]
# #         return quickSort(less) + [pivot] + quickSort(greater)
#
# # 测试代码
# import random
#
# def randomList(list_length):
#     list = []
#     for i in range(list_length):
#         list.append(random.randint(0, list_length))
#     return list
#
# test_number = eval(input("Please input length of array: "))
# my_list = randomList(test_number)
# print(my_list)
# print(quickSort(my_list))
# endregion


# 散列表的应用形式：防止人重复投票
# region Description
# voted = {}
# def check_voter(name):
#     if voted.get(name):
#         print("kick them out!")
#     else :
#         voted[name] = True
#         print("let them vote!")
#
# # 测试代码
# check_voter('tom')
# check_voter('wang')
# check_voter('tom')
#
# # 散列表的应用形式：网站缓存
# cache = {}
# def get_page(url):
#     if cache.get(url):
#         return cache[url]
#     else :
#         data = get_data_from_server(url) # 这个函数仅仅是一个伪函数，为了方便理解
#         cache[url] = data
#         return data
# endregion


# 广度优先搜索算法
# region Description
#
# # 创建人际关系图
# graph = {}
# graph['you'] = ['alice', 'bob', 'claire']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom', 'jonny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['jonny'] = []
#
# # 暂时将这个函数作为，判断搜索结果的函数
# def person_is_seller(name):
#     return name[-1] == 'm'
#
# import collections # 引进该模块用于创建队列
#
# # 编写相应的广度优先算法
# def search(name):
#     search_queue = collections.deque()  # 创建一个双端队列
#     search_queue += graph[name] # 将第一个节点的邻居添加都搜索队列中
#     searched = [] # 该列表用于记录检查过的人，防止搜索进入死循环
#     while search_queue:
#         person = search_queue.popleft() # 将双端队列中最左边的元素提取出来
#         if person not in searched:
#             if person_is_seller(person):
#                 print(person + ' is a mango seller!')
#                 return True
#             else:
#                 print(person)
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
# search('you')
# endregion


# 狄克特斯拉算法
# region Description
#
# # 定义查找未处理的节点中开销最低的节点
# def find_lowest_cost_node(costs):
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
# # 狄克斯特拉函数
# def dikesitela_search(graph, costs, parents, processed):
#     node = find_lowest_cost_node(costs)
#     while node is not None:
#         cost = costs[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs)
#
# # 定义一个显示路径的函数
# def show_path(parents, list_path, finishing_node):
#     n = finishing_node
#     if n == None:
#         list_path.reverse()
#         return list_path
#     else :
#         list_path.append(n)
#         node_name = parents[n]
#         return show_path(parents, list_path, node_name)
#
# # 构建graph
# graph = {}
# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
#
# graph['a'] = {}
# graph['a']['fin'] = 1
#
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
#
# graph['fin'] = {}
#
# # 构建costs
# costs = {}
# infinity = float('inf')
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity
#
# # 构建parents
# parents = {}
# parents['start'] = None
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None
#
# # 构建processed列表
# processed = []
#
# # 构建graph1
# graph1 = {}
# graph1['start'] = {}
# graph1['start']['a'] = 5
# graph1['start']['b'] = 2
#
# graph1['a'] = {}
# graph1['a']['c'] = 4
# graph1['a']['d'] = 2
#
# graph1['b'] = {}
# graph1['b']['a'] = 8
# graph1['b']['d'] = 7
#
# graph1['c'] = {}
# graph1['c']['d'] = 6
# graph1['c']['fin'] = 3
#
# graph1['d'] = {}
# graph1['d']['fin'] = 1
#
# graph1['fin'] = {}
#
# # 构建costs
# costs1 = {}
# infinity = float('inf')
# costs1['a'] = 5
# costs1['b'] = 2
# costs1['c'] = infinity
# costs1['d'] = infinity
# costs1['fin'] = infinity
#
# # 构建parents
# parents1 = {}
# parents1['start'] = None
# parents1['a'] = 'start'
# parents1['b'] = 'start'
#
#
# # 将构建好的数据代入算法中求解。
# dikesitela_search(graph1, costs1, parents1, processed)
# path_list = []
# path = show_path(parents1,path_list, finishing_node='fin')
# print(path)
# endregion


# 贪婪算法
# region Description
# # 集合覆盖问题的一种解法-近似算法(approximation algorithm)：求解一个广播节目在哪些电台播出可以覆盖所有地区
#
# # 创建需要被覆盖地区的集合
# states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
#
# # 创建电台字典:电台名称为键，其覆盖的地区为值
# stations = {}
# stations['kone'] = set(['id', 'nv', 'ut'])
# stations['ktwo'] = set(['wa', 'id', 'mt'])
# stations['kthree'] = set(['or', 'nv', 'ca'])
# stations['kfour'] = set(['nv', 'ut'])
# stations['kfive'] = set(['ca', 'az'])
#
# # 创建一个用来存储最终选择的电台
# final_stations = set()
#
# # 编写该问题的近似算法
# def approximation_algorithm(states_needed, stations, final_stations):
#     while states_needed:
#         best_station = None
#         states_covered = set()
#         for station, states in stations.items():
#             covered = states_needed & states
#             if len(covered) > len(states_covered):
#                 best_station = station
#                 states_covered = covered
#         states_needed -= states_covered
#         final_stations.add(best_station)
#
# approximation_algorithm(states_needed, stations, final_stations)
# print(final_stations)
# endregion


# 动态规划
# region Description
# # 最长公共子串（伪代码）
# if word_[i] == word_[j]:
#     cell[i][j] = cell[i-1][j-1] + 1
# else :
#     cell[i][j] = 0

# 最长公共子序列（伪代码）
# if word_a[i] == word_b[j]:
#     cell[i][j] = cell[i-1][j-1] + 1
# else :
#     cell[i][j] = max(cell[i-1][j], cell[i][j-1])
# endregion


# K最邻近算法
import  math
a = math.sqrt((3-2)**2 + (4-5)**2 + (4-1)**2 + (1-3)**2 + (4-1)**2)

print(a)



#k-means应用实例(经典的聚类算法，其本质是将n个数据对象划分为k个聚类，使同一个聚类中的数据对象相似度较高，不同聚类中的数据对象相似度较小)
#其基本思想为：以空间中k个点为中心，进行聚类，对最靠近他们的对象归类。通过迭代的方法，逐次更新各聚类中心的值，直到得到最好的聚类结果
# region Description
# import numpy as np
# import matplotlib.pyplot as plt
#
# def main():
# 	##step 1:load dataSet
# 	print('setp 1: loading data.....')
# 	dataSet = []
# 	dataSetFile = open('./testSet.txt')
# 	for line in dataSetFile:
# 		lineArr = line.strip().split('\t')
# 		#print(lineArr)
# 		dataSet.append([float(lineArr[0]), float(lineArr[1])])
# 	#print(dataSet)
#
# 	#step 2:clustering...
# 	print('step 2: clustering...')
# 	dataSet = np.mat(dataSet)
# 	print(dataSet)
#
# 	k = 4 #设定聚类中心的个数
# 	centers_result, clusterAssignment_result = kmeans(dataSet, k, 100)  #设置100为最大迭代次数
#
# 	#step 3:show the result
# 	print('show the result...')
# 	showCluster(dataSet, k, centers_result, clusterAssignment_result)
#
# #设置初始聚类中心
# def initCenters(dataSet, k):
# 	numSamples, dim = dataSet.shape
# 	centers = np.zeros((k, dim))
# 	for i in range(k):
# 		index = int(np.random.uniform(0, numSamples))  #通过随机选取一个行数来定义初始化聚类中心,这两行代码的意思是在0到样本矩阵总行数之间选取一个随机整字index，将样本矩阵中index行的数据赋值到初始中心矩阵中
# 		centers[i,:] = dataSet[index,:]
# 	print(centers)
# 	return centers
#
# #计算样本点到聚类中心的距离
# def dist2Centers(sample, centers):
# 	k = centers.shape[0]
# 	dis2Centers = np.zeros(k)
# 	for i in range(k):
# 		dis2Centers[i] = np.sqrt(np.sum(np.power(sample - centers[i,:], 2)))
# 	return dis2Centers
#
# def kmeans(dataSet, k, iterNum):
# 	numSamples = dataSet.shape[0]
# 	iterCount = 0
#
# 	#clusterAssignment stores which cluster this sample belongs to,
# 	clusterAssignment = np.zeros(numSamples)
# 	clusterChanged = True
#
# 	#step 1:initialize centers
# 	centers = initCenters(dataSet, k)
# 	while clusterChanged and iterCount < iterNum :
# 		clusterChanged = False
# 		iterCount += 1
#
# 		##step 2:for each sample
# 		for i in range(numSamples):
# 			dis2Cent = dist2Centers(dataSet[i,:], centers) #计算样本数据与聚类中心的距离，返回应该为一个列矩阵
# 			minIndex = np.argmin(dis2Cent) #选出该样本点到那个聚类中心最段，并返回该聚类中心的索引值（就是第几个聚类中心）
#
# 			##step 3:update its belonged cluster
# 			if clusterAssignment[i] != minIndex: #如果该样本点对应的聚类中心并不是其最短距离的聚类中心，则更新归类矩阵
# 				clusterChanged = True
# 				clusterAssignment[i] = minIndex
#
# 		#step 4:update centers
# 		for j in range(k):
# 			pointsInCluster = dataSet[np.nonzero(clusterAssignment[:] == j)[0]] #返回该类下的所有样本数据
# 			centers[j,:] = np.mean(pointsInCluster, axis=0) #对该类下的所有样本数据取均值，并用该均值重新定义聚类中心
# 		print('Congratulations, Cluster Achieved!')
# 	return centers, clusterAssignment
#
# #对聚类后的样本数据，分颜色处理
# def showCluster(dataSet, k, centers, clusterAssignment):
# 	numSamples, dim = dataSet.shape
#
# 	mark = ['or', 'ob', 'og', 'om']
#
#
# 	# draw all samples
# 	for i in range(numSamples):
# 		markIndex = int(clusterAssignment[i])
# 		plt.plot(dataSet[i,0], dataSet[i,1], mark[markIndex])
#
# 	mark = ['Dr', 'Db', 'Dg', 'Dm']
# 	#draw the centers
# 	for i in range(k):
# 		plt.plot(centers[i,0], centers[i,1], mark[i], markersize = 17)
#
# 	plt.show()
#
# main()
# endregion












