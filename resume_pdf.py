from time import time
from random import random
import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 
def get_secure_filename():
    s = str(time()).replace('.', '')
    s+= str(random())[2:]
    return 'static/resumes/' + s + '.pdf'

def generate_pdf_from_data(data):
    filename = get_secure_filename()
    subprocess.check_call(['touch', filename])
        
    doc = SimpleDocTemplate(filename,pagesize=letter, rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18)
    Story = []
    
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT))
    
    Story.append(Paragraph('<font size=18>%s</font>' % data.personal_info['name'], styles["Center"]))
    Story.append(Spacer(1, 12))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['phone'], styles["Center"]))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['email'], styles["Center"]))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['location'], styles["Center"]))
    Story.append(Spacer(1, 24))
 
    Story.append(Paragraph('<font size=12 style=bold>Education</font>', styles["Left"]))    
    Story.append(Paragraph('<font size=12>%s</font>' % data.education[0]['name'], styles["Left"]))
    
    Story.append(Paragraph('<font size=12 bold>Experience</font>', styles["Left"]))

    Story.append(Paragraph('<font size=12 style=bold>Projects</font>', styles["Left"]))

    Story.append(Paragraph('<font size=12 style=bold>Skills</font>', styles["Left"]))
    for skill in data.skills:
        Story.append(Paragraph('<font size=12>%s</font>' % skill, styles['Left']))

    doc.build(Story)
    return '/' + filename 
