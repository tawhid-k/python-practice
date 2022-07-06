#ass-4 prob-9
class Batsman:
    def __init__(self,name=None,run=None,ball=None):
        self.name = name
        self.run = run
        self.ball = ball
        if (type(name) == int):
            self.ball = self.run
            self.run = self.name
            self.name = "New Batsman"
        
    def battingStrikeRate(self):
        self.StrikeRate = self.run/(self.ball) * 100
        return self.StrikeRate
    def setName(self,name):
        self.name = name
    def printCareerStatistics(self):
        self.battingStrikeRate()
        print(f"Name: {self.name}")
        print(f"Runs Scored: {self.run} , Balls Faced: {self.ball}")
        
b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())