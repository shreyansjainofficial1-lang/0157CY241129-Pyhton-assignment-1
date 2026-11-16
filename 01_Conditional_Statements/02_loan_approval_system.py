salary = float(input("Enter monthly salary (Rs.): "))
credit_score = int(input("Enter credit score: "))
age = int(input("Enter age: "))

salary_ok = salary >= 30000
credit_ok = credit_score >= 700
age_ok = 21 <= age <= 60

conditions_met = sum([salary_ok, credit_ok, age_ok])

if conditions_met == 3:
    result = "Approved"
elif conditions_met == 2:
    
    result = "Conditionally Approved"
else:
    result = "Rejected"

print("Loan status:", result)
