for i in range(1, 10):
    left = ''.join(str(d) for d in range(1, i+1))
    right = ''.join(str(d) for d in range(9, 9-i, -1))
    print(f"{left} * 8 + {i} = {right}")

for i in range(1, 10):
    left = ''.join(str(d) for d in range(1, i+1))
    right = '1' * (i + 1)
    print(f"{left} * 9 + {i+1} = {right}")

for i in range(1, 10):
    left = '1' * i
    right = []
    for d in range(1, i+1):
        right.append(str(d))
    for d in range(i-1, 0, -1):
        right.append(str(d))
    right = ''.join(right)
    print(f"{left} * {left} = {right}")