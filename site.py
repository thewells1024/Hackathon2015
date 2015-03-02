# coding=UTF-8
from flask import Flask, make_response, request, render_template
from resume_data import UserData, deserialize, validate
from resume_pdf import generate_pdf_from_data

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Start of the resume-generation process
@app.route('/resume/', methods=['GET', 'POST'])
def resume():
    if request.method == 'GET':
        try:
            pdf = generate_pdf_from_data(deserialize(request.cookies.get('data_cookie')))
            response = make_response(render_template('resume.html', pdf=pdf))
        except Exception:
            response = render_template('resume.html', pdf=None)
    else:
        data = UserData(dict(request.form))
        if validate(data):
            pdf = generate_pdf_from_data(data)
            response = make_response(render_template('resume.html', pdf=pdf))
            response.set_cookie('data_cookie', data.serialize())
        else:
            response = render_template('resume.html', pdf=None)
    return response

# Page about making resumes
@app.route('/info/')
def resume_info():
    return render_template('info.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/reset/')
def reset():
    response = make_response(render_template('resume.html', pdf=None))
    return response

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()