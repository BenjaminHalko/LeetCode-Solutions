class MyHashMap:

    def __init__(self):
        self.keys = []
        self.data = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.data[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.data.append(value)

    def get(self, key: int) -> int:
        return self.data[self.keys.index(key)] if key in self.keys else -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            del self.data[self.keys.index(key)]
            self.keys.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)