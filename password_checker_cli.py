import string
import sys

common_passwords = [
    "123456", "password", "admin", "qwerty",
    "abc123", "password123", "letmein"
]

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long.")

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 2
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 2
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 2
    else:
        feedback.append("Add at least one number.")

    if any(c in string.punctuation for c in password):
        score += 2
    else:
        feedback.append("Add at least one special character.")

    if password.lower() in common_passwords:
        score = 0
        feedback.append("Password is too common and unsafe.")

    return score, feedback


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python password_checker_cli.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    
    print("\n===== ADVANCED PASSWORD CHECKER =====")
    print(f"Testing password: {password}")
    
    score, feedback = check_strength(password)
    
    print("\n----- RESULT -----")
    print(f"Password Score: {score} / 11")
    
    if score <= 4:
        print("Strength: WEAK")
    elif score <= 8:
        print("Strength: MEDIUM")
    else:
        print("Strength: STRONG")
    
    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print(f"  - {f}")
    else:
        print("\nGreat! Your password is secure.")
    
    print("=====================================\n")
