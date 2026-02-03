#Используя словарь посчитать количество уникальных слов в заданном предложении
#«Изучаем язык Питон». Вывести на экран каждую пару «ключ:значение».
text = " Изучаем язык Питон "

word = text.split()

word_count = {}
for word in word:
    word_count[word] = word_count.get(word, 0) + 1
for key, value in word_count.items():
    print(f"{key}: {value}")

print(f"Количество уникальных слов: {len(word_count)}")
