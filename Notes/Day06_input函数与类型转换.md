# Day06 Python input函数与类型转换


# 1. input()函数


## 什么是input()

`input()` 用于获取用户在控制台输入的数据。

基本格式：

```python
变量 = input("提示信息")
```


例如：

```python
name = input("请输入姓名：")

print(name)
```


运行：

```
请输入姓名：Tom
```

输出：

```
Tom
```


---

# 2. input()的返回值类型


需要注意：

> input()获取到的数据默认都是字符串(str)类型。


例如：

```python
age = input("请输入年龄：")

print(type(age))
```


输入：

```
18
```


输出：

```
<class 'str'>
```


虽然输入的是数字：

```
18
```

但是Python会认为：

```python
"18"
```

而不是：

```python
18
```


---

# 3. 数据类型转换


如果需要进行数学运算，需要转换类型。


常用转换函数：

|函数|作用|
|-|-|
|int()|转换为整数|
|float()|转换为浮点数|
|str()|转换为字符串|


---

## int()转换


示例：

```python
age = input("请输入年龄：")

age = int(age)

print(age + 1)
```


输入：

```
18
```


输出：

```
19
```


---

## float()转换


适用于小数：

```python
money = float(input("请输入金额："))
```


例如：

输入：

```
100.5
```


转换后：

```python
100.5
```


---

# 4. 用户信息输入示例


代码：

```python
name = input("请输入一个姓名: ")

age = input("请输入一个年龄: ")

print(f"您的姓名是: {name}, 年龄是: {age}")
```


流程：

```
用户输入
    ↓
input获取字符串
    ↓
保存到变量
    ↓
print输出
```


---

# 5. 模拟银行卡取款程序


## 初始余额

```python
total = 10000
```


表示：

账户余额：

```
10000元
```


---

## 输入密码


```python
password = input("请输入银行卡密码: ")

print(f"密码正确：{password}")
```


注意：

这里密码也是字符串。


---

## 输入取款金额


错误方式：

```python
withdrawal_amount = input("请输入取款金额: ")

print(total - withdrawal_amount)
```


原因：

```
int类型
+
str类型
```

无法进行数学运算。


---

正确方式：

```python
withdrawal_amount = int(input("请输入取款金额: "))

print(total - withdrawal_amount)
```


或者：

```python
withdrawal_amount = input("请输入取款金额: ")

print(total - int(withdrawal_amount))
```


---

# 6. 简化写法


原本：

```python
withdrawal_amount = input("请输入金额")

withdrawal_amount = int(withdrawal_amount)
```


可以写成：

```python
withdrawal_amount = int(input("请输入金额"))
```


执行顺序：

```text
用户输入
    ↓
input()
    ↓
得到字符串
    ↓
int()
    ↓
转换成整数
    ↓
保存变量
```


---

# 今日总结


今天学习：

- input()函数
- 用户输入数据
- input返回值类型
- 数据类型转换
- int()和float()使用
- 简单用户交互程序


重点：

## 1. input默认返回字符串

```python
input()
```

返回：

```python
str
```


## 2. 数字计算前需要转换

错误：

```python
10 + "5"
```


正确：

```python
10 + int("5")
```


## 3. 常用转换

```python
int()
float()
str()
```


## 4. 程序流程开始变化

以前：

```
代码
 ↓
输出
```


现在：

```
用户输入
 ↓
程序处理
 ↓
输出结果
```
