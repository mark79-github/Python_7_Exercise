print("Програма за разреждане на сок (натиснете Enter без число за край):")

while True:
    input_water_ml = input("Въведете количество вода в mL: ")

    if input_water_ml == "":
        break

    try:
        water_ml = float(input_water_ml)
        concentrate_ml = water_ml / 7
        result = round(concentrate_ml)
    except ValueError:
        print("Моля, въведете валидно число!")
    else:
        print(f"Нужен концентрат: {result} mL")

print("Програмата приключи")