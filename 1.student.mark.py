numberOfStudent = 0
numberOfCourse = 0
students_list = list()
student_info = dict()
course_list = list()
course_infor = dict()


def number_student():
    global numberOfStudent
    numberOfStudent = int(input("Enter number of students:"))


def student_infor():
    global student_info
    global students_list
    for student in range(numberOfStudent):
        student_info = {
            "id": input("Enter ID: "),
            "name":  input("Enter name: "),
            "DoB":  input("Enter DoB: ")
        }
        students_list.append(student_info)


def print_student_list():
    for student in students_list:
        print(student)


def number_course():
    global numberOfCourse
    numberOfCourse = int(input("Enter number of course: "))


def course_information():
    global course_infor
    global course_list
    for course in range(numberOfCourse):
        course_infor = {
            "id": input("Enter ID of the course: "),
            "nameOfCourse": input("Enter the name of the course: ")
        }
        course_list.append(course_infor)


def course_mark_input():
    global students_list
    global student_info
    course = input("Select the course: ")
    for student in students_list:
        student.update({course: None})
        notification = f"Enter the mark of {student['id']} {student['name']}: "
        mark = float(input(notification))
        student[course] = mark


def start_program():
    number_student()
    number_course()
    student_infor()
    print_student_list()
    course_information()
    course_mark_input()
    print_student_list()


start_program()
