# Day04 Python标识符与变量交换


# 1. 标识符（Identifier）

## 什么是标识符？

标识符是程序员在代码中为：

- 变量
- 函数
- 类
- 其他程序元素

所起的名字。

例如：

```python
age = 18
```

其中：

- age 是变量名
- 18 是变量存储的数据

---

# 2. 标识符命名规则

Python对标识符有明确规定：

## ① 只能包含：

- 英文字母（a-z、A-Z）
- 数字（0-9）
- 下划线（_）


正确：

```python
name
user_name
age2
```

错误：

```python
user-name   # 包含特殊符号
user name   # 包含空格
```


---

## ② 不能以数字开头

正确：

```python
age1 = 20
```

错误：

```python
1age = 20
```


---

## ③ 不能使用Python关键字

Python中有一些保留词，不能作为变量名。

例如：

```python
True
False
None
and
or
if
else
elif
for
while
```

错误：

```python
if = 10
```

但是：

```python
true = 10
```

是合法的。

原因：

Python严格区分大小写。

---

## ④ 区分大小写

以下是三个不同的变量：

```python
age = 10

Age = 20

AGE = 30
```

Python认为它们分别代表不同的数据。


---

# 3. 变量命名规范

虽然Python允许很多写法，但是实际开发推荐：

## ① 见名知意

不推荐：

```python
a = 100
```

推荐：

```python
student_age = 18
```


---

## ② 多个单词使用下划线连接

推荐：

```python
user_name
total_price
```

这种方式叫：

> snake_case（蛇形命名）


---

## ③ 英文字母全部小写

推荐：

```python
user_name
```

不推荐：

```python
UserName
```


---

# 4. 变量值交换


## 普通交换方式

例如：

```python
a = 10
b = 20
```

交换两个变量：

需要借助第三个变量：

```python
c = a

a = b

b = c
```

结果：

```
a = 20
b = 10
```


---

# 5. Python特有交换方式


Python支持直接交换变量：

```python
a,b = 10,20

a,b = b,a
```


完整示例：

```python
a,b = 10,20

print("交换前：a=%d,b=%d"%(a,b))

a,b = b,a

print("交换后：a=%d,b=%d"%(a,b))
```


输出：

```
交换前：a=10,b=20

交换后：a=20,b=10
```


---

# 今日总结

今天学习：

- 标识符的概念
- Python变量命名规则
- Python变量命名规范
- Python大小写敏感特点
- Python变量交换


重点记忆：

1. 变量名只能包含：
   - 字母
   - 数字
   - 下划线

2. 变量不能数字开头

3. 不能使用Python关键字

4. 推荐使用：
   
```python
user_name
```

而不是：

```python
UserName
```

5. Python可以直接交换变量：

```python
a,b = b,a
```