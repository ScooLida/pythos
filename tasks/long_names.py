# Входные данные
# В первой строке содержится целое число n (1≤n≤100). В каждой из последующих n строк содержится по одному слову. Все слова состоят из малых латинских букв и имеют длину от 1 до 100 символов.
#
# Выходные данные
# Выведите n строк. В i строке должен находиться результат замены i-го слова из входных данных.

chlen = []
while True:
    x = input()
    if x:
        chlen.append(x)
    else:
        break
for i in chlen:
    if len(i) < 9:
        print(i)
    else:
       print(f'{i[0]}{len(i)-2}{i[len(i)-1]}')
