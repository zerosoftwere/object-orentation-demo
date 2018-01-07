class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        if age < 0:
            raise ValueError('Age cannot be less than 0')  
        self.age = age

    def __repr__(self):
        return '[name: {}, age: {}]'.format(self.name, self.age)