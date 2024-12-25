import re

def check_password_strength(password):
    strength = 0
    missing_conditions = []

    if len(password) >= 12:
        strength += 2
    else:
        missing_conditions.append("+12 characters.")
    if re.search(r'[A-Z]', password):
        strength += 2
    else:
        missing_conditions.append("Uppercase letter.")
    if re.search(r'[a-z]', password):
        strength += 2
    else:
        missing_conditions.append("Lowercase letter.")
    if re.search(r'\d', password):
        strength += 2
    else:
        missing_conditions.append("Number (0-9).")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 2
    else:
        missing_conditions.append("Special character (!, @, #, $, etc.).")

    if strength >= 8:
        level = "strong"
    elif strength >= 5:
        level = "moderate"
    else:
        level = "weak"

    return strength, level, missing_conditions

password = input("Enter a password to check its strength: ")
strength, level, missing_conditions = check_password_strength(password)

if level == "strong":
    print(f"Your password is strong ({strength}/10).")
    if strength == 10:
        print("Congratulations! Your password is top secure!")
elif level == "moderate":
    print(f"Your password is moderate ({strength}/10). It is missing: {', '.join(missing_conditions)}")
else:
    print(f"Your password is weak ({strength}/10). To create a strong password, include:")
    print("- +12 characters.\n- Uppercase letter(A-Z).\n- Lowercase letter(a-z).\n- Number (0-9).\n- Special character (!, @, #, $, etc.).")

# GitHub promotion at the end
print("\nCheck out more cool projects on my GitHub: https://github.com/waelzaafouri")
