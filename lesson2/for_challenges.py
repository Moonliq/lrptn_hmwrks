print('Задание 1')
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for n in names:
    print(n)


print('Задание 2')
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
s = 0
for n in names:
    print(n, len(n) )


print('Задание 3')
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for n in names:
    if is_male[n]:
        print(f'{n} мужик')
    else:
            print(f'{n} не мужик')

print('Задание 4')
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
grsum = 0
stud = 0
for n in groups:
    grsum += 1
    stud = len(n)
    print(f'В группе №{grsum} {stud} студентов')
print(f'Всего групп {grsum}')
       

print('Задание 5')
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
grsum = 0
for n in groups:
    grsum += 1
    print(f'В группе №{grsum}: {", ".join(n)}')