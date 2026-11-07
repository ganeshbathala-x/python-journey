class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
    def add_student(self,student):
        self.students.append(student)
    def __contains__(self,student):
        return student in self.students

course=Course("python")
course.add_student("ramu")
course.add_student("ravi")
print("ramu"in course)
print("raju"in course)