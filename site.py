from flask import Flask, render_template
app = Flask(__name__)

# Homepage
@app.route('/')
def homepage():
	return render_template('homepage.html')

# Start of the resume-generation process
@app.route('/form/', methods = ['GET', 'POST'])
def resume_info_form():
	if request.method == 'GET':
		return # the form
	else:
		# get their info from the POST
		return # something

# Page about making resumes
@app.route('/info/')
def resume_info():
	return render_template('resume_info.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
