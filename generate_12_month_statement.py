from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import random

def generate_12_month_statement(output_file="statement_12_months.pdf"):
    c = canvas.Canvas(output_file, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, 750, "AI National Bank – 12-Month Account Statement")

    c.setFont("Helvetica", 12)
    c.drawString(40, 725, "Account Number: 123456789012")
    c.drawString(40, 710, "Account Holder: John Doe")
    c.drawString(40, 695, "Period: Jan 2024 – Dec 2024")
    c.drawString(40, 680, "Status: Verified")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 650, "Month")
    c.drawString(140, 650, "Deposits (₹)")
    c.drawString(260, 650, "Withdrawals (₹)")
    c.drawString(400, 650, "Closing Balance (₹)")
    c.line(40, 645, 550, 645)

    months = [
        "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024",
        "May 2024", "Jun 2024", "Jul 2024", "Aug 2024",
        "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024"
    ]

    y = 625
    closing_balance = 50000

    c.setFont("Helvetica", 12)

    for m in months:
        deposits = random.randint(10000, 30000)
        withdrawals = random.randint(5000, 20000)
        closing_balance = closing_balance + deposits - withdrawals

        c.drawString(40, y, m)
        c.drawString(140, y, f"₹{deposits:,}")
        c.drawString(260, y, f"₹{withdrawals:,}")
        c.drawString(400, y, f"₹{closing_balance:,}")

        y -= 25
        if y < 80:
            c.showPage()
            y = 750

    c.showPage()
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 750, "Year-End Summary")

    c.setFont("Helvetica", 12)
    c.drawString(40, 720, f"Final Closing Balance: ₹{closing_balance:,}")
    c.drawString(40, 700, "Average Monthly Balance: ₹52,300.75")
    c.drawString(40, 680, "Account Status: Verified")

    c.save()
    print(f"Generated 12-month statement PDF: {output_file}")


if __name__ == "__main__":
    generate_12_month_statement()
