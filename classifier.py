import re

LOAN_KWS = ["loan", "emi", "agreement", "borrower", "lender", "sanction", "interest"]
STATEMENT_KWS = ["statement", "deposits", "withdrawals", "balance", "transactions"]

def classify_document(text):
    txt = text.lower()

    loan_count = sum(1 for kw in LOAN_KWS if kw in txt)
    stmt_count = sum(1 for kw in STATEMENT_KWS if kw in txt)

    if loan_count > stmt_count:
        return "loan", min(0.95, 0.6 + 0.05 * loan_count)
    elif stmt_count > loan_count:
        return "statement", min(0.95, 0.6 + 0.05 * stmt_count)
    else:
        return "unknown", 0.3
