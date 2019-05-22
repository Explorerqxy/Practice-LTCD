class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.csize = capacity
        self.cache = {}
        self.priority = []  # 要被移除的key = priority[0]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.has_key(key):
            self.priority.append(key)
            self.priority.remove(key)

        return self.cache.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cache.has_key(key):
            self.priority.remove(key)
            self.priority.append(key)

        else:  # 寫入 滿了取代
            if len(self.cache) == self.csize:  # 滿了
                # print(replace)
                self.cache.pop(self.priority[0])
                self.priority.pop(0)

            self.priority.append(key)

        self.cache[key] = value

        return

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)