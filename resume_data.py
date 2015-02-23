# For handling the user data in a clean-ish and standardized way

def dict_count(fd, string, search):
    return len([x for x in fd.keys() if x.find(string) >= 0 and x.find(search) >= 0])

def parse_dict(fd, string, search, keys):
    temp = []
    for i in range(dict_count(fd, string, search)):
        temp.append({})
        for k in keys:
            temp[i][k] = fd[string+str(i)+k]
    return temp

def serialize_dict(dict):
    s = "{ "
    for key in dict.keys():
        if len(dict[key]) == 0:
            continue
        s += "|" + key + ":" + dict[key] + "| "
    s += "} "
    return s

def serialize_lod(string, dict):
    s = ""
    s += string + " < "
    for e in dict:
        s += serialize_dict(e) + ", "
    s = s[0:len(s) - 3]
    s += " >\n"
    return s

# Takes a cookie string and returns an instance of UserData
def deserialize(cookie):
    pass

class UserData:
    def __init__(self, fd):
        pi = {}
        pi['name'] = fd['name']
        pi['phone'] = fd['phone']
        pi['location'] = fd['location']
        pi['email'] = fd['email']
        self.personal_info = pi

        self.education = parse_dict(fd, "school", "name", ["name", "location", "degree", "gpa", "status", "year"])

        self.work_experience = parse_dict(fd, "job", "position", ["position", "employer", "location", "time_period", "comments"])

        self.projects = parse_dict(fd, "project", "title", ["title", "summary", "comments"])
        
        self.skills = [skill for skill in fd['skills'].split("\n")]
    
    # Takes a python object and returns an object for a cookie
    def serialize(self):
        s = "Personal_Info " + serialize_dict(self.personal_info) + "\n"
        s += serialize_lod("Education", self.education)
        s += serialize_lod("Work Experience", self.work_experience)
        s += serialize_lod("Projects", self.projects)
        s += "Skills < "
        for skill in self.skills:
            s += skill + ", "
        s = s[0:len(s) - 3]
        s += " >"
        return s

if __name__ == '__main__':
    formDict = {"name":"Kent Kawahara", "phone":"(951) 314-1525", "location":"San Luis Obispo, CA", "email":"kkawahar@calpoly.edu", "school0name": "Cal Poly", "school0location": "SLO", "school0degree": "BS Computer Engineering", "school0gpa": "4.0", "school0status": "in progress", "school0year": "2018", "job0position": "Counselor in Training", "job0employer": "Camp Conrad-Chinnock", "job0location": "Angelus Oaks, CA", "job0time_period": "2014", "job0comments": "Worked to provide kids with type 1 diabetes a good camping experience\nResponsibilities included serving food, assisting in activity areas such as the pool and the crafts area\nAssisted counselors in checking the campers' blood glucoses\nTaught me about the work that it takes to run an organized program.", "project0title": "Card Game", "project0summary": "Worked in a small team to implement a card game in Java.", "project0comments": "Gained experience developing software in a small group setting \nStrengthen knowledge of Git.", "skills": "Knowledge of Microsoft Office and Apple equivalents.\nA working knowledge of Java, C++, Git, HTML, CSS, and PHP.\nExperience with C, Objective-C, JavaScript, Swift, Python, and BASH script.\nModerate knowledge of French."}
    from resume_pdf import generate_pdf_from_data as g
    u = UserData(formDict)
    print u.serialize()
    g(u)
