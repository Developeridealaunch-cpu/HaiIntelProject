# generate_loan_agreement.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import date

def generate_loan_agreement(output="loan_agreement_sample.pdf"):
    c = canvas.Canvas(output, pagesize=letter)

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 750, "LOAN AGREEMENT")
    c.setFont("Helvetica", 10)
    c.drawString(40, 735, f"Agreement Date: {date.today().strftime('%d/%m/%Y')}")

    # Lender / Borrower info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 705, "LENDER:")
    c.setFont("Helvetica", 11)
    c.drawString(120, 705, "ABC Finance Pvt Ltd")
    c.drawString(120, 690, "Registered Office: 12 Finance Street, Mumbai")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 660, "BORROWER:")
    c.setFont("Helvetica", 11)
    c.drawString(120, 660, "John Doe")
    c.drawString(120, 645, "Address: 101 Home Lane, Pune")

    # Loan terms
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 615, "LOAN TERMS")
    c.setFont("Helvetica", 11)
    c.drawString(40, 595, "Loan Amount: ₹500,000.00")
    c.drawString(40, 580, "Interest Rate (p.a.): 10.5%")
    c.drawString(40, 565, "Tenure: 36 months")
    c.drawString(40, 550, "EMI (approx): ₹16,300.00")
    c.drawString(40, 535, "Start Date: 01/04/2024")
    c.drawString(40, 520, "Maturity Date: 01/04/2027")

    # Clauses (multi-line paragraph)
    c.setFont("Helvetica", 10)
    text = c.beginText(40, 490)
    text.setLeading(14)
    text.textLines([
        "This Loan Agreement is made between ABC Finance Pvt Ltd (the 'Lender') and John Doe (the 'Borrower').",
        "The Lender agrees to lend and the Borrower agrees to borrow the principal sum of ₹500,000 on the terms set out below.",
        "The Borrower shall repay the loan in equated monthly instalments (EMIs) together with interest at the stated rate.",
        "The Borrower agrees to pay all fees, charges, and costs associated with this loan as set out in the schedule.",
    ])
    c.drawText(text)

    # Signature lines
    c.setFont("Helvetica", 11)
    c.drawString(40, 200, "_________________________")
    c.drawString(40, 185, "Signature of Borrower")
    c.drawString(350, 200, "_________________________")
    c.drawString(350, 185, "Authorized signatory, Lender")

    # Footer / metadata fields included to make OCR extraction easier
    c.setFont("Helvetica", 9)
    c.drawString(40, 150, "Document ID: LN-2024-0001")
    c.drawString(40, 135, "Sanctioned Amount: ₹500,000")
    c.drawString(40, 120, "EMI Amount: ₹16,300")
    c.drawString(40, 105, "Applicant Name: John Doe")
    c.drawString(40, 90, "Financer: ABC Finance Pvt Ltd")

    c.save()
    print(f"Generated loan agreement PDF: {output}")

if __name__ == "__main__":
    generate_loan_agreement()
