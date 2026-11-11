
import math
import string


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "iloveyou",
    "abc123",
    "letmein"
}


def analyze_password(password):

    score = 0
    findings = []
    recommendations = []

    # 1. Check password length
    length = len(password)

    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        findings.append("Password is too short.")
        recommendations.append("Use at least 12 characters.")

    # 2. Check character variety
    if any(c.islower() for c in password):
        score += 15
    else:
        findings.append("No lowercase letters found.")
        recommendations.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 15
    else:
        findings.append("No uppercase letters found.")
        recommendations.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 15
    else:
        findings.append("No numbers found.")
        recommendations.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 15
    else:
        findings.append("No special characters found.")
        recommendations.append("Add special characters.")

    # 3. Detect common passwords
    if password.lower() in COMMON_PASSWORDS:
        score -= 40
        findings.append("This is a commonly used password.")
        recommendations.append("Avoid common password choices.")

    # 4. Detect repeated characters
    if len(password) >= 3 and len(set(password)) == 1:
        score -= 25
        findings.append("Password contains only repeated characters.")
        recommendations.append("Use a more varied combination.")

    # 5. Detect predictable sequences
    lower_password = password.lower()

    alphabet_sequences = [
        string.ascii_lowercase[i:i+4]
        for i in range(23)
    ]

    number_sequences = [
        string.digits[i:i+4]
        for i in range(7)
    ]

    keyboard_sequences = [
        "qwer", "asdf", "zxcv",
        "poiuy", "lkjh", "mnbv"
    ]

    all_sequences = (
        alphabet_sequences
        + number_sequences
        + keyboard_sequences
    )

    if any(seq in lower_password for seq in all_sequences):
        score -= 15
        findings.append(
            "Password contains a predictable sequence."
        )
        recommendations.append(
            "Avoid consecutive letters, numbers and keyboard patterns."
        )


    # 5. Estimate theoretical entropy
    pool = 0

    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    entropy = 0

    if pool > 0:
        entropy = length * math.log2(pool)

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # 6. Assign a rating
    if score >= 80:
        rating = "Strong"
    elif score >= 50:
        rating = "Moderate"
    else:
        rating = "Weak"

    if not findings:
        findings.append("No basic weaknesses detected by these checks.")

    if not recommendations:
        recommendations.append("Continue using unique passwords.")

    return {
        "score": score,
        "rating": rating,
        "entropy": round(entropy, 2),
        "findings": findings,
        "recommendations": recommendations
    }
