#finished_courses = ['Вводный модуль', 'Основы языка программирования']
#courses_in_progress = ['Git', 'ООП и работа с API']
#attached_courses = ['Вводный модуль', 'Основы языка программирования', 'Git', 'ООП и работа с API']
#grade = []
#grades = []
#for course, grad in zip(courses_in_progress, grade):
#    gradeses = {course: grad}
#    grades.append(gradeses)

#print(grades)


#def count_average(grades):

    #pass



class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []
        self.ever_grade = []
        self.student_list.append(self)


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in \
                self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за ' \
                  f'домашние задания: {self.ever_grade}\nКурсы в процессе ' \
                  f'изучения: {", ".join(self.courses_in_progress)}\nЗавершённый ' \
                  f'курсы: {", ".join(self.finished_courses)}'
            return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.ever_grade < other.ever_grade

    def calc_ever(self):
        self.grades = sum(self.grades)/len(self.grades)
        #print(self.grades)
        return self.grades

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.ever_grade = []
        self.lecturer_list.append(self)



    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ever_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.ever_grade < other.ever_grade

    def calc_ever(self):
        self.grades = sum(self.grades)/len(self.grades)
        #print(self.grades)
        return self.grades




class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in \
                self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)

#finished_courses = ['Вводный модуль', 'Основы языка программирования']
#courses_in_progress = ['Git', 'ООП и работа с API']
student_1 = Student('Александр', 'Воршак', 'М.')
student_1.courses_in_progress += ['Git']
student_1.courses_in_progress += ['ООП и работа с API']
student_1.finished_courses += ['Вводный модуль']
student_1.finished_courses += ['Основы языка программирования']
student_1.grades += [8, 9, 7]
student_1.grades += [10, 8, 9]
student_1.ever_grade = student_1.calc_ever()

#print(student_1.ever_grade)

student_2 = Student('Анастасия', 'Сорша', 'Ж.')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['ООП и работа с API']
student_2.finished_courses += ['Вводный модуль']
student_2.finished_courses += ['Основы языка программирования']
student_2.grades += [6, 10, 7]
student_2.grades += [9, 6, 8]
student_2.ever_grade = student_2.calc_ever()

#print(student_2.ever_grade)

reviewer_1 = Reviewer('Евгений', 'Андропов')
reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['ООП и работа с API']

reviewer_2 = Reviewer('Василий', 'Свиридов')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['ООП и работа с API']

lecturer_1 = Lecturer('Максим', 'Суржевский')
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['ООП и работа с API']
lecturer_1.grades += [9, 10, 7]
lecturer_1.grades += [8, 10, 10]
lecturer_1.ever_grade = lecturer_1.calc_ever()

#print((lecturer_1.ever_grade))

lecturer_2 = Lecturer('Павел', 'Катаров')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['ООП и работа с API']
lecturer_2.grades += [9, 10, 10]
lecturer_2.grades += [8, 10, 8]
lecturer_2.ever_grade = lecturer_2.calc_ever()

#print((lecturer_2.ever_grade))

stud_grade_list = [student_1.grades, student_2.grades]

#ever_grade1 = sum(student_1.grades)/len(student_1.grades)
#ever_grade2 = sum(student_2.grades)/len(student_2.grades)


#student_1.ever_grade = ever_grade1
#student_2.ever_grade = ever_grade2

#ever_grade3 = sum(lecturer_1.grades)/len(lecturer_1.grades)
#ever_grade4 = sum(lecturer_2.grades)/len(lecturer_2.grades)

#lecturer_1.ever_grade = ever_grade3
#lecturer_2.ever_grade = ever_grade4

#student_list = [student_1, student_2]

#for i in student_list:
    #if int in i:
        #print('t')


print(student_1)
print(reviewer_1)
print(lecturer_1)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)
