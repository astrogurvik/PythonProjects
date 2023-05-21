# Задача 4.72(а)
n1 = int(input('Введите число n1:\n'))
n2 = int(input('Введите число n2:\n'))
n3 = int(input('Введите число n3:\n'))

print('Вы ввели числа: ', str(n1), str(n2), str(n3))

if n1 > n2 and n1 > n3:
    print('первое - наибольшее число')
elif n2 > n1 and n2 > n3:
    print('второе - наибольшее число')
elif n3 > n1 and n3 > n2:
    print('третье - наибольшее число')
elif n1 == n2 and n1 != n3 and n2 != n3:
    print('Нет наибольшего числа.', "Числа n1 и n2 - равны")
elif n2 == n3 and n2 != n1 and n3 != n1:
    print('Нет наибольшего числа.', "Числа n2 и n3 - равны")
elif n1 == n3 and n1 != n2 and n3 != n2:
    print('Нет наибольшего числа.', "Числа n1 и n3 - равны")
else:
    print('Нет наибольшего числа. Все числа равны')

# Задача 4.72(б)
n1 = int(input('Введите число n1:\n'))
n2 = int(input('Введите число n2:\n'))
n3 = int(input('Введите число n3:\n'))

print('Вы ввели числа: ', str(n1), str(n2), str(n3))

if n1 < n2 and n1 < n3:
    print('первое - наименьшее число')
elif n2 < n1 and n2 < n3:
    print('второе - наименьшее число')
elif n3 < n1 and n3 < n2:
    print('третье - наименьшее число')
elif n1 == n2 and n1 != n3 and n2 != n3:
    print('Нет наименьшего числа.', "Числа n1 и n2 - равны")
elif n2 == n3 and n2 != n1 and n3 != n1:
    print('Нет наименьшего числа.', "Числа n2 и n3 - равны")
elif n1 == n3 and n1 != n2 and n3 != n2:
    print('Нет наименьшего числа.', "Числа n1 и n3 - равны")
else:
    print('Нет наименьшего числа. Все числа равны')

# Задача 4.76
n1 = int(input('Введите число n1:\n'))
n2 = int(input('Введите число n2:\n'))

print('Вы ввели числа: ', str(n1), str(n2))

if abs(n1) > abs(n2):
    result = n1 / 2
    print(result)

# Задача 4.78
n1 = int(input('Введите число n1:\n'))
n2 = int(input('Введите число n2:\n'))
n3 = int(input('Введите число n3:\n'))

print('Вы ввели числа: ', str(n1), str(n2), str(n3))

if n1 % 2 == 0:
    print(n1)
if n2 % 2 == 0:
    print(n2)
if n3 % 2 == 0:
    print(n3)

# Задача 4.83
n1 = float(input('Введите число n1:\n'))
n2 = float(input('Введите число n2:\n'))
n3 = float(input('Введите число n3:\n'))
n4 = float(input('Введите число n4:\n'))

print('Вы ввели числа: ', str(n1), str(n2), str(n3), str(n4))

result = 0
if n1 > 5:
    result = result + n1
if n2 > 5:
    result = result + n2
if n3 > 5:
    result = result + n3
if n4 > 5:
    result = result + n4
print(result)

# Задача 4.84
n1 = int(input('Введите целое число n1:\n'))
n2 = int(input('Введите целое число n2:\n'))
n3 = int(input('Введите целое число n3:\n'))
n4 = int(input('Введите целое число n4:\n'))

print('Вы ввели числа: ', str(n1), str(n2), str(n3), str(n4))

result = 0
if n1 % 3 == 0:
    result = result + n1
if n2 % 3 == 0:
    result = result + n2
if n3 % 3 == 0:
    result = result + n3
if n4 % 3 == 0:
    result = result + n4
print(result)

print('Hello, world!')