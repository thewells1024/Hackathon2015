from time import time
from random import randrange
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 

def get_secure_filename():
    return 'test.pdf'
    s = str(time()).replace('.', '')
    s+= str(random())[2:]
    return '/tmp/resumes/' + '.pdf'

def generate_pdf_from_data(data):
    doc = SimpleDocTemplate(get_secure_filename(),pagesize=letter, rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18)
    Story=[]
    
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    ptext = '<font size=18>%s</font>' % data.personal_info['name'] 
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    doc.build(Story)
