import random


def generate_read():
    listt = []
    n = random.randrange(start=7, stop=15)
    for i in range(n):
        start_a = random.randrange(start=0, stop=20)
        len_a = random.randrange(start=1, stop=40)
        end_a = start_a + len_a
        listt.append((start_a, end_a))
    return listt


data = generate_read()
print(data)
itog = []
while len(data) > 0:
    a1 = min(data, key=lambda a: a[1])
    itog.append(a1)
    data = filter(lambda b: b[0] > a1[1], data)
    data = list(data)
print(itog)
# data[][1]
