# Day03 Python变量与数据类型

## 1. 字面量（Literal）

字面量指的是代码中直接写出的固定值。

Python常见字面量类型：

| 类型 | 示例 | 说明 |
| ---- | ---- | ---- |
| 整数(int) | 100 | 不带小数的数字 |
| 浮点数(float) | 3.14 | 带小数的数字 |
| 布尔值(bool) | True / False | 表示真假 |
| 字符串(str) | "Test" | 文本内容 |
| 空值(NoneType) | None | 表示没有值 |

示例：

```python
print(100)       # 整数
print(3.14)      # 浮点数
print(True)      # 布尔值
print(False)     # 布尔值
print("Test")    # 字符串
print(None)      # 空值
```

---

# 2. 布尔值参与运算

Python中的布尔值可以参与数学运算：

```python
print(True + 1)
print(False - 1)
```

运行结果：

```
2
-1
```

原因：

```text
True = 1
False = 0
```

所以：

```python
True + 1
等价于：
1 + 1
```

---

# 3. 变量（Variable）

变量可以理解为：

> 用一个名字保存数据，之后可以通过名字访问数据。

Python变量定义：

```python
变量名 = 数据
```

例如：

```python
a = 100

print(a)
```

输出：

```
100
```

---

# 4. 查看变量类型

Python提供：

```python
type()
```

查看变量的数据类型。

示例：

```python
a = 100

print(type(a))
```

输出：

```
<class 'int'>
```

---

# 5. Python动态类型语言

Python属于：

> 动态类型语言

意思是：

变量创建时不需要提前声明类型。

例如：

```python
a = 100
print(type(a))

a = 152.54
print(type(a))
```

同一个变量：

第一次：

```
int
```

第二次：

```
float
```

类型可以改变。

---

## 注意：

虽然Python允许改变变量类型：

```python
a = 100
a = "Hello"
```

但是实际项目开发中：

> 推荐一个变量尽量只保存一种类型的数据。

这样代码更容易维护。

---

# 6. 变量参与计算

变量可以直接参与数学运算。

示例：

```python
base = 20.7
incr = 50

print("计算数据的值为：", base + incr)

print("进一步计算数据的值为：", base + incr * 2)
```

运行结果：

```
计算数据的值为：70.7

进一步计算数据的值为：120.7
```

---

# 7. 多个变量同时赋值

Python支持一次给多个变量赋值：

```python
base, incr = 20.7, 50
```

等价于：

```python
base = 20.7
incr = 50
```

这种写法更加简洁。

---

# 本日总结

今天学习：

- Python基本数据类型
    - int
    - float
    - bool
    - str
    - None

- 字面量概念

- 变量定义和使用

- type()查看变量类型

- Python动态类型特点

- 多变量同时赋值

重点：

1. Python变量不需要声明类型
2. True等价于1，False等价于0
3. type()可以查看数据类型
4. 实际开发中建议变量类型保持稳定