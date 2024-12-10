import sympy as sp

x = sp.symbols('x')
function=input("Введите функцию:")
# наша функция=  x/((1-x^2)^3)
nomer = int(input("Введите номер производной: "))
f = sp.sympify(function) #парсим
derivative = sp.diff(f, x, nomer) #н-я производная
value = derivative.subs(x, 0) #значение производной в x=0

factorial=1
for i in range(2,nomer+1):
    factorial*=i
result=value/factorial
print(f"коэффициент равен: {result}")

