n = int(input("Введите число:"))
found = False
for _ in range(n):
    line = input(("Введите текст:"))
    if 'кот' in line or 'Кот' in line:
        found = True
if found:
    print('МЯУ')
else:
    print('НЕТ')


n = int(input("Введите число:"))
found = False
for _ in range(n):
    line = input(("Введите текст:"))
    if 'кот' in line or 'Кот' in line:
        found = True
        break
if found:
    print('МЯУ')
else:
    print('НЕТ')


line_number = 0
result = -1
while True:
    line = input((("Введите текст:")))
    line_number += 1
    if 'стоп' in line or 'СТОП' in line:
        break
    if 'кот' in line or 'Кот' in line:
        if result == -1:
            result = line_number
print(result)


line_number = 0
result  = -1
num = 0
while True:
    line = input(("Введите текст:"))
    line_number += 1
    if 'стоп' in line or 'СТОП' in line:
        break
    if 'кот' in line or 'Кот' in line:
        num += 1
        if result  == -1:
            result  = line_number
print(num)
print(result )


a = int(input())
b = int(input())
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    else:
        print(i, end=' ')
print()


summa = 0
x = 0
the_first_ten = -1
while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
    summa += n
    x += 1
    if summa == 10 and the_first_ten == -1:
        the_first_ten = x
print(the_first_ten)



n = int(input("Введите количество строк: "))
for _ in range(n):
    line = input("Введите текст: ")
    if "плохо" in line:
        continue
    print(line)


while True:
    line = input(("Введите текст: "))
    if line == "СТОП":
        break
    if "пёс" in line.lower():
        found_cat = False
    elif "кот" in line.lower():
        found_cat = True
if found_cat:
    print("МЯУ")
else:
    print("НЕТ")


n = int(input(("Введите количество строк: ")))
total = 0
for _ in range(n):
    num = int(input("Введите число: "))
    if num <= 0:
        continue
    total += num
print(total)


a = 0
b = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        if a <= 100:
            print("ОК")
        else:
            print("СТОП")
        break
    a += num
    b += 1
    if a > 100:
        print("СТОП")
        print(b)
        break


