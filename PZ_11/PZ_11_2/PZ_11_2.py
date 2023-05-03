# Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.



# читаем содержимое текстового файла
with open("text18-22.txt", "r", encoding='UTF-8') as file:
    text = file.read()
print("Original text:")
print(text)

# считаем количество заглавных букв
upper_count = sum(1 for c in text if c.isupper())
print("Number of uppercase letters:", upper_count)

# заменяем символы в третьей строке их ASCII-кодами
lines = text.split("\n")
if len(lines) >= 3:
    lines[2] = "".join(str(ord(c)) + " " for c in lines[2])
new_text = "\n".join(lines)

# записываем новый текст в новый файл в стихотворной форме
with open("new_file.txt", "w") as new_file:
    new_file.write(new_text)