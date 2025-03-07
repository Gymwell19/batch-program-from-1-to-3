a, b = map(int, input().split())
if a > b: a, b = b, a
print(list(range(a + 1, b)))