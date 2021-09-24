# https://www.1point3acres.com/bbs/thread-786869-1-1.html
from typing import Dict, List

def findLowestRank(employee1, employee2, rank, report) -> str:
    manager_lst1 = []
    manager_lst2 = []
    
    for e in report[employee1]:
        manager_lst1.append((e, rank[e]))
    
    manager_lst1.sort(key=lambda x: x[1])
    for e in report[employee2]:
        manager_lst2.append((e, rank[e]))
    manager_lst2.sort(key=lambda x: x[1])

    i, j = 0, 0
    while i < len(manager_lst1) and j < len(manager_lst2):
        if manager_lst1[i][0] < manager_lst2[j][0]:
            i += 1
        elif manager_lst1[i][0] > manager_lst1[j][0]:
            j += 1
        else:
            return manager_lst1[i][0]
    return -1

rank = {'A': 4, 'B': 3, 'E': 3, 'D': 2}
report = {'A': [], 'B': ['A'], 'E': ['B'], 'D': ['B', 'A']}
res = findLowestRank('D', 'E', rank, report)
print(res)