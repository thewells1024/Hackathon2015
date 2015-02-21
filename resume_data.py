#For handling the user data in a clean-ish and standardized way

class UserData:
    def __init__(self):
        self.personal_info = []
    
    # Takes a python object and returns an object for a cookie
    def serialize(data):
        s = ""
        for group in data:
    
    # Takes an object and returns a python object
    def deserialize(data):
        pass
    
    # Takes a python dictionary representation of our form and returns a python object
    def parse_http_form(formList):
        pass
    
    # Takes a python object and returns a python file descriptor to /static/tmp/<session_id>_<secure_filename>.pdf containing the pdf resume
    def generate_pdf_resume(data):
        pass
