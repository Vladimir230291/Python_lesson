# Простой консольный калькулятор
a = float(input("Введите первое число: "))
b = float(input("Введите второe число: "))
c = 0
print("Что будем делать?: (+, -, /, *, mod, pow, div)")
oper = str(input())
if oper == "+":
    c = a + b
elif oper == "-":
    c = a - b
elif oper == "/":
    if b != 0:
        c = a / b
    else:
        print("деление на 0!")
elif oper == "*":
    c = a * b
elif oper == "mod":
    if b != 0:
        c = a % b
    else:
        print("деление на 0!")
elif oper == "pow":
    c = pow(a, b)
elif oper == "div":
    if b != 0:
        c = a // b
    else:
        print("Деление на 0")
else:
    print("Введите корректную операцию")
print(c)
