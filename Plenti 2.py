list1 = set(map(int,input().split()))
list2 = set(map(int,input().split()))
xlists = list1. intersection(list2) # пересечение множеств
print(len(xlists))