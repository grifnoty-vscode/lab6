counts = {i: 0 for i in range(1, 10)}

# Зчитуємо весь рядок чисел
numbers = map(int, input("Введіть числа: ").split())

for num in numbers:
    if num == 0:
        break 
    if num in counts:
        counts[num] += 1

print(*(counts[i] for i in range(1, 10)))