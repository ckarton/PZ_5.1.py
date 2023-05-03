# Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц

def calculate_grades(grades):
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    total = 0

    for grade in grades:
        if grade == 2:
            two_count += 1
        elif grade == 3:
            three_count += 1
        elif grade == 4:
            four_count += 1
        elif grade == 5:
            five_count += 1
        total += grade

    average = total / len(grades)

    return (two_count, three_count, four_count, five_count, average)


grades = [3, 4, 4, 5, 4, 3, 3, 5, 5, 4, 2, 4, 5, 5, 5, 4, 3, 5, 4, 5]
(two_count, three_count, four_count, five_count, average) = calculate_grades(grades)

print("Количество 2:", two_count)
print("Количество 3:", three_count)
print("Количество 4:", four_count)
print("Количество 5:", five_count)
print("Средний:", average)