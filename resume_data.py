# For handling the user data in a clean-ish and standardized way

"""
personal_info 		dict(str:str) 					= {"name": "John Smith", "phone": "(123) 456-7890", "location": "Canada", "email": "jsmith@calpoly.edu"}

education 			list(dict(str:str)) 			= [ {"school_name": "Cuesta", "degree": "BS Things", "status": "in progress", "year": "2018"} ]

work_experience 	list(dict(str:str)) 			= [ {"employer": "Stringy.com", "location": "Anytown, USA", "time period": "2013-2014", "comments": ["str1", "str2", "str3"]}]

projects 			list(dict(str:str)) 			= [ {"title": "Resume Website", "summary": "Text Block", "comments": ["a thing", "moar thing", "even more thang"]} ]

skills 				list(str) 						= ["A string", "Another string", "A third string", "Fourth string quarterback"]

"""

def dict_count(fd, string):
	return len([x for x in fd.keys() if x.find(string) >= 0])

def dict_sketchy_shit(fd, string, keys):
	temp = []
	for i in range(dict_count(fd, string)):
		temp.append({})
		for k in keys:
			temp[i][k] = fd[string+str(i)+k]
	return temp

class UserData:
    def __init__(self, fd):
		pi = {}
		pi['name'] = fd['name']
		pi['phone'] = fd['phone']
		pi['location'] = fd['location']
		pi['email'] = fd['email']
        self.personal_info = pi

		self.education = dict_sketchy_shit(fd, "school", ["name", "degree", "status", "year"])

		self.work_experience = dict_sketchy_shit(fd, "job", ["employer", "location", "time period", "comments"])

		self.projects = dict_sketchy_shit(fd, "project", ["title", "summary", "comments"])
		
		self.skills = [skill for skill in fd['skills'].split("\n")]
    
    # Takes a python object and returns an object for a cookie
    def serialize(data):
        s = ""
    
    # Takes an object and returns a python object
    def deserialize(data):
        pass
    
    # Takes a python object and returns a python file descriptor to /static/tmp/<session_id>_<secure_filename>.pdf containing the pdf resume
    def generate_pdf_resume(data):
        pass
