numberOfStudent = 0
numberOfCourse = 0
students_list = list()
student_info = dict()


def number_student():
    global numberOfStudent
    numberOfStudent = int(input("Enter number of students:"))


def student_infor():
    global student_info
    global students_list
    for i in range(numberOfStudent):
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


number_student()
print(f"number of student: {numberOfStudent}")
number_course()
print(f"Number of course: {numberOfCourse}")
student_infor()
print_student_list()

