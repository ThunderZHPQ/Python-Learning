# Day08 Python条件判断


# 1. 条件判断的作用


程序默认按照代码顺序执行：

```text
第一行
↓
第二行
↓
第三行
```


但是实际程序中，经常需要：

- 如果满足条件，执行A
- 如果不满足条件，执行B


例如：

```
如果余额足够
    扣款
否则
    提示余额不足
```


Python使用：

```python
if
else
```

实现条件判断。


---

# 2. if语句基础结构


格式：

```python
if 条件:
    条件成立执行的代码
```


示例：

```python
score = 695

if score >= 680:
    print("恭喜你，考上了清华大学")
```


执行流程：

```
score >= 680
        |
        ↓
    True?
        |
        ↓
执行print()
```


---

# 3. if-else结构


当条件不满足时，需要执行另一段代码。


格式：

```python
if 条件:
    条件成立执行
else:
    条件不成立执行
```


示例：

```python
score = 600

if score >= 680:
    print("考上清华")
else:
    print("未达到分数线")
```


执行：

如果：

```
score >= 680
```

结果：

```
True
```

执行if。


否则：

执行else。


---

# 4. Python缩进规则 ⭐⭐⭐


Python使用缩进表示代码块。


例如：

```python
if score >= 680:
    print("成功")
```


其中：

```python
print()
```

属于if代码块。


注意：

## 冒号不能省略

正确：

```python
if age >= 18:
```

错误：

```python
if age >= 18
```


---

## 缩进必须保持一致


推荐：

4个空格：

```python
if True:
    print("hello")
```


错误：

```python
if True:
    print("hello")
      print("world")
```


不同缩进会导致：

- 语法错误
- 逻辑错误


---

# 5. 使用逻辑运算符组合条件


多个条件可以使用：

```python
and
or
not
```


例如：

登录验证：


```python
if account == input_account and password == input_password:
    print("登录成功")
else:
    print("登录失败")
```


含义：

账号正确

并且

密码正确


两个条件必须同时满足。


---

# 6. 模拟登录案例


代码：

```python
account = 2678324880

password = 123456


input_account = int(input("请输入账号: "))

input_password = int(input("请输入密码: "))


if input_account == account and input_password == password:
    print("登录成功")
else:
    print("登录失败")
```


流程：

```
输入账号密码

↓

比较账号

↓

比较密码

↓

两个都正确？

↓

输出结果
```


---

# 7. 闰年判断案例 ⭐


闰年规则：

满足以下任意条件：

条件1：

```
能被4整除
并且
不能被100整除
```


或者：


条件2：

```
能被400整除
```


数学表达：

```
(year % 4 == 0 and year % 100 != 0)
or
(year % 400 == 0)
```


Python实现：


```python
year = int(input("请输入年份: "))


if (year % 4 == 0 and year % 100 != 0) \
or (year % 400 == 0):

    print(f"{year}是闰年")

else:

    print(f"{year}不是闰年")
```


---

# 8. 条件判断执行流程


例如：

```python
if 条件:
    A
else:
    B
```


流程：

```
开始

 ↓

判断条件

 ↓

True ───执行A

 ↓

False ──执行B

 ↓

结束
```


---

# 今日总结


今天学习：

- if条件判断
- if-else结构
- Python缩进规则
- 多条件判断
- and/or逻辑组合


重点：

## 1. if格式

```python
if 条件:
    执行代码
```


## 2. else格式

```python
if 条件:
    A
else:
    B
```


## 3. 条件结果必须是：

```python
True
False
```


## 4. 多条件：

```python
条件1 and 条件2
```

表示：

两个条件都满足


```python
条件1 or 条件2
```

表示：

任意一个满足


## 5. Python通过缩进区分代码块

推荐：

```python
4个空格
```
