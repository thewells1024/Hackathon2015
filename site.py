# coding=UTF-8
from flask import Flask, make_response, redirect, request, render_template
from resume_data import UserData, deserialize, validate_delim, validate_req, unescape
from resume_pdf import generate_pdf_from_data
from datetime import datetime, timedelta

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Start of the resume-generation process
@app.route('/resume/', methods=['GET', 'POST'])
def resume():
    try:
        if request.method == 'GET':
            data = deserialize(request.cookies.get('data_cookie'))
            return render_template('resume.html', pdf=None, info=data.stringify())
        else:
            data = UserData(dict(request.form))
            if validate_delim(data):
                if validate_req(data):
                    pdf = generate_pdf_from_data(data)
                    response = make_response(render_template('resume.html', pdf=pdf))
                    response.set_cookie('data_cookie', unescape(data.serialize()), expires = datetime.now() + timedelta(days=365))
                    return response
                else:
                    return render_template('resume.html', pdf=None, rfail="Failed")
            else:
                return render_template('resume.html', pdf=None, dfail="Failed")
    except:
        return render_template('resume.html', pdf=None)

# Page about making resumes
@app.route('/info/')
def resume_info():
    return render_template('info.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
