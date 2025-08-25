print("\U0001F911 Bill Split Calculator")
amount = float(input("Enter total amount:\n"))
tip = float(input("Enter tip amount percentage:\n"))
tip_amount = (tip / 100) * amount
total = tip_amount + amount
people = int(input("Total no.of people:\n"))
print(f"Total (including tip): ${total}")
amount_person = total / people
print(f"Each person pays: ${amount_person}")
