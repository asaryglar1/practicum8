N = int(input("Введите число N: "))
print(f"Совершенные числа до {N}:")
for num in range(2, N + 1):
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    if sum_divisors == num:
        print(num, end=' ')