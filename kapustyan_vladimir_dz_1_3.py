number = int(input('Введите число'))
words = ['процент', 'процента', 'процентов']
group_1 = [2,3,4]
group_2 = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
if (number in group_1):
    print(words[1])
elif (number in group_2):
    print(words[2])
elif (number == 1):
    print(words[0])
n=int(1)
while n <= 20:
    if (n in group_1):
        print(n,words[1])
    elif (n in group_2):
        print(n,words[2])
    elif (n == 1):
        print(n,words[0])
    n += 1