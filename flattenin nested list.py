def flatten(L):
    for e in L:
        if hasattr(e,'__iter__'):
            yield from flatten(e)
        else:
            yield e

def numberOfElements(L):
    length = 0
    for x in L:
        if hasattr(x,'__iter__'):
            length += numberOfElements(x)
        else:
            length += 1
    return length

L = [1,2,[3,4,[5,6],7],8]

length = numberOfElements(L)
f = flatten(L)

newList = []

for i in range(length):
    newList.append(next(f))

print(newList)

