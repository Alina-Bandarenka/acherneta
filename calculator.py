print("Ведите число")
a = int(input())
print("Ведите число")
b = int(input())
print("Выберете операцию")
print("1 сложение")
print("2 вычитание")
print("3 умнажение")
print("4 деление")
d = int(input())
if d == 1:
    print(a+b)
if d == 2:
    print(a-b)
if d == 3:
    print(a*b)
if d == 4:
    print(a/b)