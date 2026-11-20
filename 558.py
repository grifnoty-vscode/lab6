n = int(input("Введіть кількість синонімів: "))
sunoims = {}

for i in range(n):
    word1, word2 = input("Введіть синоніми: ").split()
    sunoims[word1] = word2
    sunoims[word2] = word1

target = input("Введіть слово для пошуку: ").strip()
print(sunoims[target])
