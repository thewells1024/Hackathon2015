from flask import Flask, make_response, redirect, request, render_template, url_for
from resume_data import UserData

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Start of the resume-generation process
@app.route('/form/', methods = ['GET', 'POST'])
def resume_info_form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = UserData(request.form)
        response = make_response(redirect(url_for('resume')))
        response.set_cookie(serialize(data))
        return response

@app.route('/resume/')
def resume_generator():
    data = deserialize(request.cookies.get('form_data'))
    pdf = generate_pdf_resume(data)
    return render_template('resume.html', pdf=pdf)

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
