from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def get_secure_filename():
    return "test.pdf"

def generate_pdf_from_data(data):
    c = canvas.Canvas(get_secure_filename(), pagesize=letter)
    c.setFont('Helevetica', 12)
    c.setLineWidth(2)

