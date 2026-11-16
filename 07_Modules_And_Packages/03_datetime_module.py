from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))

birth_text = input("Enter date of birth (DD-MM-YYYY): ")
birth_date = datetime.strptime(birth_text, "%d-%m-%Y").date()
today = date.today()

if birth_date > today:
    print("Date of birth cannot be in the future.")
else:
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    print("Age:", age, "years")
