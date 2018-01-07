from person import Person

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    def set_major(self, major):
        self.major = major
    
    def __repr__(self):
        return '{}[major: {}]'.format(super().__repr__(), self.major)


class PostgradStudent(Student):
    def __init__(self, name, age, major):
        super().__init__(name, age, major)
        self.thesis = None

    def set_thesis(self, thesis):
        self.thesis = thesis

    def __repr__(self):
        return '{}[thesis: {}]'.format(super().__repr__(), self.thesis)