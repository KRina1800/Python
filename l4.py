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
