best_score = 0
count = 0
score = int(input())  # Первый ввод до цикла

while score != -1:
    if score > best_score:
        best_score = score
    count += 1  # Увеличиваем счётчик друзей
    score = int(input())  # Следующий ввод в конце цикла

print(f"Лучший результат: {best_score}")
print(f"Количество друзей: {count}")