def dotInIntervals(intervals, dots):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()

    res = []
    curr = 0
    i, j = 0, 0

    while i < len(events) - 1:
        print('i', i)
        print('j', j)
        print('res', res)
        if events[i][1] == 1:
           curr += 1
        elif events[i][1] == -1:
            curr -= 1
        
        if j < len(dots) and events[i][0] <= dots[j] < events[i+1][0]:
                res.append(curr)
                i += 1
                j += 1
        else:
            i += 1
    if len(dots) > j:
        res += ([curr] * (len(dots) - j))

    return res

res = dotInIntervals([[1,5],[3,7],[9,15],[10,13]], [2,3,6,8,10,15])
print(res)



        
