# Тип учебного материала
while True:
    item_type = str.lower(input("Введите название типа учебного материала (книга/видео): "))
    if item_type == "книга" or item_type == "видео":
        break
    else:
        print("Неверный ввод!")

# Категория товара
item_category = str.lower(input("Введите категорию товара: "))

# Стоимость товара
while True:
    try:
        item_cost = float(input("Введите стоимость материала: "))
        if item_cost >= 0:
            print("Материал успешно добавлен.")
            break
        else:
            print("Ошибка! Цена товара не может быть отрицательной. Пожалуйста, введите положительное значение.")
    except ValueError:
        print("Ошибка! Пожалуйста, введите цену в числовом виде.")

# Сообщение о завершении ввода товара
message_result = f"Ваш материал: Тип - {item_type}, Стоимость - {item_cost:.2f}, Категория - {item_category}"
print(message_result)