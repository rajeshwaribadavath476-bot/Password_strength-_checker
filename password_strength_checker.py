import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


# Main Program
password = input("Enter a password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions to improve security:")
    for item in feedback:
        print("-", item)
else:
    print("Excellent! Your password meets all security requirements.")