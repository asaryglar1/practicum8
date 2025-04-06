total_income = 0
count = 0
income = float(input())
while income != 0:
    total_income += income
    count += 1
    income = float(input())
if count > 0:
    average_income = total_income / count
    print(f"Средний доход: {average_income:.2f}")