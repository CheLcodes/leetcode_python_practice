class KVStore:
    def __init__(self):
        self.stack = [{}] # hold all the transactions
        self.dic = {} # hold all the k, v pairs
    
    def set(self, key, value):
        # O(1)
        # update the top element
        self.stack[-1][key] = value
        self.dic[key] = value
        
    def get(self, key):
        # O(n_transctions)
        if key in self.dic: 
            return self.dic[key]
        else:
            print(f"{key} not set")

        # for i in range(len(self.stack)-1, -1, -1):
        #     if key in self.stack[i]:
        #         return self.stack[i][key]
    
    def count(self, val):
        cnt = 0
        for k, v in self.dic.items():
            if v == val:
                cnt += 1
        return cnt
    
    def begin(self):
        # O(1)
        # add an empty element to the stack
        self.stack.append({})
    
    def commit(self):
        # O(n_keys)
        if len(self.stack) == 1 and self.stack[0] == {}:
            print("NO TRANSACTION")
            return
        last_trans = self.stack.pop()
        for k, v in last_trans.items():
            self.stack[-1][k] = v

    def delete(self, key):
        # O(n_transactions)
        if key in self.dic:
            for i in range(len(self.stack)-1, -1, -1):
                if key in self.stack[i]:
                    del self.stack[i][key]
                    break
            del self.dic[key]
        else:
            print(f"{key} not set")

    def rollback(self):
        # O(1)
        if len(self.stack) == 1 and self.stack[0] == {}:
            print("NO TRANSACTION")
            return
        self.stack.pop()
        self.update_dic()
    
    def update_dic(self):
        for i in range(len(self.stack)):
            for k, v in self.stack[i].items():
                self.dic[k] = v


def test_KVStore():
    kv = KVStore()
    kv.set(1, 3)

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_single_transaction():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4


def test_KVStore_rollback():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) is None

def test_KVStore_no_transaction():
    kv = KVStore()
    kv.begin()
    kv.commit()


def test_KVStore_multiple_begin():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)

    kv.begin()
    kv.set(3, 5)

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) == None
    assert kv.get(3) == None


test_KVStore_no_transaction()