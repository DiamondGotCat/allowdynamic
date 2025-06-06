[![Upload Python Package](https://github.com/DiamondGotCat/allowdynamic/actions/workflows/python-publish.yml/badge.svg)](https://github.com/DiamondGotCat/allowdynamic/actions/workflows/python-publish.yml)

# allowdynamic
Dynamic, callable-backed array-like access with optional caching.

## 🔧 Installation

```bash
pip install allowdynamic
````

## 🚀 Example

### Array-like Access (int)
```python
from allowdynamic import DynamicContainer

def fibonacci(n):
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

fib = DynamicContainer(fibonacci)

print(fib[10])          # → 55
print(fib[5:10])        # → [5, 8, 13, 21, 34]
print(10 in fib)        # True, if already cached
```

### Dict-like Access (str/other)
```python
from allowdynamic import DynamicContainer

def fibonacci_str(n_str):
    n = int(n_str)
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return str(b)

fib_str = DynamicContainer(fibonacci_str)

print(fib_str["10"])          # → "55"
print("10" in fib_str)        # True, if already cached
```

## 📦 Features

- Dict-like access to any function (`container[key]`)
- Optional result caching (`cacheMode`)
- Slice support (only on int) (`container[1:5]`)
- Manual cache control (`isCached`, `updateCache`, `removeFromCache`, etc.)

## 📄 License
MIT License

(c) 2025 DiamondGotCat
