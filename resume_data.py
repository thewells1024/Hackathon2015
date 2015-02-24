# For handling the user data in a clean-ish and standardized way

import json

def dict_count(fd, string, search):
    return len([x for x in fd.keys() if x.find(string) >= 0 and x.find(search) >= 0])

def parse_dict(fd, string, search, keys):
    temp = []
    for i in range(dict_count(fd, string, search)):
        temp.append({})
        for k in keys:
            temp[i][k] = ''.join(fd[string+str(i)+k])
    return temp

def serialize_dict(d):
    s = "{ "
    for key in d.keys():
        if len(''.join(d[key])) == 0:
            continue
        s += key + ":" + ''.join(d[key]) + ".^."
    s += "}"
    return s

def serialize_lod(string, d):
    s = ""
<<<<<<< HEAD
    s += string + "<"
    for e in dict:
        s += serialize_dict(e) + "^.^"
=======
    s += string + " < "
    for e in d:
        s += serialize_dict(e) + ", "
>>>>>>> 75e3314842b6d3e9f6698a4bf93c949ea45f24b1
    s = s[0:len(s) - 3]
    s += ">"
    return s

def deserialize_dict(string):
    dict = {}
    dict_list = string[string.find("{") + 1:string.find("}")].split(".^.")
    for pair in dict_list:
        semi = pair.find(":")
        if semi != -1:
            dict[pair[:semi]] = pair[semi + 1:len(pair) - 1]
    return dict

def deserialize_lod(string, identifier):
    lasd = {}
    num = 0
    for dict in string[string.find("<") + 1:string.find(">")].split("^.^"):
        temp = deserialize_dict(dict)
        for key in temp.keys():
            lasd[identifier + str(num) +key] = temp[key]
        num += 1
    return lasd

# Takes a cookie string and returns an instance of UserData
def deserialize(cookie):
    formData = {}
    for dataSet in cookie.split("-_-"):
        id = dataSet[:2]
        if id == "Pe":
            temp = deserialize_dict(dataSet)
            for key in temp.keys():
                formData[key] = temp[key]
        elif id == "Ed" or id == "Wo" or id == "Pr":
            identifier = ""
            if id == "Ed":
                identifier = "school"
            elif id == "Wo":
                identifier = "job"
            else:
                identifier = "project"
            temp = deserialize_lod(dataSet, identifier)
            for key in temp.keys():
                formData[key] = temp[key]
        else:
            myList = dataSet[dataSet.find("<") + 1:dataSet.find(">")].split("^.^")
            s = ""
            for item in myList:
                s += item + "\n"
            s[:len(s) - 1]
            formData["skills"] = s
    print formData
    return UserData(formData)
            

class UserData:
    def __init__(self, fd):
        pi = {}
        pi['name'] = ''.join(fd['name'])
        pi['phone'] = ''.join(fd['phone'])
        pi['location'] = ''.join(fd['location'])
        pi['email'] = ''.join(fd['email'])
        self.personal_info = pi
        self.education = parse_dict(fd, "school", "name", ["name", "location", "degree", "gpa", "status", "year"])
        self.work_experience = parse_dict(fd, "job", "position", ["position", "employer", "location", "time_period", "comments"])
        self.projects = parse_dict(fd, "project", "title", ["title", "summary", "comments"])
        self.skills = [skill for skill in ''.join(fd['skills']).split('\r\n')]
    
    # Takes a python object and returns an object for a cookie
    def serialize(self):
        s = "Personal Info" + serialize_dict(self.personal_info) + "-_-"
        s += serialize_lod("Education", self.education) + "-_-"
        s += serialize_lod("Work Experience", self.work_experience) + "-_-"
        s += serialize_lod("Projects", self.projects) + "-_-"
        s += "Skills<"
        for skill in self.skills:
            s += skill + "^.^"
        s = s[0:len(s) - 3]
        s += ">"
        return s
        

if __name__ == '__main__':
    formDict = {u'name':u'Kent Kawahara', u'phone':u'(951) 314-1525', u'location':u'San Luis Obispo, CA', u'email':u'kkawahar@calpoly.edu', u'school0name': u'Cal Poly', u'school0location': u'SLO', u'school0degree': u'BS Computer Engineering', u'school0gpa': u'4.0', u'school0status': u'in progress', u'school0year': u'2018', u'job0position': u'Counselor in Training', u'job0employer': u'Camp Conrad-Chinnock', u'job0location': u'Angelus Oaks, CA', u'job0time_period': u'2014', u'job0comments': u'Worked to provide kids with type 1 diabetes a good camping experience\nResponsibilities included serving food, assisting in activity areas such as the pool and the crafts area\nAssisted counselors in checking the campers blood glucoses\nTaught me about the work that it takes to run an organized program.', u'project0title': u'Card Game', u'project0summary': u'Worked in a small team to implement a card game in Java.', u'project0comments': u'Gained experience developing software in a small group setting \nStrengthen knowledge of Git.', u'skills': u'Knowledge of Microsoft Office and Apple equivalents.\nA working knowledge of Java, C++, Git, HTML, CSS, and PHP.\nExperience with C, Objective-C, JavaScript, Swift, Python, and BASH script.\nModerate knowledge of French.'}
    from resume_pdf import generate_pdf_from_data as g
    u = UserData(formDict)
    my_str = u.serialize()
    print my_str
    uPrime = deserialize(my_str)
    print uPrime.serialize()
    g(u)
