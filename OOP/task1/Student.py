class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.courses = ['English']

    def study_course(self, *args):
        self.courses.extend(args)

    def enter_job(self, *args):
        if set(self.courses).issubset(set(args)) or set(args).issubset(set(self.courses)):
            print('Студент', self.name, 'принят на работу')
        else:
            print('Увы, вы нам не подходите')






