# Задача N1.
# Написать функцию-генератор, которая примет количество чисел N
# а будет возвращать N чисел последовательности Фибоначчи.
# Каждое число такой последовательности равно сумме двух предыдущих.

def fibonacci(number: int):
    num_a = 0
    num_b = 1
    while num_a < number:
        yield num_a
        num_a, num_b = num_b, num_a + num_b

for num in fibonacci(10):
    print(num, end=" ")
else:
    print("\n")

# Задача N2.
# Написать функцию, которая примет список, а вернёт словарь,
# где ключом будут элементы списка, а значениями их количество.
# То есть функция должна посчитать количество элементов в списке.

def list_to_dict(lst: list):
    dct = {i+1: lst[i] for i  in range(len(lst))}
    return dct

test_lst = [1, 6, 7, -5, 7, 11, 0, -12, 2, -4]
print(list_to_dict(test_lst))