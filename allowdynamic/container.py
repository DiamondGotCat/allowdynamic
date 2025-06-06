# allowdynamic
# (c) 2025 DiamondGotCat
# MIT License

from typing import Callable, Dict, Any

class DynamicContainer:
    def __init__(self, action: Callable[[Any], Any], cacheMode: bool = True, sliceLimit: int = 1_000_000):
        self.cache: Dict[Any, Any] = {}
        self.cacheMode = cacheMode
        self.system = {"action": action}
        self.sliceLimit = sliceLimit

    def __getitem__(self, key: Any):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(self.sliceLimit))]
        elif (key in self.cache) and self.cacheMode:
            return self.cache[key]
        else:
            value = self.system["action"](key)
            self.cache[key] = value
            return value

    def __contains__(self, key):
        return (key in self.cache) if self.cacheMode else False
        
    def __repr__(self):
        return f"<DynamicContainer: {len(self.cache)} cached entries (use cache: {'enabled' if self.cacheMode else 'disabled'})>"
    
    def __len__(self):
        return len(self.cache)
    
    def setCacheMode(self, enable: bool = True):
        self.cacheMode = enable
    
    def isCached(self, key):
        return key in self.cache
    
    def updateCache(self, key, value):
        self.cache[key] = value
    
    def removeFromCache(self, key):
        self.cache.pop(key, None)

    def clearCache(self):
        self.cache.clear()

    def newAction(self, action: Callable[[Any], Any]):
        self.system["action"] = action

