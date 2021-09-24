def sameSetCards(card1, card2, card3):
    for i in range(4):
        if not checkVals(card1[i], card2[i], card3[i]):
            return False
    return True

def checkVals(a, b, c):
    tmp = set()
    tmp.add(a)
    tmp.add(b)
    tmp.add(c)
    if len(tmp) == 1 or len(tmp) == 3:
        return True
    return False

# follow-up: 
# what if there are m cards with n attributes 
# where each attribute has k potential ‍‌‌‌‌‍‍‍‌‍‌‍‍‌‍‍‍‍‍values

print(sameSetCards((2, 0, 1, 2), (1, 1, 0, 1), (0, 1, 2, 0)))
