n = int(input())
m = int(input())
op = input()

if op == '+':
    print(n + m)
elif op == '-':
    print(n - m)
elif op == '*':
    print(n * m)
elif op == '/':
    print(n / m)
else:
    print('Invalid operator')