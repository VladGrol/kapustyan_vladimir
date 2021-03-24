task_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for element in task_list:
    list_split = element.split(" ")
    print(f'Привет, {list_split[-1].title()}!')
