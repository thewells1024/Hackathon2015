from flask import Flask, make_response, request, render_template
from resume_data import UserData, deserialize
from resume_pdf import generate_pdf_from_data

app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Start of the resume-generation process
@app.route('/resume/', methods=['GET', 'POST'])
def resume():
    if request.method == 'GET': # and request.cookies.get('data_cookie') == None:
        return render_template('resume.html', pdf=None)
    #elif request.cookies.get('data_cookie') != None:
        #pdf = generate_pdf_from_data(deserialize(request.cookies.get('data_cookie')))
    else:
        print dict(request.form)
        data = UserData(dict(request.form))
        pdf = generate_pdf_from_data(data)
        #response = make_response(render_template('resume.html', pdf=pdf))
        #response.set_cookie('data_cookie', serialize(data))
        #return response
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
