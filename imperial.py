students = [
    {'name': 'Sauda', 'major': 'comp-sci'},
    {'name': 'Chuchu', 'major': 'comp-sci'},
]

def set_student_name(student, name):
    student['name'] = name

def set_student_major(student, major):
    student['major'] = major

def str_student(student):
    return '[name: {}, major: {}]'.format(student['name'], student['major']);


set_student_major(students[0], 'bio-sci')

print (students)