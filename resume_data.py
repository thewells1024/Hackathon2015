# For handling the user data in a clean-ish and standardized way
# coding=UTF-8

import json

def dict_count(fd, string, search):
    return len([x for x in fd.keys() if x.find(string) >= 0 and x.find(search) >= 0])

def parse_dict(fd, string, search, keys):
    temp = []
    for i in range(dict_count(fd, string, search)):
        print str(fd[string + str(i) + search])
        if str(fd[string + str(i) + search]) != "[u'']":
            temp.append({})
            for k in keys:
                try:
                    temp[i][k] = u''.join(fd[string+str(i)+k])
                except KeyError:
                    continue
    return temp

def serialize_dict(d):
    s = "{"
    for key in d.keys():
        if len(u''.join(d[key])) == 0:
            continue
        s += key + ":" + u''.join(d[key]) + ".^."
    s += "}"
    return s

def serialize_lod(string, d):
    s = ""
    s += string + "<"
    for e in d:
        s += serialize_dict(e) + "^.^"
    s = s[0:len(s) - 3]
    s += ">"
    return s

def deserialize_dict(string):
    dict = {}
    dict_list = string[string.find("{") + 1:string.find("}")].split(".^.")
    for pair in dict_list:
        semi = pair.find(":")
        if semi != -1:
            dict[pair[:semi]] = pair[semi + 1:]
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
            s = s[:len(s) - 1]
            formData["skills"] = s
    return UserData(formData)

def validate(data):
    try:
        for info in data.personal_info:
            if info == "" or info == "[u'']":
                return False
        for schoolInfo in data.education[0]:
            if schoolInfo != "gpa" and (schoolInfo == "" or schoolInfo == "[u'']"):
                return False
        if data.skills[0] == "" or data.skills[0] == "[u'']":
            return False
        return True
    except KeyError:
        return False

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
        self.skills = [skill for skill in ''.join(fd['skills']).split('\n')]
    
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
    formDict = {"name":"Kent Kawahara", "phone":"(951) 314-1525", "location":"San Luis Obispo, CA", "email":"kkawahar@calpoly.edu", "school0name": "Cal Poly", "school0location": "SLO", "school0degree": "BS Computer Engineering", "school0gpa": "4.0", "school0status": "in progress", "school0year": "2018", "job0position": "Counselor in Training", "job0employer": "Camp Conrad-Chinnock", "job0location": "Angelus Oaks, CA", "job0time_period": "2014", "job0comments": "Worked to provide kids with type 1 diabetes a good camping experience\nResponsibilities included serving food, assisting in activity areas such as the pool and the crafts area\nAssisted counselors in checking the campers blood glucoses\nTaught me about the work that it takes to run an organized program.", "project0title": "Card Game", "project0summary": "Worked in a small team to implement a card game in Java.", "project0comments": "Gained experience developing software in a small group setting \nStrengthen knowledge of Git.", "skills": "Knowledge of Microsoft Office and Apple equivalents.\nA working knowledge of Java, C++, Git, HTML, CSS, and PHP.\nExperience with C, Objective-C, JavaScript, Swift, Python, and BASH script.\nModerate knowledge of French."}
    from resume_pdf import generate_pdf_from_data as g
    u = UserData(formDict)
    my_str = u.serialize()
    print my_str + "\n\n\n"
    uPrime = deserialize(my_str)
    print uPrime.serialize()
    print g(u)
