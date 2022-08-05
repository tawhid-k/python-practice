class Student:
    def __init__(self, name = None, department = None):
        if name == None and department == None:
            print('Student name and department need to be set')
        elif department == None:
            print('Department for '+name+' needs to be set')
        else:
            print(name + ' is from ' + department + ' department')
        self.name = name
        self.department = department
        self.courses = []
        
    def update_name(self, name):
        self.name = name
        
    def update_department(self, department):
        self.department = department
        
    def enroll(self, *courses):
        for i in courses:
            self.courses.append(i)
            
    def printDetail(self):
        print('Name: ' + self.name)
        print('Department: ' + self.department)
        print(self.name + ' enrolled ' + str(len(self.courses)) + " course(s):")
        for i in self.courses:
            print(i, end=', ')
        
s1 = Student()
print('=========================')
s2 = Student('Carol')
print('=========================')
s3 = Student('Jon', 'EEE')
print('=========================')
s1.update_name('Bob')
s1.update_department('CSE')
s2.update_department('BBA')
s1.enroll('CSE110', 'MAT110', 'ENG091')
s2.enroll('BUS101')
s3.enroll('MAT110', 'PHY111')
print('###########################')
s1.printDetail()
print('=========================')
s2.printDetail()
print('=========================')
s3.printDetail()
    
    