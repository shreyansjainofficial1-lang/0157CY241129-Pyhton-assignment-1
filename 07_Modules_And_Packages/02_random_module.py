import random
import string

otp = "".join(random.choices(string.digits, k=6))
password_characters = string.ascii_letters + string.digits + "!@#$%^&*"
random_password = "".join(random.choices(password_characters, k=12))
random_numbers = [random.randint(1, 100) for _ in range(10)]

print("Six-digit OTP:", otp)
print("Random password:", random_password)
print("Random list:", random_numbers)
