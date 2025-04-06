X = int(input())
total = 0
for i in range(1, X + 1):
    total += i
    expression = " + ".join(str(num) for num in range(1, i + 1))
    print(f"{expression} = {total}")