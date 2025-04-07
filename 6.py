N = int(input("Введите количество ступеней N: "))

for i in range(1, N + 1):
    print("  " * (N - i), end="")
    print("* " * i)