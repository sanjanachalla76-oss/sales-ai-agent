def qualify_lead(lead_info):
    score = 0

    if lead_info.get("budget", 0) > 500:
        score += 1
    if lead_info.get("interest_level", "") == "high":
        score += 1
    if lead_info.get("timeline", "") == "immediate":
        score += 1

    return f"Lead Score: {score}/3"


def recommend_product(lead_info):
    if lead_info.get("budget", 0) > 1000:
        return "Recommended: Premium Plan"
    elif lead_info.get("budget", 0) > 500:
        return "Recommended: Standard Plan"
    else:
        return "Recommended: Basic Plan"


def draft_email(lead_info):
    return f"""
Hi {lead_info.get('name', 'Customer')},

Thank you for your interest in our product.
Based on your needs, we recommend the best plan for you.

Let us know a good time to connect.

Best regards,
Sales Team
"""