from OOP.task1.Student import Student


if __name__ == '__main__':
    s_1 = Student('Ivan', 'Soloviev', 22)
    s_1.study_course('Python', 'Java')

    s_2 = Student('Ivan', 'Petrov', 23)
    s_2.study_course('Python', 'SQL')

    s_3 = Student('Oleg', 'Soloviev', 21)
    s_3.study_course('Java', 'Python', 'SQL')

    s_1.enter_job('Python', 'Java', 'English')
    s_2.enter_job('Python', 'Java', 'English')
    s_3.enter_job('Python', 'Java', 'English')

