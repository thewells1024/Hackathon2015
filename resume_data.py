# For handling the user data in a clean-ish and standardized way

"""
personal_info         dict(str:str)                     = {"name": "John Smith", "phone": "(123) 456-7890", "location": "Canada", "email": "jsmith@calpoly.edu"}

education             list(dict(str:str))             = [ {"school_name": "Cuesta", "degree": "BS Things", "status": "in progress", "year": "2018"} ]

work_experience     list(dict(str:str))             = [ {"employer": "Stringy.com", "location": "Anytown, USA", "time period": "2013-2014", "comments": ["str1", "str2", "str3"]}]

projects             list(dict(str:str))             = [ {"title": "Resume Website", "summary": "Text Block", "comments": ["a thing", "moar thing", "even more thang"]} ]

skills                 list(str)                         = ["A string", "Another string", "A third string", "Fourth string quarterback"]

"""
school0name
01234567890

def dict_count(fd, string, search):
    return len([x for x in fd.keys() if x[:6] == string and x[7:] == search])

def dict_sketchy_shit(fd, string, search, keys):
    temp = []
    for i in range(dict_count(fd, string, search)):
        temp.append({})
        for k in keys:
            temp[i][k] = fd[string+str(i)+k]
    return temp

def serialize_dict(dict):
    s = "{ "
    for key in dict.keys():
        s += "|" + key + ":" + dict[key] + "| "
    s += "} "
    return s
    

class UserData:
    def __init__(self, fd):
        pi = {}
        pi['name'] = fd['name']
        pi['phone'] = fd['phone']
        pi['location'] = fd['location']
        pi['email'] = fd['email']
        self.personal_info = pi

        self.education = dict_sketchy_shit(fd, "school", "name", ["name", "degree", "status", "year"])

        self.work_experience = dict_sketchy_shit(fd, "job", "employer", ["employer", "location", "time period", "comments"])

        self.projects = dict_sketchy_shit(fd, "project", "title", ["title", "summary", "comments"])
        
        self.skills = [skill for skill in fd['skills'].split("\n")]
    
    # Takes a python object and returns an object for a cookie
    def serialize(data):
        s = ""
        s += "Personal_Info { " + serialize_dict(self.personal_info) + "\n"
        s += "Education < "
        for institute in self.education:
            s += serialize_dict(institute) + ", "
        s = s[0:len(s) - 3]
        s += " >\n"
        s += "Work Experience < "
        for exp in self.work_experience:
            s += serialize_dict(exp) + ", "
        s = s[0:len(s) - 3]
        s += " >\n"
        s += "Projects < "
        for proj in self.projects:
            s += serialize(proj) + ", "
        s = s[0:len(s) - 3]
        s += " >\n"
        s += "Skills < "
        for skill in self.skills:
            s += skill + ", "
        s = s[0:len(s) - 3]
        s += " >\n"
    
    # Takes an object and returns a python object
    def deserialize(data):
        pass
    
    # Takes a python object and returns a python file descriptor to /static/tmp/<session_id>_<secure_filename>.pdf containing the pdf resume
    def generate_pdf_resume(data):
        pass
