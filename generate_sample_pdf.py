from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf(output="sample_statement.pdf"):
    c = canvas.Canvas(output, pagesize=letter)

    t = c.beginText(40, 720)
    t.setFont("Helvetica", 12)

    t.textLine("Sample Bank Statement")
    t.textLine("Account: 123456789012")
    t.textLine("Period: Jan-Dec 2024")
    t.textLine("Average Balance: ₹52,300.75")
    t.textLine("Status: verified")

    c.drawText(t)
    c.save()

if __name__ == "__main__":
    create_pdf()
