# allowdynamic
Dynamic variables in Python

## Install
```
pip install allowdynamic
```

## import
```
from allowdynamic import DynamicContainer
```

## Example
```
❯ python
>>> def fibonacci(n):
...     if n <= 0:
...         return 0
...     elif n == 1:
...         return 1
...     a, b = 0, 1
...     for _ in range(2, n + 1):
...         a, b = b, a + b
...     return b
... 
>>> from allowdynamic import DynamicContainer
>>> fibonacci_array = DynamicContainer(fibonacci)
>>> for i in range(0, 10):
...     print(f"#{i} in fibonacci_array: {fibonacci_array[i]}")
... 
#0 in fibonacci_array: 0
#1 in fibonacci_array: 1
#2 in fibonacci_array: 1
#3 in fibonacci_array: 2
#4 in fibonacci_array: 3
#5 in fibonacci_array: 5
#6 in fibonacci_array: 8
#7 in fibonacci_array: 13
#8 in fibonacci_array: 21
#9 in fibonacci_array: 34
>>> 
```
