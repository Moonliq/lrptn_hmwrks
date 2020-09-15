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

def stu_list(stu):
  names = {}
  for x in stu:
    z = stu.count(x)
    names[x["first_name"]] = z
  namessr = sorted(names, key=names.get, reverse=True)
  return(names[namessr[0]], (sorted(names, key=names.get, reverse=True)[0]))
print(f'Самое частое имя среди учеников: {stu_list(students)[1]}')
print(f'Имя {stu_list(students)[1]} встречаеся {stu_list(students)[0]} раз')
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
for students in enumerate(school_students, start=1):
  group = students[0]
  students = students[1]
  # for x in students:
  #   z = students.count(x)
  #   sps.append(x["first_name"])
  #   names[x["first_name"]] = z
  #   namessr = sorted(names, key=names.get, reverse=True)
  print(f'Самое частое имя среди учеников {group} класса: {stu_list(students)[1]}')

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
for klass in school:
  boy = 0
  girl = 0
  for x in klass['students']:
    clasno = klass['class']
    if is_male[x['first_name']]:
      boy += 1
    else:
      girl += 1
  print(f'В классе {clasno} {girl} девочки и {boy} мальчика')

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
total_dic = []
for klass in school:
  boy = 0
  girl = 0
  for x in klass['students']:
    clasno = klass['class']
    if is_male[x['first_name']]:
      boy += 1
    else:
      girl += 1
  total_dic += [(clasno, boy, girl)]
maxboy = sorted(total_dic, key=lambda student: student[1], reverse=True)
maxgirl = sorted(total_dic, key=lambda student: student[2], reverse=True)
print(f'Больше всего мальчиков в классе {(maxboy[0])[0]}')
print(f'Больше всего девочек в классе {(maxgirl[0])[0]}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a