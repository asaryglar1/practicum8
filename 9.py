n = int(input("Введите число N: "))

if n < 2:
    print("Нет простых чисел в указанном диапазоне")
else:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i: n + 1: i] = [False] * len(sieve[i * i: n + 1: i])
    print("Простые числа до", n, "включительно:")
    for number in range(2, n + 1):
        if sieve[number]:
            print(number, end=' ')