# Входные данные
# В первой строке входных данных записано единственное целое число n (1≤n≤1000) — количество задач на соревновании. Далее в n строках записано по три целых числа, каждое из которых равно 0 или 1. Если первое число в строке равно 1, то Петя уверен в решении этой задачи, в противном случае он не уверен в решении. Второе число обозначает мнение Васи, а третье — мнение Тони. Числа в строках разделены пробелами.
#
# Выходные данные
# Выведите единственное целое число — количество задач, которые друзья будут реализовывать на соревновании.
a = 0
jopa = 0
answ = 0
n = int(input())
for i in range(n):
    i = input()
    i2 = i.split(' ')
    for p in i2:
        a += int(p)
    if a > 1:
        jopa += 1
    a=0

print(jopa)
