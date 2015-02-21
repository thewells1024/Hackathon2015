from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('homepage.html')

@app.route('/form/', methods = ['GET', 'POST'])
def resume_info_form():
	if request.method == 'GET':
		return # the form
	else:
		# get their info from the POST

@app.route('/info/')
def resume_ideas():
	# static page about making resumes
	return


if __name__ == '__main__':
	app.debug = True
	app.run()
