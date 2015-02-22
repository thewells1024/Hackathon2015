from time import time
from random import randrange
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 

def get_secure_filename():
    return '/static/resumes/test.pdf'
    s = str(time()).replace('.', '')
    s+= str(random())[2:]
    return '/static/resumes/' + s + '.pdf'

def generate_pdf_from_data(data):
    filename = get_secure_filename()
    doc = SimpleDocTemplate(filename,pagesize=letter, rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18)
    Story=[]
    
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Left', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Right', alignment=TA_CENTER))
    
    ptext = '<font size=18>%s</font>' % data.personal_info['name'] 
    Story.append(Paragraph(ptext, styles["Center"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=10>%s</font>' % data.personal_info['phone'] 
    Story.append(Paragraph(ptext, styles["Center"]))
    ptext = '<font size=10>%s</font>' % data.personal_info['email'] 
    Story.append(Paragraph(ptext, styles["Center"]))
    ptext = '<font size=10>%s</font>' % data.personal_info['location'] 
    Story.append(Paragraph(ptext, styles["Center"]))
    Story.append(Spacer(1, 24))

    ptext = '<font size=12>%s</font>' % data.education['school' + i + 'name']
    Story.append(Paragraph(ptext, styles["Left"]))

    doc.build(Story)
    return filename 