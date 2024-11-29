import re

def check_password_strength(password):
    """
    Assess the strength of a given password based on various criteria.
    """
    # Initialize variables
    strength_score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength_score += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Provide overall feedback
    if strength_score == 5:
        return f"Password Strength: Strong ({strength_score}/5)\nGreat job! Your password is very secure."
    elif strength_score >= 3:
        return f"Password Strength: Moderate ({strength_score}/5)\nSuggestions:\n" + "\n".join(feedback)
    else:
        return f"Password Strength: Weak ({strength_score}/5)\nSuggestions:\n" + "\n".join(feedback)


if __name__ == "__main__":
    print("Welcome to the Password Complexity Checker!")
    user_password = input("Enter a password to evaluate: ")
    result = check_password_strength(user_password)
    print(result)
