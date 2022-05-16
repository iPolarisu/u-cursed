import json
from courses import coursembed as ce

# reads active courses
def load_coursesData():
    with open('coursesData.json', 'r') as f:
       coursesData = json.load(f)
    return coursesData

# updates coursesData
def save_coursesData(coursesData):
    with open('coursesData.json', 'w') as f:
       json.dump(coursesData, f)

# adds server to coursesData
def addServerData(server_id):
    coursesData = load_coursesData()
    coursesData[server_id] = []
    save_coursesData(coursesData)

# remove server from coursesData
def removeServerData(server_id):
    coursesData = load_coursesData()
    del coursesData[server_id]
    save_coursesData(coursesData)

# adds course data to coursesData
def addCourseData(course, server_id):
    coursesData = load_coursesData()
    coursesData[server_id].append(course)
    save_coursesData(coursesData)

# removes course from coursesData
def removeCourseData(active_course, server_id):
    coursesData = load_coursesData()
    coursesData[server_id].remove(active_course)
    save_coursesData(coursesData)

# returns boolean for course in server data
def courseInServerData(active_course, server_id):
    coursesData = load_coursesData()
    if active_course in coursesData[server_id]:
        return True
    else:
        return False

# returns list of active courses
def activeCourses(server_id):
    coursesData = load_coursesData()
    courses = ''
    for course in coursesData[server_id]:
        courses += f'{course} '
    return courses
    