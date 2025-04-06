while True:
    user_input = input("Введите число: ")
    if user_input.lstrip('-').isdigit():
        number = int(user_input)
        print(f"Введено целое число: {number}")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")