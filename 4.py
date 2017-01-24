# -*- coding: utf - 8 -*-
# 车辆有100
cars = 100
# 车内可以载客4人
space_in_a_car = 4.0
# 司机有30人
drivers = 30
# 乘客有90人
passengers = 90
# 没有司机的汽车等于车辆的数目减去司机的数目
cars_not_driven = cars - drivers
# 可以驾驶的车辆数等于司机的数量
cars_driven = drivers
# 载客容量等于可以驾驶的车辆数目乘以每辆车内的空间数量
carpoool_capacity = cars_driven * space_in_a_car
# 每辆车能得到的乘客数等于乘客数除以可以驾驶的车辆数目
average_passengers_per_car = passengers / cars_driven

# 可以使用的车辆数目
print "There are", cars , "available."
# 但是这里只有30个司机
print "There are only", drivers, "drivers available."
# 今天又不能行使的车辆数目
print "There will be", cars_not_driven, "empty cars today."
# 今天我们能够运输的最多乘客数
print "We can transport", carpoool_capacity, "people today."
# 今天我们能运输的乘客的数量
print "We have", passengers, "to carpool today."
# 我们需要让每辆车承载3名乘客
print "We need to put about", average_passengers_per_car, "in each car."
