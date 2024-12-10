def factorial(x):
    result=1
    for i in range(1,x+1):
        result=result*i
    return result

#коэффициент производящей функции при нечетных степенях  
def coefficient(x):
    k=x//2
    return factorial (k+2)/(factorial(k)*factorial(2))
    
print("Введите общее кол-во цветов:")
n=int(input())
if (n%2==0):
    print("Введенное n - четное. Необходимо нечетное")
else:
    print(f"Количество всевозможных букетов с условием чет/нечет: {int(coefficient(n))}")