input_water_ml_ml = float(input("Въведете количество вода в mL: "))

concentrate_ml = input_water_ml_ml / 7

result = round(concentrate_ml)

print(f"За {input_water_ml_ml:.0f} mL вода трябва да добавите {result} mL концентрат.")