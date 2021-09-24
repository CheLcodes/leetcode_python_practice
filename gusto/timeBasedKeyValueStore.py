import collections
class TimeMap:
    def __init__(self):
        self.dic = collections.defaultdict(list)
    
    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        lst = self.dic[key]
        l, r = 0, len(lst)  - 1
        while l <= r:
            mid = l + (r - l) // 2
            if lst[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return '' if r == -1 else lst[r][1]

tm = TimeMap()
tm.set('foo', 'bar', 1)
print(tm.get('foo', 1))
tm.get('foo', 3)
tm.set('foo', 'bar2', 4)
print(tm.get('foo', 4))
print(tm.get('foo', 5))

