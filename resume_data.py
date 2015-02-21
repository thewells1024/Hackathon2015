# NOTE 'a python object' needs to be a standardized thing

# Takes a python object and returns JSON for a cookie
def serialize(data):
	pass

# Takes a JSON object and returns a python object
def deserialize(data):
	pass

# Takes a python dictionary representation of our form and returns a python object
def parse_http_form(formList):
	pass

# Takes a python object and returns a python file descriptor to /static/tmp/<session_id>_<secure_filename>.pdf containing the pdf resume
def generate_pdf_resume(data):
	pass
