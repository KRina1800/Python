n = int(input(("Введите количество строк: ")))
unique_words = set()
for _ in range(n):
    word = input(("Введите текст: ")).strip()
    unique_words.add(word)
print(len(unique_words))


n = int(input(("Введите количество строк: ")))
cities = set()
for _ in range(n):
    cities.add(input("Введите город: ").strip().lower())
new_city = input("Введите новый город: ").strip().lower()
if new_city in cities:
    print("TRY ANOTHER")
else:
    print("OK")


s1 = set()
while True:
    line = input(("Введите числа первого списка: ")).strip()
    if not line: break
    for x in line.split(): s1.add(int(x))
s2 = set()
while True:
    line = input(("Введите числа второго списка: ")).strip()
    if not line: break
    for x in line.split(): s2.add(int(x))
c = s1 & s2
if c:
    first = True
    for num in c:
        if not first:
            print(' ', end='')
        print(num, end='')
        first = False
    print()
else:
    print("EMPTY")



english_n = int(input())
german_n = int(input())
english = set()
german = set()
for _ in range(english_n):
    surname = input()
    english.add(surname)
for _ in range(german_n):
    surname = input()
    german.add(surname)
one_language = english ^ german
if not one_language:
    print('NO')
else:
    print(len(one_language))


m = int(input())
library = set()
for _ in range(m):
    book = input()
    library.add(book)
n = int(input())
for _ in range(n):
    book = input()
    if book in library:
        print("YES")
    else:
        print("NO")



m = int(input())
k = int(input())
present_all = set()
for _ in range(k):
    present_all.add(input())
for _ in range(m - 1):
    k = int(input())
    current_day = set()
    for _ in range(k):
        current_day.add(input())
    present_all &= current_day
for surname in present_all:
    print(surname)



n = int(input())
employee = {}
for _ in range(n):
    surname = input()
    if surname in employee:
        employee[surname] += 1
    else:
        employee[surname] = 1
result = 0
for surname in employee:
    if employee[surname] > 1:
        result += employee[surname]
print(result)



m = int(input())
fridge = set()
for _ in range(m):
    fridge.add(input().strip())
n = int(input())
for _ in range(n):
    parts = input().split()
    recipe_name = parts[0]
    ingredients = set(parts[1:])
    if ingredients <= fridge:
        print(recipe_name)


m = int(input())
available = set()
for _ in range(m):
    available.add(input().strip())
n = int(input())
cooked = set()
for _ in range(n):
    dishes = input().split()
    for dish in dishes:
        cooked.add(dish)
not_cooked = available - cooked
for dish in not_cooked:
    print(dish)



set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

sym_diff = set1 ^ set2

if not sym_diff:
    print("EMPTY")
else:
    first = True
    for num in sym_diff:
        if not first:
            print(' ', end='')
        print(num, end='')
        first = False
    print()


