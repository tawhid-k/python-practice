class Exam:
   def __init__(self,marks):
      self.marks = marks
      self.time = 60
   def examSyllabus(self):
      return "Maths, English"
   def examParts(self):
      return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
    def __init__(self, marks, time, *sub):
        self.time = time
        self.sub = sub
        super().__init__(time)
    def __str__(self):
        return('Marks: ' + str(self.marks) + ' Time: ' + str(self.time) + ' minutes Number of Parts: ' + str(len(self.sub)+2))
    def examSyllabus(self):
        s = super().examSyllabus()
        for i in self.sub:
            s += ', ' + i
        return s
    def examParts(self):
        s = super().examParts()
        c = 3
        for i in self.sub:
            s += 'Part ' + str(c) + ' - ' + i + '\n'
            c += 1
        return s

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())