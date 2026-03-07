import math

box_w = int(input("Ширина на кашона в cm: "))
box_h = int(input("Дължина на кашона в cm: "))
plat_w_m = float(input("Ширина на платформата в m: "))
plat_h_m = float(input("Дължина на платформата в m: "))

plat_w = plat_w_m * 100
plat_h = plat_h_m * 100

count_1 = math.floor(plat_w / box_w) * math.floor(plat_h / box_h)
count_2 = math.floor(plat_w / box_h) * math.floor(plat_h / box_w)

result = max(count_1, count_2)
print(f"Максимален брой кашони: {result} бр.")