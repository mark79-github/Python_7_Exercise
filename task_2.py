def is_numb(x):
    try:
        float(x)
    except ValueError:
        return False
    else:
        return True

num = input("Въведете число: ")

while not is_numb(num):
    print("Грешка! Това не е валидно число.")
    num = input("Опитайте отново: ")

num = float(num)
print("Въведохте числото:", num)