class Student:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.courses = []
        
    def advise(self, *courses):
        for i in courses:
            self.courses.append(i)
        print(self.name + ', you have taken ' + str(3.0*len(self.courses)) + ' credits')
        print('List of courses:', end=' ')
        for i in self.courses:
            print(i, end=', ')
        print()
        print('Status:', end=' ')
        if len(self.courses) < 3:
            print('You have to take at least ' + str(3-len(self.courses)) + ' more courses')
        elif len(self.courses) > 4:
            print('You have to drop at least ' + str(len(self.courses) - 4) + ' courses')
        
    def details(self):
        return 'Name: ' + self.name + '\nID: ' + self.id + '\nDepartment: ' + self.department
        
        
s1 = Student('Alice','20103012','CSE')
s2 = Student('Bob', '18301254','EEE')
s3 = Student('Carol', '17101238','CSE')
print('##########################')
print(s1.details())
print('##########################')
print(s2.details())
print('##########################')
s1.advise('CSE110', 'MAT110', 'PHY111')
print('##########################')
s2.advise('BUS101', 'MAT120')
print('##########################')
s3.advise('MAT110', 'PHY111', 'ENG102',
'CSE111', 'CSE230')
