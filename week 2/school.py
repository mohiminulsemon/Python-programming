class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id


    def __repr__(self) -> str: # __repr__ is used to print the object itself as a string
        return f'Student name: {self.name}, clss: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, subject: {self.subject}, id: {self.id}'

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else: 
            id = len(self.students) + 1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
    def __repr__(self) -> str:
        print('welcome to ', self.name)
        print('-----------Our Teachers-----------')
        for teacher in self.teachers:
            print(teacher)
        print('-----------Our Students-----------')
        for student in self.students:
            print(student)
        return 'done'
    

# alia = Student('alia', 9, 1)
# print(alia)
# ranbeer = Teacher('ranbeer', 'math', 101)
# print(ranbeer)

phitron = School('phitron')
phitron.enroll('alia', 5500)
phitron.enroll('rani',8000)
phitron.enroll('asihwariaya',7000)
phitron.enroll('vaijan',90000)

phitron.add_teacher('tom cruise', 'DS')
phitron.add_teacher('Decap', 'Algo')
phitron.add_teacher('Aj', 'Database')

print(phitron)