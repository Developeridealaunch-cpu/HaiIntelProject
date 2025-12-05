import re
from llm_extract import llm_extract

def find_account_number(text):
    m = re.search(r"(?:Account|A/c|Acct)[^\d]{0,10}([0-9]{6,20})", text, re.I)
    return m.group(1) if m else None

def find_period(text):
    m = re.search(r"(Period|Statement Period)[:\s]+([A-Za-z0-9\-–\s,]+[0-9]{4})", text, re.I)
    return m.group(2).strip() if m else None

def find_avg_balance(text):
    m = re.search(r"(Average Balance|Avg Balance)[:\s₹$]*([0-9,]+\.\d+)", text, re.I)
    if m:
        return float(m.group(2).replace(",", ""))
    return None

def find_status(text):
    for word in ["verified", "unverified", "pending", "approved", "closed"]:
        if word in text.lower():
            return word
    return "unknown"


def extract_fields(text):
    # Rule-based extraction
    acc = find_account_number(text)
    period = find_period(text)
    avg = find_avg_balance(text)
    status = find_status(text)

    score = 0
    if acc: score += 0.4
    if period: score += 0.3
    if avg: score += 0.2
    if status != "unknown": score += 0.1

    # If rules are confident enough → return results
    if score >= 0.7:
        return {
            "accountNumber": acc,
            "period": period,
            "avgBalance": avg,
            "status": status
        }, round(score, 2)

    # Otherwise → fallback to LLM extraction
    llm_values = llm_extract(text)

    # Confidence from number of extracted fields
    non_null = sum(1 for v in llm_values.values() if v)
    conf = min(0.99, 0.4 + 0.12 * non_null)

    return llm_values, round(conf, 2)
