import math

def input_bounded(prompt, min_val, max_val, is_int):
    while True:
        try:
            val = float(input(prompt))
            if min_val <= val <= max_val:
                return int(val) if is_int else val
            else:
                print(f"Стойността трябва да е между {min_val} и {max_val}")
        except ValueError:
            print("Моля, въведете валидно число")

box_w = input_bounded("Ширина на кашона от 20 до 70 cm: ", 20, 70, True)
box_h = input_bounded("Дължина на кашона от 20 до 70 cm: ", 20, 70, True)
plat_w = input_bounded("Ширина на платформата от 0.8 до 2.8 m: ", 0.8, 2.8, False) * 100
plat_h = input_bounded("Дължина на платформата от 0.8 до 2.8 m: ", 0.8, 2.8, False) * 100

count_1 = math.floor(plat_w / box_w) * math.floor(plat_h / box_h)
count_2 = math.floor(plat_w / box_h) * math.floor(plat_h / box_w)

print(f"Максимален брой кашони: {max(count_1, count_2)} бр.")