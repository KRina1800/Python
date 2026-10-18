text = input()
words = text.split()
third_words = words[2::3]
print(' '.join(third_words))


x = input().split()
for s in x:
    n = int(s)
    print('*' * n)


n = int(input())
squares = [x ** 2 for x in range(n + 1)]
print(' '.join(str(x) for x in squares))


nums = list(map(int, input().split()))
result = [x ** 2 for x in nums if x % 2 != 0 and (x ** 2) % 10 != 9]
print(*result)


words = input().split()
result = '["' + '", "'.join(words) + '"]'
print(result)


n = int(input())
lines = []
for _ in range(n):
    line = input()
    if 'лук' not in line:
        lines.append(line)
print(', '.join(lines))


print(*input().split(), sep='\n')


from urllib.parse import urlparse, parse_qs
url = input()
parsed = urlparse(url)
params = parse_qs(parsed.query)
q_value = params.get('q', [None])[0]
print(q_value)
