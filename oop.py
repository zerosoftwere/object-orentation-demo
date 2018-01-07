from student import Student, PostgradStudent

students = [
    Student('Sauda', 24, 'comp-sci'),
    PostgradStudent('Chuchu', 12, 'comp-sci')
]

students[1].set_thesis('Advance Web Infastructor')

print(students)