# allowdynamic
# (c) 2025 DiamondGotCat
# MIT License

from typing import Callable, Dict, Any

class DynamicContainer:
    def __init__(self, action: Callable[[Any], Any]):
        self.cache: Dict[Any, Any] = {}
        self.system = {"action": action}

    def __getitem__(self, key: Any):
        if key in self.cache:
            return self.cache[key]
        else:
            value = self.system["action"](key)
            self.cache[key] = value
            return value

    def __contains__(self, key):
        return key in self.cache

    def newAction(self, action: Callable[[Any], Any]):
        self.system["action"] = action

    def clearCache(self):
        self.cache.clear()
