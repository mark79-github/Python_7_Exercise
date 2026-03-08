import math

def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        clean_input = user_input.replace('.', '', 1).replace('-', '', 1)
        if clean_input.isdigit():
            return float(user_input)
        else:
            print("Грешка! Моля, въведете валидно число.")

number = get_valid_number("Въведете число: ")
precision = int(get_valid_number("Въведете брой знаци за закръгляване (цяло число): "))

res_floor = math.floor(number)
res_ceil = math.ceil(number)
res_round_fixed = round(number, precision)
res_round_simple = round(number)

print(f"Оригинално число: {number}")
print(f"math.floor({number})  -> {res_floor}")
print(f"math.ceil({number})   -> {res_ceil}")
print(f"round({number}, {precision}) -> {res_round_fixed}")
print(f"round({number})       -> {res_round_simple}")
