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
