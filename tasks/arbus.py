# Входные данные
# В первой и единственной строке входных данных записано целое число w (1≤w≤100) — вес купленного ребятами арбуза.
#
# Выходные данные
# Выведите YES, если ребята смогут поделить арбуз на две части, каждая из которых весит четное число килограмм, и NO в противном случае.

ves = int(input())
if ves % 2 == 1 or ves == 2 :
    print("NO")
elif (ves - 2) % 2 == 1:
    print("NO")
else:
    print("YES")

