#字面量写法

# print(100) #整数
# print(3.14) #浮点数/小数
# print(True) #布尔值
# print(False) #布尔值
# print("Test") #字符串
# print(None) #空值

# print(True+1) #布尔值可以参与运算，True=1,False=0
# print(False-1) #布尔值可以参与运算，True=1,False=0

#变量--->Python是动态类型语言，一个变量是可以存储不同类型的数据的（但是项目开发中，推荐变量只存储一种类型的数据）
# a = 100 #整数
# print(a) #输出变量的值
# print(type(a)) #输出变量的类型

# a = 152.54 #浮点数
# print(a) #输出变量的值
# print(type(a)) #输出变量的类型

#示例
# base = 20.7
# incr = 50
# print("计算数据的值为：",base + incr) #输出变量的值
# print("进一步计算数据的值为：",base + incr*2) #输出变量的值

#多个变量同时赋值
base, incr = 20.7, 50
print("计算数据的值为：",base + incr) #输出变量的值
print("进一步计算数据的值为：",base + incr*2) #输出变量的值