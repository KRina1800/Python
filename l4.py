n = int(input("Введите число: "))
x = n
while x >= 1:
    print(x)
    x = x - 1


num = int(input())
while num != 0:
    print(num, end=' ')
    num = int(input())


line = input()
while line != "":
    print(line)
    line = input()


temp = float(input("Введите температуру: "))
while temp != 0:
    if temp > 28:
        print("ЖАРКО")
    elif temp < 15.5:
        print("ХОЛОДНО")
    else:
        print("НОРМАЛЬНО")
    temp = float(input("Введите температуру: "))


password = input("Введите пароль: ")
password2 = input("Повторите пароль: ")
if len(password) < 8:
    print("Слишком короткий!")
elif password != password2:
    print("Пароли не совпадают!")
else:
    print("OK")


password = ""
while len(password) < 8 or password != password2 or "123" in password:
    password = input("Введите пароль: ")
    password2 = input("Повторите пароль: ")
    if len(password) < 8:
        print("Слишком короткий! Пароль должен быть не менее 8 символов.")
    elif password != password2:
        print("Пароли не совпадают! Пожалуйста, введите пароль еще раз.")
    elif "123" in password:
        print('Пароль не должен содержать "123"! Пожалуйста, введите другой пароль.')
print("OK")


total_sum = 0
number = -1
while number != 0:
    number = int(input("Введите число (0 для завершения): "))
    total_sum += number
print("Итоговая сумма:", total_sum)


n = int(input("Введите целое число: "))
if n == 0:
    print("Количество цифр: 1")
else:
    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print("Количество цифр:", count)


n = int(input("Введите целое число: "))
n = abs(n)
sum = 0
while n > 0:
    last = n % 10
    sum += last
    n //= 10
print("Сумма цифр:", sum)


secret = 18
guess = -1
while guess != secret:
    guess = int(input("Введите ваше число: "))
    if guess < secret:
        print("БОЛЬШЕ")
    elif guess > secret:
        print("МЕНЬШЕ")
print("УГАДАЛ!")

