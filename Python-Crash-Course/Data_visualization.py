"""《python编程从入门到实践》-数据可视化"""

import matplotlib.pyplot as plt
import random
import pygal

'''
#绘制折线图
x = [1, 2, 3, 4, 5,]
squares = [1, 4, 9, 16, 25,]
plt.plot(x, squares)

#  设置图标标题并给坐标轴加上标签
plt.title('Squares Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squates of Value', fontsize=14)

#  设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
'''

#绘制散点图
'''
x_value = list(range(1, 1001))
#y = [1, 4, 9, 16, 25,]
y = [x**2 for x in x_value] #自动计算数据,列表解析

plt.scatter(x_value, y, s=200, edgecolor='none', c=y, cmap=plt.cm.Greens)

#  设置图标标题并给坐标轴加上标签
plt.title('Squares Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Squates of Value', fontsize=14)

#  设置坐标轴的取值范围
plt.axis([0, 1200, 0, 1100000])

plt.show()
'''

#随机漫步示例
'''
class RandomWalk():
    """生成随机漫步数据的类"""

    def __init__(self, num_points=500):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步数据都始于（0，0）
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_value) < self.num_points:
            # 决定前进方向和沿这个方向前进的距离
            x_direction = random.choice([-1, 1])
            x_distance = random.choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = random.choice([-1, 1])
            y_distance = random.choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #  拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #  计算下一个点的x和y
            new_x = self.x_value[-1] + x_step
            new_y = self.y_value[-1] + y_step

            self.x_value.append(new_x)
            self.y_value.append(new_y)

while True:
    # 创建一个RandWalk的实例
    points = int(input('请输入随机漫步的点数：'))
    rw = RandomWalk(points)
    rw.fill_walk()

    #  设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, s=1)

    #  突出起点和终点
    plt.scatter(0, 0, s=100, c='green')
    plt.scatter(rw.x_value[-1], rw.y_value[-1], s=100, c='red')

    #  隐藏坐标轴
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n):')
    if keep_running == 'n':
        break
'''

#pygal库
'''
class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return random.randint(1, self.num_sides)
'''

'''
#创建一个六面的骰子
die = Die()

#掷几次骰子，并将结果存储在列表中
results = []
for num_roll  in range(1000):
    result = die.roll()
    results.append(result)

#分析结果,统计各个面出现的次数
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
'''
'''
#  同时掷两个骰子
die_1 = Die()
die_2 = Die()

#掷几次骰子，并将结果存储在列表中
results = []
for num_roll  in range(1000):
    result = die_1.roll() + die_2.roll() 
    results.append(result)

#分析结果,统计各个面出现的次数
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Result of rolling two D6 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die2_visual.svg')
'''

'''
# 根据csv格式的天气数据绘制，相应的最高和最低气温图表。
import csv
import datetime #为了将字符串式的日期转换为相应的日期格式。

#分析CSV文件,从文件中获取最高气温,最低气温，日期
filename = input("Please enter name of file: ")
with open(filename) as f :
    reader = csv.reader(f)
    heard_row = next(reader)
    #print(heard_row)

    #显示文件头内容和各个内容的索引，可知日期的索引为0，最高气温的索引为1
    # for index, column_row in enumerate(heard_row):
    #     print(index, column_row)

    #将数据中的最高温度提取到一个列表中
    highs = []
    dates = []
    lows = []
    for row in reader: #遍历文件中的余下各行。

        # high = int(row[1])
        # highs.append(high)

        # low = int(row[3])
        # lows.append(low)

        # date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
        # dates.append(date)

        # 修改成一种更加安全的读取方式，防止某部分数据丢失而导致程序异常
        # 如果某一项数据在某一段时间内缺失，那么该时间段的数据将不会考虑
        try:
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "miss date.")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形。
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # 从文件名中截取城市名称和日期
    city_and_date = filename.split('_')
    data_city = city_and_date[0]
    current_date = city_and_date[2]
    data_date = current_date.split('.')[0]

    # 设置图形格式
    plt.title("Daily high and low temperatures " + data_date + 
    "\n" + data_city, fontsize=24)

    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
'''

'''# # 制作世界人口地图：json格式
# import json
# from pygal_maps_world.i18n import COUNTRIES
#
# def get_country_code(country_name):
#     """根据指定的国家，返回Pygal使用的两个字母的国别码"""
#     for code, name in COUNTRIES.items():
#         if name == country_name:
#             return code
#     # 如果没有找到指定的国家，就返回None
#     return None
#
# # print(get_country_code('Andorra'))
# # print(get_country_code('Afghanistan'))
#
#
# filename = input("Please enter name of file: ")
# with open(filename) as f :
#     pop_data = json.load(f)
#
# # 打印每个国家2010年的人口数量
# for pop_dict in pop_data:
#     if pop_dict['Year'] == "2010":
#         country_name = pop_dict["Country Name"]
#         population = int(float(pop_dict['Value']))
#         code = get_country_code(country_name)
#         if code:
#             print(code + ":" + str(population))
#         else :
#              print('ERROR - ' + country_name)

import pygal
import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.style import LightColorizedStyle, RotateStyle

# wm.title = "North, Central, and South America"

# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
#
# wm.render_to_file('america.svg')

# wm.title = 'Population of Countries in North America'
# wm.add('North America',{'ca':3412600, 'us':309349000, 'mx':113423000})
# wm.render_to_file('na_population.svg')


def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('Afghanistan'))


filename = input("Please enter name of file: ")
with open(filename) as f :
    pop_data = json.load(f)

#定义一个字典来存放国别码和2010人口数量
cc_population = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

# 将收集到的数据根据人口数量进行分组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc,pop in cc_population.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else :
        cc_pop_3[cc] = pop
# 打印相应人口规模中的国家数量
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

# 开始绘制图表

# 设置图表的基础颜色
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)

wm = pygal.maps.world.World(style=wm_style)

# 向图表中添加相应的数据
wm.title = 'World Population in 2010, by Country.'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)
wm.render_to_file('world_population.svg')
'''

# 使用网站API进行网站源数据的更新，以保证程序可以对最新的数据信息进行可视化。


# 测试requests库
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 搜索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# # 研究第一个库
# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict)) # 返回第一个字典中共包含了多少键值
# # for key in sorted(repo_dict.keys()): # 打印出相应的键值
# #     print(key)
#
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# # 将每一个库的信息提取出来
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
#     print('\n')

# 将从API获取的信息进行可视化
names, stars, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    # 为了在图表中添加每个项目的描述信息，将Bar类中add()的参数改为一个元素为字典的列表。
    # 字典中存放的是星数和项目的描述。
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 制作图表
my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

# 通过Config类，来定制图标的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')



