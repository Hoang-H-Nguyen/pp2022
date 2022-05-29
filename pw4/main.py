from domains.Student import Student as Student
from domains.Course import Course as Course
from input import *


def start_program():
    student_list = list()
    course_list = list()

    student_num = Student.student_number()
    inputStudentInfor(student_num, student_list)
    Student.display_student_list(student_list)

    course_num = Course.course_number()
    inputCourseInfor(course_num, course_list)
    choose_course_to_mark(course_list, student_list)
    gpa = calculate_GPA(student_list)
    print(gpa)

start_program()
