import pickle
def pickle(file, student_list):
    student_data = open(file, 'wb')
    pickle.dump(student_list, student_data)
    student_data.close()
