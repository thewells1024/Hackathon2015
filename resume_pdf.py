# coding=UTF-8
from time import time
from random import random
import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# Generates a unique filename for a resume pdf
def get_secure_filename():
    s = str(time()).replace('.', '')
    s+= str(random())[2:]
    return 'static/resumes/' + s + '.pdf'

# Takes a user data object and populates a pdf with the info, returning the url path to the pdf file
def generate_pdf_from_data(data):
    if data == None:
        return None
    filename = get_secure_filename()
    subprocess.check_call(['touch', filename])
        
    doc = SimpleDocTemplate(filename,pagesize=letter, rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18)
    Story = []
    
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="tabbed", leftIndent=24))
    
    Story.append(Paragraph('<font size=18>%s</font>' % data.personal_info['name'], styles['Center']))
    Story.append(Spacer(1, 12))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['phone'], styles['Center']))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['email'], styles['Center']))
    Story.append(Paragraph('<font size=10>%s</font>' % data.personal_info['location'], styles['Center']))
    Story.append(Spacer(1, 24))
 
    Story.append(Paragraph('<font size=12><b>Education</b></font>', styles['Left']))    
    for school in data.education:
        Story.append(Paragraph('<font size=12>%s, %s</font>' % (school['name'], school['location']), styles['Left']))
        Story.append(Paragraph('<font size=12>%s, %s (graduation year %s)</font>' % (school['degree'], school['status'], school['year']), styles['tabbed']))
        try:
            Story.append(Paragraph('<font size=12>GPA: %s</font>' % school['gpa'], styles['tabbed']))
        except KeyError:
            pass
        Story.append(Spacer(1, 12))
    
    if data.work_experience:
        Story.append(Paragraph('<font size=12><b>Experience</b></font>', styles['Left']))
        for job in data.work_experience:
            Story.append(Paragraph('<font size=12>%s, %s %s %s</font>' % (job['position'], job['employer'], job['location'], job['time_period']), styles['tabbed']))
            for comment in job['comments'].split("\n"):
                Story.append(Paragraph('<font size=12>%s</font>' % comment, styles['tabbed']))
            Story.append(Spacer(1, 12))
    
    if data.projects:
        Story.append(Paragraph('<font size=12><b>Projects</b></font>', styles["Left"]))
        for item in data.projects:
            Story.append(Paragraph('<font size=12>%s</font>' % item['title'], styles['Left']))
            Story.append(Paragraph('<font size=12>%s</font>' % item['summary'], styles['tabbed']))
            for comment in item['comments'].split("\n"):
                Story.append(Paragraph('<font size=12>%s</font>' % comment, styles['tabbed']))
            Story.append(Spacer(1, 12))

    Story.append(Paragraph('<font size=12><b>Skills</b></font>', styles['Left']))
    for skill in data.skills:
        Story.append(Paragraph('<font size=12>%s</font>' % skill, styles['tabbed']))

    doc.build(Story)
    return '/' + filename 
