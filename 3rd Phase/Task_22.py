class Hotel:
    def __init__(self, name):
        self.name = name
        self.stuff = []
        self.guest = []
        self.stuffId = 0
        self.guestId = 0
        
    def addStuff(self, name, age, phone = '000'):
        self.stuffId += 1
        self.stuff.append([self.stuffId, name, age, phone])
        print('Staff with ID ' + str(self.stuffId) + ' is added')
    
    def addGuest(self, name, age, phone = '000'):
        self.guestId += 1
        self.guest.append([self.guestId, name, age, phone])
        print('Guest With ID ' + str(self.guestId) + ' is created')
        
    def getGuestById(self, id):
        for i in self.guest:
            if i[0] == id:
                print('Guest ID: ' + str(str(i[0])))
                print('Name: ' + i[1])
                print('Age: ' + str(i[2]))
                print('Phone no: ' + str(i[3]))
                return
            
    def getStuffById(self, id):
        for i in self.stuff:
            if i[0] == id:
                print('Staff ID: ' + str(i[0]))
                print('Name: ' + i[1])
                print('Age: ' + str(i[2]))
                print('Phone no: ' + str(i[3]))
                return
            
    def allGuest(self):
        print('All Guest:')
        print('Number of Guest: ' + str(self.guest))
        for i in self.guest:
            print(f'Guest ID: {i[0]} Name: {i[1]} Age: {i[2]} Phone no: {i[3]}')
        
    def allStaffs(self):
        print('All Staffs:')
        print('Number of Staff: ' + str(self.guest))
        for i in self.stuff:
            print(f'Staff ID: {i[0]} Name: {i[1]} Age: {i[2]} Phone no: {i[3]}')

h = Hotel("Lakeshore")
h.addStuff( "Adam", 26)
print("=================================")
print(h.getStuffById(1))
print("=================================")
h.addGuest('Carol',35,'123')
print("=================================")
print(h.getGuestById(1))
print("=================================")
h.addGuest("Diana", 32, '431')
print("=================================")
print(h.getGuestById(2))
print("=================================")
h.allStaffs()
print("=================================")
h.allGuest()
