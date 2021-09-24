# /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
# * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
# * evicting the T with lowest rank among the ones that it has available
# * If there is a tie, the cache may choose any T with lowest rank to evict.
# */

import heapq

class rankableNode:
    def __init__(self, val):
        self.val = val
    
    def getRank(self, val):
        return val

class PQNode:
    def __init__(self, key, val):
        self.key = key
        self.val = rankableNode(val)

    def __lt__(self, other):
        return self.val.getRank() < other.getRank()

class ReatainBestCache:
    def __init__(self, ds, entriesToRetain):
        self.dic = {}   # {key: val}
        self.size = entriesToRetain
        self.heap = []  # (key, val)
        self.ds = ds
    
    def get(self, key):
        if key in self.dic:
            return self.dic[key]
        
        val = self.ds[key]
        if len(self.dic) < self.size:
            self.dic[key] = val
            heapq.heappush(self.heap, PQNode(key, val))
        else:
            head = self.heap[0]
            if head.getRank() < val.getRank():
                heapq.heappop(self.heap)
                del self.dic[key]
                heapq.heappush(self.heap, PQNode(key, val))
        return val

# public class RetainBestCache<K, T extends Rankable> {
# int entriesToRetain;
# HashMap<K, T> map = new HashMap<K,T>();
# DataSource<K,T> ds;


#  
# /* Constructor with a data source (assumed to be slow) and a cache size */
# public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
# //impliment here
# }



# public T get(K key) {
# //impliment here
# }
# /*
# * For reference, here are the Rankable and DataSource interfaces.
# * You do not need to implement them, and should not make assumptions
# * about their implementations.
# */
# public interface Rankable {
# /**
# * Returns the Rank of this object, using some algorithm and potentially
# * the internal state‍‌‌‌‌‍‍‍‌‍‌‍‍‌‍‍‍‍‍ of the Rankable.
# */
# long getRank();
# }
# public interface DataSource<K, T extends Rankable> {
# T get(K key);
# }