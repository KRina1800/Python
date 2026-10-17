a = [int(input()) for _ in range(int(input()))]
x = a[-1]
fl = False
for i in range(len(a) - 1):
    for j in range(i + 1, len(a) - 1):
        if a[i] * a[j] == x:
            fl = True
            break
    if fl:
        break
print('ДА' if fl else 'НЕТ')


cnt = int(input())
all_pairs = []
good_pairs = []
for _ in range(cnt):
    line = input()
    all_pairs.append(line)
    parts = line.split()
    grade = parts[1]
    if grade in ('4', '5'):
        good_pairs.append(line)
for pair in all_pairs:
    print(pair)
print()
for pair in good_pairs:
    print(pair)


n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
sorted_lines = sorted(lines)
for line in sorted_lines:
    print(line)


n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
sorted_lines = sorted(lines, key=lambda x: (len(x), x))
for line in sorted_lines:
    print(line)


n = int(input())
a, b = 1, 1
for i in range(n):
    if i == 0 or i == 1:
        print(1)
    else:
        c = a + b
        print(c)
        a, b = b, c


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for i in range(n - 1):
    swapped = False
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break
for x in nums:
    print(x)


 n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
unique_nums = set(nums)
print(len(unique_nums))



n = int(input())
for _ in range(n):
    s = input()
    space_index = -1
    for i in range(len(s)):
        if s[i] == ' ':
            space_index = i
            break
    a_str = s[:space_index]
    b_str = s[space_index + 1:]
    a = int(a_str)
    b = int(b_str)
    if a <= b:
        print(a, b)
    else:
        print(b, a)


n = int(input())
people = []
for _ in range(n):
    line = input()
    space_index = -1
    for i in range(len(line)):
        if line[i] == ' ':
            space_index = i
            break
    surname = line[:space_index]
    height = int(line[space_index + 1:])
    people.append((surname, height))
for i in range(n - 1):
    swapped = False
    for j in range(0, n - i - 1):
        if people[j][1] < people[j + 1][1]:
            people[j], people[j + 1] = people[j + 1], people[j]
            swapped = True
    if not swapped:
        break
for surname, height in people:
    print(surname, height)


n = int(input())
strings = []
for _ in range(n):
    strings.append(input())
pairs = []
for s in strings:
    pairs.append((len(s), s))
for p in pairs:
    print(p)
