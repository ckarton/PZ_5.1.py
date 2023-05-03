# чтение файла
with open("ip_address.txt", "r") as f:
    ips = f.readlines()

# удаление символа новой строки из каждой строки
ips = [ip.strip() for ip in ips]

# разделяющие IP-адреса нулевым четвертым октетом
zeros = [ip for ip in ips if ip.split(".")[3] == "0"]
others = [ip for ip in ips if ip.split(".")[3] != "0"]

# запись в файл 1
with open("file1.txt", "w") as f:
    f.write("\n".join(zeros))

# запись в файл 2
with open("file2.txt", "w") as f:
    f.write("\n".join(others))

# подсчет количества строк в каждом файле
with open("file1.txt", "r") as f:
    count1 = len(f.readlines())
with open("file2.txt", "r") as f:
    count2 = len(f.readlines())

# вывод количества строк в каждом файле
print("Number of lines in file1.txt:", count1)
print("Number of lines in file2.txt:", count2)