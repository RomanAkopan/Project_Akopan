#Создать словарь my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}. Добавьте пару
#'profession': 'Doctor', измените age на 40 и выведите значение city.
my_dict = {
    'name': 'Alice',
    'age': 35,
    'city': 'New-York'
 }
print(my_dict)
if 'proffesion' not in my_dict:
  my_dict['proffession'] = 'Doctor'
print(my_dict)
my_dict['age'] = 40
print(my_dict)
del my_dict['city']
print(my_dict)