from flask import Flask, request, render_template, url_for
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
		# get their info from the POST
		return # something

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
