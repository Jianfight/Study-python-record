# 二分查找算法
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


# # 选择排序算法
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


# 递归
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


# 快速排序
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


# 散列表的应用形式：防止人重复投票
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


# 广度优先搜索算法
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


# 狄克特斯拉算法

# 定义查找未处理的节点中开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 狄克斯特拉函数
def dikesitela_search(graph, costs, parents, processed):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

# 定义一个显示路径的函数
def show_path(parents, list_path, finishing_node):
    n = finishing_node
    if n == None:
        list_path.reverse()
        return list_path
    else :
        list_path.append(n)
        node_name = parents[n]
        return show_path(parents, list_path, node_name)

# 构建graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# 构建costs
costs = {}
infinity = float('inf')
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 构建parents
parents = {}
parents['start'] = None
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 构建processed列表
processed = []

# 构建graph1
graph1 = {}
graph1['start'] = {}
graph1['start']['a'] = 5
graph1['start']['b'] = 2

graph1['a'] = {}
graph1['a']['c'] = 4
graph1['a']['d'] = 2

graph1['b'] = {}
graph1['b']['a'] = 8
graph1['b']['d'] = 7

graph1['c'] = {}
graph1['c']['d'] = 6
graph1['c']['fin'] = 3

graph1['d'] = {}
graph1['d']['fin'] = 1

graph1['fin'] = {}

# 构建costs
costs1 = {}
infinity = float('inf')
costs1['a'] = 5
costs1['b'] = 2
costs1['c'] = infinity
costs1['d'] = infinity
costs1['fin'] = infinity

# 构建parents
parents1 = {}
parents1['start'] = None
parents1['a'] = 'start'
parents1['b'] = 'start'


# 将构建好的数据代入算法中求解。
dikesitela_search(graph1, costs1, parents1, processed)
path_list = []
path = show_path(parents1,path_list, finishing_node='fin')
print(path)










