# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}")


# Создаем объект класса Товар
product1 = Product("Мышка", 2990, 50)
product2 = Product("Клавиатура", 4990, 30)

# Выводим информацию о каждом товаре
print("Информация о товаре 1:")
product1.display_info()

print("\nИнформация о товаре 2:")
product2.display_info()
