N = int(input("Введите N: "))
count = 0
for num in range(2, N + 1):
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    if sum_divisors == num:
        count += 1
print(f"Количество совершенных чисел от 2 до {N}: {count}")