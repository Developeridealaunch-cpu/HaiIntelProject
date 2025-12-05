import os, json, re

OPENAI_AVAILABLE = False
try:
    import openai
    OPENAI_AVAILABLE = True
except:
    pass

FIELDS = [
    "accountNumber", "period", "avgBalance", "status",
    "loanAmount", "emiAmount", "loanTenure",
    "borrowerName", "lenderName", "agreementDate"
]

def llm_extract(text):
    if OPENAI_AVAILABLE and os.getenv("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"):
        try:
            openai.api_key = os.getenv("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")
            prompt = f"""
Extract these fields from the document:
{FIELDS}

Return only valid JSON.

Document:
{text}
"""
            resp = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a strict JSON extraction engine."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0,
            )

            content = resp.choices[0].message["content"]
            parsed = json.loads(content)
            return parsed
        except:
            return {}

    # Offline fallback heuristics (if no LLM available)
    extracted = {}
    extracted["accountNumber"] = re.search(r"Account[:\s]*([0-9]{6,20})", text, re.I)
    extracted["loanAmount"] = re.search(r"Loan Amount[:\s₹]*([0-9,]+)", text, re.I)
    extracted["emiAmount"] = re.search(r"EMI[:\s₹]*([0-9,]+)", text, re.I)
    extracted["borrowerName"] = re.search(r"Borrower[:\s]*([A-Za-z ]+)", text, re.I)
    extracted["lenderName"] = re.search(r"(Lender|Financer)[:\s]*([A-Za-z ]+)", text, re.I)

    # Convert and clean
    out = {}
    for key, value in extracted.items():
        if value:
            v = value.group(1) if isinstance(value.group(1), str) else value.group(2)
            out[key] = v.strip()
        else:
            out[key] = None

    return out
