import numpy as np
from domains.Student import Student
from domains.Course import Course
from domains.Mark import Mark


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


def choose_course_to_mark(course_list, student_list):
    while True:
        choice = input("Enter any key or 'exit' to not entering mark: ")
        if choice == 'exit':
            break
        course_id = Mark.select_course(course_list)
        Mark_of_a_course(course_id, student_list)


def calculate_GPA(student_list):
    chosen_student = input("Enter student ID you want to calculate GPA: ")
    for student in student_list:
        if chosen_student == student['Student ID']:
            total_credit = 0
            total_point = 0
            course_ID = list(student['marks'].keys())
            data = list(student['marks'].values())
            arrayPoints = np.array(data)
            for i in range(len(arrayPoints)):
                print(f"This is the point of the course {course_ID[i]}: {arrayPoints[i]}")
                credit = int(input(f"Enter number of credits you want of the course for the students {student['Student ID']}: "))
                total_credit += credit
                points = arrayPoints[i] * credit
                total_point += points
            gpa = float(total_point) / total_credit
            return gpa
    print("There is not this student ID in the list")





