class Student:
    def __init__(self, id: str, name: str, DoB: str):
        # Assign to self object
        self.__id = id
        self.__name = name
        self.__DoB = DoB

    def student_number():
        student_num = int(input("Enter the number of students: "))
        return student_num

    def student_add(self, student_list):
        student_info = {
            "Student ID": self.__id,
            "Student Name": self.__name,
            "Student DoB": self.__DoB,
            "marks": {}
        }
        student_list.append(student_info)
        return student_list

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

    def display_student_list(student_list):
        print("This is a student list: ")
        for student in student_list:
            print(f"{student['Student ID']:<8} {student['Student Name']:<20}")


class Course:
    def __init__(self, idCourse: int, nameCourse: str):
        # Assign to self object
        self.__id_course = idCourse
        self.__name_course = nameCourse
        self.__mark_list = dict()

    def course_number():
        course_num = int(input("Enter the number of courses: "))
        return course_num

    def course_add(self, course_list):
        course_info = {
            "Course ID": self.__id_course,
            "Course Name": self.__name_course,
        }
        course_list.append(course_info)
        return course_list

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


class Mark:
    def select_course(course_list):
        for course in course_list:
            print(course)
        course_id = input("Enter one of the ID from the course above: ")
        return course_id

    def input_mark(courseId, student_list):
        students = student_list
        print(f"Enter mark of the course {courseId} for students")
        for student in students:
            mark = float(input(f"- Enter the mark of student: {student['Student ID']}-{student['Student Name']}: "))
            student['marks'][courseId] = mark

    def display_mark(courseId, student_list):
        print(f"This is the mark for the course {courseId}")
        for student in student_list:
            print(f"{student['Student ID']:<8} {student['Student Name']:<20} {student['marks'][courseId]:<10}")


def inputStudentInfor(student_num, student_list):
    """Enter the information of each student"""
    for i in range(student_num):
        student_ID = input("Enter the ID of the Student: ")
        student_name = input("Enter the name of the Student: ")
        student_DoB = input("Enter the DoB of the Student: ")
        new_student = Student(student_ID, student_name, student_DoB)
        new_student.student_add(student_list)


def inputCourseInfor(course_num, course_list):
    """Enter the information of each student"""
    for i in range(course_num):
        course_ID = input("Enter the ID of the Course: ")
        course_name = input("Enter the Name of the Course: ")
        new_course = Course(idCourse=course_ID, nameCourse=course_name)
        new_course.course_add(course_list)


def Mark_of_a_course(course_id, student_list):
    Mark.input_mark(course_id, student_list)
    Mark.display_mark(course_id, student_list)


def start_program():
    student_list = list()
    course_list = list()

    student_num = Student.student_number()
    inputStudentInfor(student_num, student_list)
    Student.display_student_list(student_list)

    course_num = Course.course_number()
    inputCourseInfor(course_num, course_list)

    course_id = Mark.select_course(course_list)
    Mark_of_a_course(course_id, student_list)


start_program()