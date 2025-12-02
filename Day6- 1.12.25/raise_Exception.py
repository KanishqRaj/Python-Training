def checkAge(age):
    if age < 18:
        raise ValueError("Age must be greater than 18")
    return "Allowed"

print(checkAge(16))