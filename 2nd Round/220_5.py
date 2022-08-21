class FinalQ:
    def print(self,array,idx):
      if(idx<len(array)):
        profit = self.calcProfit(array[idx]) #TO DO
        print('Investment: ' + str(array[idx]) + '; Profit: ' + str(profit))
    def calcProfit(self,investment):
        profit = 0
        if investment - 25000 <= 0:
            return 0
        else:
            investment -= 25000
            if investment > 75000:
                profit = 75000*0.45
                investment -= 75000
                profit += (investment*0.8)
            else:
                profit = (investment * 0.45)
        return profit
                
    
#Tester
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)
f.print(array,1)
f.print(array,2)
f.print(array,3)
