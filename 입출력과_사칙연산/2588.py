a = input()
b = input()

a = int(a)
b = int(b)

x = (b % 10)
y = (b % 100) - (b % 10)
z = (b // 100)

print(a * x)
print(int(a * y / 10))
print(a * z)
print(a * b)
