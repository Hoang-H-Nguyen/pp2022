from domains.Student import Student as Student
from domains.Course import Course as Course
from input import *
import shutil, gzip, sys
import pickle


def writeStudent(student_list):
    with open('students.txt', 'a+', encoding='utf-8') as f:
        for student in student_list:
            f.write(f"{student['Student ID']} {student['Student Name']} {student['Student DoB']}\n")

def writeCourse(course_list):
    with open('students.txt', 'a+', encoding='utf-8') as f:
        for course in course_list:
            f.write(f"{course['Course ID']} {course['Course Name']}\n")

def compress(filename_in, filename_out):
    with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
    # Reads the file by chunks to avoid exhausting memory
        shutil.copyfileobj(fin, fout)

def decompress(file):
    with gzip.open(file, "rb") as fin:
        data = fin.read()
        print(f"Decompressed size: {sys.getsizeof(data)}")
        # Decompressed size: 1000033
        print(data)


def pickle_data(file, student_list):
    student_data = open('student', 'wb')
    pickle.dump(student_list, student_data)
    student_data.close()

def unpickle_data(file):
    infile = open(file, 'rb')
    new_list = pickle.load(infile)
    infile.close()
    return new_list

def start_program():
    student_list = list()
    course_list = list()

    student_num = Student.student_number()
    inputStudentInfor(student_num, student_list)
    Student.display_student_list(student_list)
    pickle_data('students.txt', student_list)
    student_list = unpickle_data('student')
    writeStudent(student_list)

    compress('students.txt', 'students_data.dat')
    decompress('students_data.dat')

    course_num = Course.course_number()
    inputCourseInfor(course_num, course_list)
    writeCourse(course_list)
    
    choose_course_to_mark(course_list, student_list)
    gpa = calculate_GPA(student_list)
    print(gpa)

start_program()