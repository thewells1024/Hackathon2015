from flask import Flask, make_response, redirect, request, render_template, url_for
from resume_data import serialize, deserialize, parse_http_form, generate_pdf_resume

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
		data = parse_http_form([field for field in request.form])
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
	return render_template('resume_info.html')

# Mockup page for testing
@app.route('/mockup/')
def mockup():
	return render_template('mockup.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.debug = True
	app.run()
