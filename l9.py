n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
print(*lines)


n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
query = input()
for line in lines:
    if query in line:
        print(line)


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
result = []
for i in range(n - 1):
    result.append(nums[i] + nums[i + 1])
print(*result)


n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
print(*lines[::-1])


n = int(input())
result = []
for _ in range(n):
    num = int(input())
    result.append(num * 3)
print(*result)


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
p = int(input())
q = int(input())
total = 0
for i in range(p, q + 1):
    total += nums[i]
print(total)


n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
word1 = input()
word2 = input()
for line in lines:
    if word1 in line and word2 in line:
        print(line)


n = int(input())
soups = ['щи', 'борщ', 'щавелевый', 'овсяный', 'по-чабански']
for i in range(n):
    print(soups[i % 5])


white_list = []
while True:
    line = input()
    if line == "":
        break
    white_list.append(line)
while True:
    query = input()
    if query == "":
        break
    found = False
    for item in white_list:
        if item == query:
            found = True
            break
    if found:
        print(query)


n = int(input())
word = [''] * n
for _ in range(n):
    s = input()
    space_index = -1
    for i in range(len(s)):
        if s[i] == ' ':
            space_index = i
            break
    pos = int(s[:space_index])
    letter = s[space_index + 1]
    word[pos - 1] = letter
for ch in word:
    print(ch, end='')
print()
