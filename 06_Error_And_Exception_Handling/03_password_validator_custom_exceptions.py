class PasswordTooShortError(Exception):
    pass

class MissingUppercaseError(Exception):
    pass

class MissingNumberError(Exception):
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters.")
    if not any(char.isupper() for char in password):
        raise MissingUppercaseError("Password must contain at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        raise MissingNumberError("Password must contain at least one number.")
    return "Password is valid."

try:
    entered_password = input("Enter a password: ")
    print(validate_password(entered_password))
except (PasswordTooShortError, MissingUppercaseError, MissingNumberError) as error:
    print("Invalid password:", error)
