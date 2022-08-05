class StudentDatabase:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []
        
    def calculateGPA (self, res, semester):
        self.semester = semester
        courses = []
        curSemester = dict()
        cgpa = 0
        totalCredit = 0
        for i in res:
            a = i.split(': ')
            courses.append(a[0])
            totalCredit += 3
            cgpa += float(a[1])*3
        cgpa /= totalCredit
        self.cgpa = cgpa
        self.grades 
        curSemester[semester] = courses
        self.grades.append([curSemester, cgpa])
        
    def printDetails(self):
        print('Name: ' + self.name)
        print('ID: ' + self.id)
        for i in self.grades:
            for j in i[0]:
                print('Courses taken in ' + j + ':')
                for k in i[0][j]:
                    print(k)
                print('GPA: ' + str(i[1]))
     

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 
'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 
'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
