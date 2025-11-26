#Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка.
x = input("Координата x: ")
y = input("Координата y: ")
while type(x) != int:
  try:
    x = int(x)
  except ValueError:
    print("неправильно введено")
    x = input("Координата x: ")
while type(y) != int:
  try:
    y = int(y)
  except ValueError:
    print("неправильно введено")
    y = input("Координата Y: ")
if x > 0 and y > 0:
  print("1 четверть")
elif x < 0 and y > 0:
  print("2 четверть")
elif x < 0 and y < 0:
  print("3 четверть")
elif x > 0 and y < 0:
  print("4 четверть")