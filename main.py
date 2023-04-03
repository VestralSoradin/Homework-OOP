#finished_courses = ['Вводный модуль', 'Основы языка программирования']
#courses_in_progress = ['Git', 'ООП и работа с API']
#attached_courses = ['Вводный модуль', 'Основы языка программирования', 'Git', 'ООП и работа с API']
#grade = []
#grades = []
#for course, grad in zip(courses_in_progress, grade):
#    gradeses = {course: grad}
#    grades.append(gradeses)

#print(grades)


def count_average(grades):

    pass



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.ever_grade = []


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
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.ever_grade = []

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.ever_grade < other.ever_grade




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

student_2 = Student('Анастасия', 'Сорша', 'Ж.')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['ООП и работа с API']
student_2.finished_courses += ['Вводный модуль']
student_2.finished_courses += ['Основы языка программирования']

reviewer_1 = Reviewer('Евгений', 'Андропов')
reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['ООП и работа с API']

reviewer_2 = Reviewer('Василий', 'Свиридов')
reviewer_2.courses_attached += ['Git']
reviewer_2.courses_attached += ['ООП и работа с API']

lecturer_1 = Lecturer('Максим', 'Суржевский')
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['ООП и работа с API']

lecturer_2 = Lecturer('Павел', 'Катаров')
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['ООП и работа с API']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'VB', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_2, 'C++', 10)

student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'VB', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'VB', 8)
student_2.rate_hw(lecturer_2, 'Python', 9)

print(student_1)
print(reviewer_1)
print(lecturer_1)
print(student_1 > student_2)
print(lecturer_1 > lecturer_2)




#average_rating_student_course([student_1, student_2], 'Python')

#average_rating_lecturer_course([lecturer_1, lecturer_2], 'Python')
