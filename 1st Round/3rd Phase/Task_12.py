class TaxiLagbe:
    def __init__ (self, no, area):
        self.no = no
        self.area = area
        self.passenger = []
        self.totalFare = 0
    
    def addPassenger(self, *passenger):
        for n in passenger:
            if len(self.passenger) == 4:
                print('Taxi Full! No more passengers can be added')
                return
            name = ''
            i = 0
            # Walker_100
            # 
            while n[i] != '_':
                name += n[i]
                i += 1
            self.passenger.append(name)
            print('Dear ' + name + '! Welcome to TaxiLagbe.')
            i += 1
            strFare = ''
            while i < len(n):
                strFare += n[i]
                i += 1
            fare = int(strFare)
            self.totalFare += fare
    
    def printDetails(self):
        print('Trip info for Taxi number: ' + self.no)
        print('This taxi can cover only ' + self.area + " area")
        print('Total passengers: ' + str(len(self.passenger)))
        print('Passenger list:')
        for i in self.passenger:
            print(i, end=', ')
        print()
        print('Total collected fare: ' + str(self.totalFare) + " Taka")

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200')
taxi1.addPassenger('Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115')
taxi2.addPassenger('Parker_215')
print('-------------------------------')
taxi2.printDetails()

        