# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
#   Содержимое первого файла:
#   Четные элементы:
#   Количество четных элементов:
#   Среднее арифметическое:
#   Содержимое второго файла:
#   Нечетные элементы:
#   Количество нечетных элементов:
#   Сумма положительных элементов:

def write_file(file_name, numbers, is_even):
    with open(file_name, 'w') as file:
        if is_even:
            file.write("Четные элементы:\n")
            count = 0
            sum = 0
            for num in numbers:
                if num % 2 == 0:
                    file.write(str(num) + '\n')
                    count += 1
                    sum += num
            file.write("Количество четных элементов: {}\n".format(count))
            file.write("Среднее значение четных элементов: {}\n".format(sum / count))
        else:
            file.write("Нечетные элементы:\n")
            count = 0
            sum = 0
            for num in numbers:
                if num % 2 != 0:
                    file.write(str(num) + '\n')
                    count += 1
                    if num > 0:
                        sum += num
            file.write("количество нечетных элементов: {}\n".format(count))
            file.write("Сумма положительных элементов: {}\n".format(sum))

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
write_file("file1.txt", numbers1, True)
write_file("file2.txt", numbers2, False)

def merge_files(file1, file2, file3):
    with open(file1, 'r') as file1, open(file2, 'r') as file2, open(file3, 'w') as file3:
        file3.write(file1.read())
        file3.write(file2.read())

merge_files("file1.txt", "file2.txt", "file3.txt")