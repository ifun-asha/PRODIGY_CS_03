import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letter check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letter check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one special character.")

    # Final strength result
    if strength_points == 5:
        print("✅ Strong password!")
    elif 3 <= strength_points < 5:
        print("⚠️ Medium strength password.")
    else:
        print("❌ Weak password.")

    # Show feedback if any
    for tip in feedback:
        print("- " + tip)

def main():
    print("~ Password Strength Checker ~")
    pwd = input("Enter your password: ")
    check_password_strength(pwd)

main()
