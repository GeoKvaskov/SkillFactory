def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
            array[idx] = x
    return array

def search(array, number, left, right):
    if left > right:
        return right
    middle = (right+left) // 2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return search(array, number, left, middle-1)
    elif number > array[middle]:
        return search(array, number, middle+1, right)
    

print('Введите последовательность чисел: ')
list_data = input().split()
int_list = []
for number in list_data:
    if number.isdigit():
        int_list.append(int(number))
    else:
        print(f'{number} - не является числом! ')
        print('Ошибка формирования списка чисел!')
        exit()
        
print(f'Ваша последовательность чисел:', int_list)
sort_list = sort(int_list)
print(f'Отсортированный список:', sort_list)

print('----------------------------------')
print(f'Введите число для поиска:', )
pointer = int(input())
position = search(sort_list, pointer, 0, (len(sort_list)-1))
if position == -1:                                                                                      #Обособляем ситуацию, когда искомое число вне нижней границы последовательности
    print('Искомое число вне нижней границы заданной последовательности')
elif position == len(sort_list)-1:                                                                        #Разграничиваем последнее в ряду число и входящие в это множество
    print('Искомое число находится на верхней границе или за ее пределами заданной последовательности')
else: print('Искомый элемент под номером:', position+1)                                                   #Делаем так, чтобы нумерация начиналась с 1 