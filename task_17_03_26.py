def validate_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Грешка: въведени са невалидни стойности.")
        except ValueError:
            print("Грешка: въведени са невалидни стойности.")

capacity = validate_float("Въведете капацитет на машината (литри на партида): ")
process_time = validate_float("Въведете време за една партида (в минути): ")
work_hours = validate_float("Въведете работни часове за деня: ")

total_minutes = work_hours * 60
batches = total_minutes // process_time
total_output = batches * capacity

print(f"За един работен ден могат да бъдат произведени {int(total_output)} литра напитка ({int(batches)} партиди).")