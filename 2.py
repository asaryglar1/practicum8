best_score = 0
count = 0
score = int(input())
while score != -1:
    if score > best_score:
        best_score = score
    count += 1
    score = int(input())
print(f"Лучший результат: {best_score}")
print(f"Количество друзей: {count}")