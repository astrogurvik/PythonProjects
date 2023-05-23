# Задача 6.22г
number = int(input('Input natural number:'))
summa = 0

while number > 0:
    digit = number % 10
    if digit > 5:
        summa = summa + digit
    number = number // 10

print(summa)

# Задача 6.22д
number = int(input('Input natural number:'))
mult = 1

while number > 0:
    digit = number % 10
    if digit > 7:
        mult = mult * digit
    number = number // 10

print(mult)

# Задача 6.23а
number = int(input('Enter natural number n:'))
a = int(input('Enter the digit you want to count in the number: '))
cnt = 0

while number > 0:
    digit = number % 10
    if digit == a:
        cnt = cnt + 1
    number = number // 10

print(cnt)

# Задача 6.23в
number = int(input('Enter natural number n:'))
a = int(input('Enter number a from 0 to 8: '))
summa = 0

if 0 <= a <= 8:
    while number > 0:
        digit = number % 10
        if digit > a:
            summa = summa + digit
        number = number // 10
    print(summa)
else:
    print('Error! The number "a" you entered is out of range from 0 to 8, please try again')

# Задача 6.27б
number = int(input('Input natural number:'))
maxDigit = 0
minDigit = 9

while number > 0:
    digit = number % 10
    if digit > maxDigit:
        maxDigit = digit
    if digit < minDigit:
        minDigit = digit
    number = number // 10

dif = maxDigit - minDigit
print('The largest digit of a number is greater than the smallest it\'s digit for', dif)