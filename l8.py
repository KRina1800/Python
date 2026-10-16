word = input()
if len(word) < 5:
    print("НЕТ")
else:
    print(word[4])


word = input()
if word.startswith('а'):
    print("ДА")
else:
    print("НЕТ")


word = input()
print(word[-1])


word1 = input()
word2 = input()
if len(word1) > 0 and len(word2) > 0:
    if word1[-1] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")


word = input()
for ch in word:
    print(ch)


message = input()
n = int(input())
if n < 1 or n > len(message):
    print("ОШИБКА")
else:
    print(message[n - 1])


 s = input()
first = True
for ch in s:
    code = ord(ch)
    if not first:
        print(', ', end='')
    print(code, end='')
    first = False
print()


a = input()
while True:
    b = input()
    if b[0] != a[-1]:
        print(b)
        break
    a = b


a = input()
vowels = "аеёиоуыэюя"
b = 0
for ch in a:
    if ch in vowels:
        b += 1
print(b)


shift = int(input())
text = input()
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
n = len(alphabet)
result = ""
for ch in text:
    idx = -1
    for i in range(n):
        if alphabet[i] == ch:
            idx = i
            break
    if idx != -1:
        new_idx = (idx + shift) % n
        result += alphabet[new_idx]
    else:
        result += ch
print(result)


s = input()
print(s[::-1])


s = input()
print(s[:3], s[-3:])


s = input()
if s.startswith('Не') or s.startswith('не'):
    print(s[2:])
else:
    print(s)


s = input()
print(s[::2])


n = int(input())
s = input()
if len(s) > n:
    print(s[:n-3] + '...')
else:
    print(s)


s = input()
if s == s[::-1]:
    print("ДА")
else:
    print("НЕТ")



w1, w2 = input(), input()
b = c = 0
r1, r2 = '', ''
for i in range(len(w1)):
    if w1[i] == w2[i]:
        b += 1
    else:
        r1 += w1[i]
        r2 += w2[i]
t = r2
for ch in r1:
    for j in range(len(t)):
        if t[j] == ch:
            c += 1
            t = t[:j] + t[j+1:]
            break
print("быки:", b)
print("коровы:", c)



s = input()
if not s:
    print(0)
else:
    max_len = 1
    cur_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = 1
    if cur_len > max_len:
        max_len = cur_len
    print(max_len)



n = int(input())
for _ in range(n):
    s = input()
    if s.startswith('####'):
        continue
    elif s.startswith('%%'):
        print(s[2:])
    else:
        print(s)



name = input()
for ch in name:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9') or ch == '_':
        continue
    else:
        print(f"Неверный символ: {ch}")
        break
else:
    print("OK")


