#Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа, расположенные между A и B (включая сами числа A и B), а также количество
a = input("Введите число а:")
b = input("Введите число b:")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильный ввод")
        a = input("Введите число а:")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильный ввод")
        b = input("Введите число b:")
if a > b:
    print("Число a должно быть меньше b")
for i in range(a, b + 1):
    print(i)