"""
https://www.1point3acres.com/bbs/thread-782494-1-1.html
有一个八卦大家流传，一开始只有 A 知道，回传知道这个八卦的人的名单
ex input: (“A”, “B”, 100), (“C”, “D”, 200), (“A”, “C”, 300), (“B”, “E”, 500)
(“A”, “B”, 100) 是 A 和 B 在时间 100 的时候见面

第二题是如果每次见面，知道八卦的‍‌‌‌‌‍‍‍‌‍‌‍‍‌‍‍‍‍‍人有 P 的机会跟不知道八卦的人说，每个人知道八卦的机率各是多少?
"""

def gossipList(events):
    events.sort(key=lambda x: x[2])
    names = set()
    for e in events:
        if e[0] not in names:
            names.add(e[0])
        if e[1] not in names:
            names.add(e[1])
    return list(names)
        
