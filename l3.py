a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Итого в сумме:")
print(a + b)


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Итого в сумме:")
print(a + b)


word = input("Введите слово: ")
length = len(word)
print("Слово", word, "имеет длину", length)


number = float(input(("Введите  число: ")))
if number > 0:
    print('+')
elif number < 0:
    print('-')
else:
    print('0')


days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
minutes_in_year = days_per_year * hours_per_day * minutes_per_hour
print(minutes_in_year)


sms_text = input("Введите текст SMS: ")
total = len(sms_text) * 40
rubles = total // 100
kopecks = total % 100
print(rubles, "р.", kopecks, "коп.")


a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
a, b = b, a
print(a)
print(b)


number = float(input("Введите число: "))
print(abs(number))


a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
integer_part = a // b
remainder = a % b
print(integer_part)
print(remainder)


a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
operation = input("Введите операцию (+, -, *, /): ")
if operation == "+":
    result = a + b
    print(result)
elif operation == "-":
    result = a - b
    print(result)
elif operation == "*":
    result = a * b
    print(result)
elif operation == "/":
    if b == 0:
        print("ОШИБКА")
    else:
        result = a / b
        print(result)
else:
    print("ОШИБКА")
