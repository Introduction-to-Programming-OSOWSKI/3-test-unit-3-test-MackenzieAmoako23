def countB(w):
    count = 0
    for i in range(0, len(w)):
        if w[i] == "b":
            count = count + 1

    return count

def removeLast(w):
    remove = ""
    for i in range(0, len(w) - 1):
        remove = remove + w[i]
    return remove

def sumBetweenOdd(x, y):
    Villager = 0
    for i in range(x + 1, y):
        if   i % 2 == 1:
            Villager = Villager + i 
    return Villager

def firstLast(w):
    if w[0] == w[len(w) - 1]:
        return True
    else:
        return False
