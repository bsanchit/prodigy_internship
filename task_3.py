import re

def assess_password_strength(password):
    
    length_criteria = len(password) > 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = [length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]
    strength = sum(criteria_met)

    feedback = "Password Strength: "
    if strength == 5:
        feedback += "Very Strong"
    elif strength == 4:
        feedback += "Strong"
    elif strength == 3:
        feedback += "Moderate"
    elif strength == 2:
        feedback += "Weak"
    else:
        feedback += "Very Weak"

    feedback += "\n\nCriteria:\n"
    feedback += f"Length (> 8 characters): {'✔️' if length_criteria else '❌'}\n"
    feedback += f"Uppercase Letter: {'✔️' if uppercase_criteria else '❌'}\n"
    feedback += f"Lowercase Letter: {'✔️' if lowercase_criteria else '❌'}\n"
    feedback += f"Number: {'✔️' if number_criteria else '❌'}\n"
    feedback += f"Special Character: {'✔️' if special_char_criteria else '❌'}\n"

    return feedback

def main():
    password = input("Enter a password to assess its strength: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
