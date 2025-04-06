best_score = 0
score = int(input())  # Первый ввод до цикла
while score != -1:
    if score > best_score:
        best_score = score
    score = int(input())  # Следующий ввод в конце цикла
print(best_score)