import time import time
from random import randrange
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 

def get_secure_filename():
    s = str(time()).replace('.', '')
    s+=str(random())[2:]
    return '/tmp/resumes/' + '.pdf'

def generate_pdf_from_data(data):
    doc = SimpleDocTemplate(get_secure_filename(),pagesize=letter, rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18)
    Story=[]

    doc.build(Story)
    return doc

