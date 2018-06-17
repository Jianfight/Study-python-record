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

# 创建人际关系图
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

import collections










