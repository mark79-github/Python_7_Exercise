PRICE_NUT = 0.13
PRICE_BOLT = 0.45
PRICE_SCREW = 0.09

nuts_count = int(input("Въведете брой гайки: "))
bolts_count = int(input("Въведете брой болтове: "))
screws_count = int(input("Въведете брой винтове: "))

total_no_vat = (nuts_count * PRICE_NUT) + (bolts_count * PRICE_BOLT) + (screws_count * PRICE_SCREW)

vat_amount = round(total_no_vat * 0.20, 2)

final_price = total_no_vat + vat_amount

print(f"Цена без ДДС: {total_no_vat:.2f} лв.")
print(f"ДДС (20%): {vat_amount:.2f} лв.")
print(f"Крайна цена за плащане: {final_price:.2f} лв.")
