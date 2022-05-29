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
