import math


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
            mark = math.floor(mark)
            student['marks'][courseId] = mark

    def display_mark(courseId, student_list):
        print(f"This is the mark for the course {courseId}")
        for student in student_list:
            print(f"{student['Student ID']:<8} {student['Student Name']:<20} {student['marks'][courseId]:<10}")
