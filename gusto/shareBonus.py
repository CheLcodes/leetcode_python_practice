"""
给你amount 和 一个map， 《雇员，应付工资》
让你return 一个map 里面是雇员和应收工资
比如 4 USD
给 2个人
anna 2
matt 1
kevin 5
尽量平均分配 多的按 字母顺序给
return
anna 2
‍‌‌‌‌‍‍‍‌‍‌‍‍‌‍‍‍‍‍matt 1
kevin 1

因为尽量平均分配，按照anna, xx kevin的顺序每人发1个，直到available salary用完
"""

class Solution:
    def shareBonus(self, amount: int, bonus_dic: dict):
        res = bonus_dic.copy()
        self.helper(amount, bonus_dic)
        for k,v in bonus_dic.items():
            res[k] -= v
        return res

    def helper(self, amount, bonus_dic):
        cnt = len(bonus_dic.keys())
        for k, v in bonus_dic.items():
            if v == 0:
                cnt -= 1
        div, mod = divmod(amount, cnt)
        if div == 0 and mod:
            keys = []
            for k, v in bonus_dic.items():
                if v != 0:
                    keys.append(k)
            keys.sort()
            i = 0
            while mod:
                bonus_dic[keys[i]] -= 1
                i += 1
                mod -= 1
            return
        amount = mod
        for k, v in bonus_dic.items():
            if v > div:
                bonus_dic[k] -= div
            elif v > 0:
                amount += (div - v)
                bonus_dic[k] = 0
        if amount:
            self.helper(amount, bonus_dic)

        
sol = Solution()
res = sol.shareBonus(1011, {'C': 100, 'A': 150, 'B': 200, 'E': 500, 'D': 600})                
print(res)







        
            


