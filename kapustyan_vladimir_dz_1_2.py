numbers_list = []
i=int(0)
while i <= 1000:
    if i % 2 != 0:
        numbers_list.append(i**3)
    i += 1
print(numbers_list)
sum = int(0)
n = int(0)
while n < len(numbers_list):
    if (numbers_list[n]//1000000000%10 + numbers_list[n]//100000000%10 + numbers_list[n]//10000000%10 + numbers_list[n]//1000000%10 + numbers_list[n]//100000%10 + numbers_list[n]//10000%10 + numbers_list[n]//1000%10 + numbers_list[n]//100%10 + numbers_list[n]//10%10 + numbers_list[n]%10)%7==0:
        sum = sum + numbers_list[n]
    n += 1
print(sum, 'сумма чисел из списка, сумма цифр которых делится на 7')
n = 0
sum_after_added_17 = int(0)
while n < len(numbers_list):
    numbers_list[n]=numbers_list[n]+17
    if (numbers_list[n] // 1000000000 % 10 + numbers_list[n] // 100000000 % 10 + numbers_list[n] // 10000000 % 10 + numbers_list[n] // 1000000 % 10 + numbers_list[n] // 100000 % 10 + numbers_list[n] // 10000 % 10 + numbers_list[n] // 1000 % 10 + numbers_list[n] // 100 % 10 + numbers_list[n] // 10 % 10 + numbers_list[n] % 10) % 7 == 0:
        sum_after_added_17 = sum_after_added_17 + numbers_list[n]
    n += 1
print(sum_after_added_17, "сумма чисел, после добавления 17")
