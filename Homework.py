#Задача 1. Найдите сумму цифр трехзначного числа

# number = int(input("Введите трехзначное число: "))
# n = number
# if  99 < number < 1000:     
#     sum = number % 10
#     sum = sum + number//100
#     number = number//10
#     sum = sum + number % 10
#     print(f"Сумма цифр числа {n} равняется {sum}")
# else:
#     print("Вы ввели не трехзначное число, повторите пожалуйста ввод!")


# Задача 2. Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# sum = int(input('Введите общее количество журавликов, которые сделали ребята: '))

# if sum % 6 == 0:
#     p = sum  // 6
#     s = sum // 6
#     k = (sum // 6)*4
#     print(f'Петя сделал {p} журавликов, Сережа сделал {s} журавликов, Катя сделала {k} журавликов.')

# Задача 3. Написать программу, которая проверяет счастливость билета. Счастливым билетом называют 
# такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

number = int(input("Введите номер Вашего билета: "))
if 99999 < number < 1000000:
    s1 = number % 10
    number = number//10
    s1 += number % 10
    number = number//10
    s1 += number % 10
    number = number//10
    s2 = number % 10
    number = number//10
    s2 += number % 10
    s2 += number//10
    if s1 == s2:
        print("Ваш билет оказался счастливым!")
    else:
        print("Ваш билет оказался обычным")
else:
    print("Некорректно введен номер билета, пожалуйста повторите ввод!")

