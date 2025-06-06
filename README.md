# allowdynamic
Dynamic, callable-backed array-like access with optional caching.

## 🔧 Installation

```bash
pip install allowdynamic
````

## 🚀 Example

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

## 📦 Features

- Array-like access to any function (`container[i]`)
- Optional result caching (`cacheMode`)
- Slice support (`container[1:5]`)
- Manual cache control (`isCached`, `updateCache`, `removeFromCache`, etc.)

## 📄 License
MIT License

(c) 2025 DiamondGotCat
