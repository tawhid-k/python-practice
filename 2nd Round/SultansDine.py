class SultansDine:
    branch = dict()
    sell = 0
    def __init__(self, branch):
        self.name = branch
        SultansDine.branch[self.name] = 0
    
    def branchInformation(self):
        print('Branch Name: ' + self.name)
        print('Branch Sell: ' + str(SultansDine.branch[self.name]) + ' Taka')
        
    def sellQuantity(self, q):
        self.quantity = q
        branchSell = 0
        if q < 10:
            branchSell = q * 300
        elif q < 20:
            branchSell = q * 350
        else:
            branchSell = q * 400
        SultansDine.branch[self.name] = branchSell
        SultansDine.sell += branchSell
        
    @staticmethod 
    def details():
        print('Total number of branch(s): ' + str(len(SultansDine.branch)))
        print('Total Sell: ' + str(SultansDine.sell))
        for branch in SultansDine.branch:
            per = (SultansDine.branch[branch] / SultansDine.sell) * 100
            print('Branch Name: ' + branch, end=', ')
            print('Branch Sell: ' + str(SultansDine.branch[branch]) + ' Taka')
            print('Branch consists of total sell\'s: ' + str(format(per, ".2f")) + '%')
            
SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()