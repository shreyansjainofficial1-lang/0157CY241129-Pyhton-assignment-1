def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if amount > balance:
        raise ValueError("Withdrawal exceeds available balance.")
    return balance - amount

try:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))
    remaining = withdraw(balance, amount)
    print(f"Withdrawal successful. Remaining balance: Rs. {remaining:.2f}")
except ValueError as error:
    print("Transaction error:", error)
