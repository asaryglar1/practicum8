N = int(input("Введите количество ступеней N: "))

for i in range(1, N + 1):
    # Печатаем пробелы перед звездочками
    print("  " * (N - i), end="")
    # Печатаем звездочки для текущей ступени
    print("* " * i)