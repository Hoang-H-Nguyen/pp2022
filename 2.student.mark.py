student_list = list()
course_list = list()


class Student:
    def __init__(self, id: str, name: str, DoB: str):
        # Assign to self object
        self.__id = id
        self.__name = name
        self.__DoB = DoB

    def student_number():
        student_num = int(input("Enter the number of students: "))
        return student_num

    def student_add(self):
        student_info = {
            "Student ID": self.__id,
            "Student Name": self.__name,
            "Student DoB": self.__DoB,
        }
        student_list.append(student_info)

    # def print_student_infor():
    #     for student in student_list:
    #         return f"ID: {student.get('Student ID')}, Student name: {student.get('Student Name')}, Student DoB: {student.get('Student DoB')}"

    def __repr__(self):
        return f"ID: {self.__id}, Student name: {self.__name}, Student DoB: {self.__DoB}"

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


class Course:
    def __init__(self, idCourse: int, nameCourse: str):
        # Assign to self object
        self.__id_course = idCourse
        self.__name_course = nameCourse
        self.__mark_list = list()

    def course_number():
        course_num = int(input("Enter the number of courses: "))
        return course_num

    def course_add(self):
        course_info = {
            "Course ID": self.__id,
            "Course Name": self.__name,
        }
        course_list.append(course_info)

    @property
    def get_id(self):
        return self.__id_course

    def set_id(self, id):
        self.__id_course = id

    @property
    def get_name(self):
        return self.__name_course

    def set_name(self, name):
        self.__name_course = name

    def add_mark(self, mark):
        self.__mark_list.append(mark)

    def __repr__(self):
        return f"(Course: ID: {self.__id_course}, name: {self.__name_course})"

    def display_mark(self):
        for student_mark in self.__mark_list:
            print(f"""Student ID: {student_mark.getId()}
                Student name: {student_mark.getName()}
                Student DoB {student_mark.getDoB()}
                Student Mark {student_mark.getMark()}""")


class Mark:
    def __init__(self, studentId, student_name, student_DoB, student_mark):
        self.__id = studentId
        self.__name = student_name
        self.__DoB = student_DoB
        self.__mark = student_mark

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDoB(self):
        return self.__id

    def getMark(self):
        return self.__mark


student_num = Student.student_number()
for i in range(student_num):
    student_ID = input("Enter the ID of the Student: ")
    student_name = input("Enter the name of the Student: ")
    student_DoB = input("Enter the DoB of the Student: ")
    new_student = Student(student_ID, student_name, student_DoB)
    student_list.append(new_student)

course_num = Course.course_number()
for i in range(course_num):
    course_ID = input("Enter the ID of the Course: ")
    course_name = input("Enter the Name of the Course: ")
    new_course = Course(idCourse=course_ID, nameCourse=course_name)
    course_list.append(new_course)
# print(student_list)
# student1 = Student("BA10-021", "Nguyen Huy Hoang", "24/07/2001")
# student1.student_add()
# student2 = Student("BA10-036", "Truong Tuan Minh", "29/02/2001")
# student2.student_add()
# student3 = Student("BA10-050", "Dinh Quang Son", "30/10/2001")
# student3.student_add()
# student4 = Student("BA10-777", "Hoang Xuan Tuyen", "5/11/2001")
# student4.student_add()

for student in student_list:
    print(student.__repr__())

for course in course_list:
    print(course.__repr__())


chosen_course = int(input("Enter the ID of course you want to add mark: "))
for i in range(len(course_list)):
    x = int(course_list[i].get_id)      # Type casting from string to int
    # Compare if the ID of the course and the course you see whether is same
    if chosen_course == x:
        for student in student_list:
            studentMark = float(
                input(f"Enter the mark of the student: {student.get_name}: "))

            new_mark = Mark(student.get_id, student.get_name,
                            student.get_DoB, studentMark)
            course.add_mark(new_mark)

for i in range(len(course_list)):
    print(f"The mark of the course {course_list[i].get_name} is: ")
    course_list[i].display_mark()
