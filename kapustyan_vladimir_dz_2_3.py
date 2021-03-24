task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i <= len(task_list):
    if i >= len(task_list):
        break
    elif task_list[i].isalpha():
        i += 1
    else:
        if len(task_list[i]) < 2:
            task_list[i] = "0" + task_list[i]
        if task_list[i][0].isdigit():
            pass
        else:
            temporary_string = task_list.pop(i)
            temporary_string = temporary_string[:1] + "0" + temporary_string[1:]
            task_list.insert(i, temporary_string)
        task_list.insert(i, '"')
        task_list.insert(i + 2, '"')
        i += 3
print(task_list)

print(f'{task_list[0]} {"".join(task_list[1:4])} {task_list[4]} {"".join(task_list[5:8])} {task_list[8]} '
      f'{task_list[9]} {task_list[10]} {task_list[11]} {"".join(task_list[12:15])} {task_list[15]}')
