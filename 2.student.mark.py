class Student:
    def __init__(self, id: str, name: str, DoB: str, course=None, mark=0.0):
        # Assign to self object
        self.__id = id
        self.__name = name
        self.__DoB = DoB
        self.__course = course
        self.__mark = mark

    @property
    def get_id(self):
        return self.__id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_DoB(self):
        return self.__DoB

    @property
    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark


class Course:

    def __init__(self, id: str, name: str):
        # Assign to self object
        self.__id = id
        self.__name = name

    @property
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    @property
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
    def __repr__(self):
        return f"(Course:ID: {self.__id}, {self.__name}, )"


student_list = []

student1 = Student("BA10-021", "Nguyen Huy Hoang", "24/07/2001")
student2 = Student("BA10-036", "Truong Tuan Minh", "29/02/2001","CS", 18.00)
student3 = Student("BA10-050", "Dinh Quang Son", "30/10/2001", "Chemistry", 19.00)
student4 = Student("BA10-777", "Hoang Xuan Tuyen", "5/11/2001", "Math", 20.00)

course_list = []
number_of_course = int(input("Enter the number of course: "))

for course in range(number_of_course):
    id_course = input("Type the ID of the course: ")
    name_course = input("Type the name of the course: ")
    course = Course(id_course, name_course)
    course_list.append(course)

