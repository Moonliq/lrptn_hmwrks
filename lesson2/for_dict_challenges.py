print('Задание 1')
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???
z = 0
sps = []
for x in students:
    z = students.count(x)
    if x["first_name"] in sps:
        continue
    else:
        sps.append(x["first_name"])
    print(f'{x["first_name"]}: {z}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


print('Задание 2')
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
#
z = 0
sps = []
names = {}
for x in students:
    z = students.count(x)
    sps.append(x["first_name"])
    names[x["first_name"]] = z
namessr = sorted(names, key=names.get, reverse=True)
print(f'Самое частое имя среди учеников: {namessr[0]}')
print(f'Имя {namessr[0]} встречаеся {names[namessr[0]]} раз')
# Очень страшно реализовал, наверное, но я чет не нашел очевидного счетчика для словарика. И чтобы он тупо расставил по значениям/

# Пример вывода:
# Самое частое имя среди учеников: Маша

print('Задание 3')
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
z = 0
group = 0
for students in school_students:
  group += 1
  sps = []
  names = {}
  for x in students:
    z = students.count(x)
    sps.append(x["first_name"])
    names[x["first_name"]] = z
    namessr = sorted(names, key=names.get, reverse=True)
  print(f'Самое частое имя среди учеников {group} класса: {namessr[0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


print('Задание 4')
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
# newdic = {}
# for klass in school:
#   print(klass)
#   newdic = {}
#   for k, v in klass.items():




# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


print('Задание 5')
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a