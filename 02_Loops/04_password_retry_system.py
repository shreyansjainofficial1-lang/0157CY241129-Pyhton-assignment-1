correct_password = "Python@123"
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    entered = input(f"Enter password (attempt {attempt}/{max_attempts}): ")
    if entered == correct_password:
        print("Login successful.")
        break
    print("Incorrect password.")
else:
    print("Maximum attempts reached. Account blocked.")
