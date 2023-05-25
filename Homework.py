#Задача 1. Найдите сумму цифр трехзначного числа

number = int(input("Введите трехзначное число: "))
n = number
if  99 < number < 1000:     
    sum = number % 10
    sum = sum + number//100
    number = number//10
    sum = sum + number % 10
    print(f"Сумма цифр числа {n} равняется {sum}")
else:
    print("Вы ввели не трехзначное число, повторите пожалуйста ввод!")

    
