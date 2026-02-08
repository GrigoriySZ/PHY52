# Задача N1
# Есть два множества:
# neighborhood_A = {'apple', 'banana', 'cherry'}
# neighborhood_B = {'banana', 'cherry', 'date'}
# Используя множества, найдите:
# Общие продукты(пересечение);
# Продукты, которые есть только в одном из двух пространств(симметрическая разность);
# Продукты, отсутствующие в первом, но присутствующие во втором(множество разностей).

neighborhood_A = {'apple', 'banana', 'cherry'}
neighborhood_B = {'banana', 'cherry', 'date'}

# Пересекающиеся продукты двух множеств
intersected_products = neighborhood_A.intersection(neighborhood_B)
print("Похожие продукты в корзинах A и B:",
      *["- " + str.title(p) for p in intersected_products], sep="\n")

# Непересекающиеся продукты обоих множеств
different_products = neighborhood_A.symmetric_difference(neighborhood_B)
print("Отличающиеся продукты в корзинах A и B:",
      *["- " + str.title(p) for p in different_products], sep="\n")

# Уникальные продукты из второго множества
unique_products_in_B = neighborhood_B.difference(neighborhood_A)
print("Уникальные продукты в корзине B:",
      *["- " + str.title(p) for p in unique_products_in_B], sep="\n")

# Задача N2
# Поиск потенциальных «пересекающихся» элементов
# Есть два наборы данных о клиентах:
# customers_region1 = {'Adam', 'Boris', 'Vera'}
# customers_region2 = {'Vera', 'Gina', 'Helga'}
# Определите:
# Кто есть в обоих регионах?
# Кто есть только в первом?
# Кто только во втором?
# Кто не зафиксирован ни там, ни там
# (вычитаем их из полного множественного набора клиентов)?

customers_region1 = {'Adam', 'Boris', 'Vera'}
customers_region2 = {'Vera', 'Gina', 'Helga'}

# Проверяем клиентов, которые есть в обоих регионах
both_regions = customers_region1 & customers_region2
print("Клиенты, которые есть в обоих регионах:",
      *[str(i+1) + ": " + c for i, c in enumerate(both_regions)], sep="\n")

# Проверяем клиентов, которые есть только в первом регионе
region1_only = customers_region1 - customers_region2
print("Клиенты, которые есть только в первом регионе:",
      *[str(i+1) + ": " + c for i, c in enumerate(region1_only)], sep="\n")

# Проверяем клиентов, которые есть только во втором регионе
region2_only = customers_region2 - customers_region1
print("Клиенты, которые есть только в первом регионе:",
      *[str(i+1) + ": " + c for i, c in enumerate(region2_only)], sep="\n")

# Проверяем клиентов, которые не относятся ни к первому, ни ко второму
union_region = customers_region1 | customers_region2
union_regions_only = region1_only ^ region2_only
not_in_regions_only = union_region - union_regions_only
print("Клиенты, которые не относятся ни к первому, ни ко второму региону:",
      *[str(i+1) + ": " + c for i, c in enumerate(not_in_regions_only)], sep="\n")

