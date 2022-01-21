import cPickle as pickle

class car():
    def __init__(self, vehID, vehSize, reg):
        self.vehID = vehID
        self.vehSize = vehSize
        self.reg = reg
    
    def getID(self):
        return self.vehID
    
    def getSize(self):
        return self.vehSize

    def getReg(self):
        return self.reg

    def setID(self, x):
        self.vehID = x
    
    def setSize(self, x):
        self.vehSize = x

    def setReg(self, x):
        self.reg = x

Cars = []

Cars.append(car("2345", "12345", 1000))
Cars.append(car("123","54321", 900))
Cars.append(car("120", "42314", 1200))


for c in Cars:
    print(c.getID())

CarFile = open("Cars.dat", "wb")
for i in range(3):
    pickle.dump(Cars[i], CarFile)

CarFile.close()

CarFile = open("Cars.dat", "rb")

Cars2 = []
for i in range(3):
    Cars2.append(pickle.load(CarFile))

CarFile.close()

print()
print()
print("Sequential file access")
for i in range(0,3):
    print(Cars2[i].getID())

print()
print()
print("Random file access")

CarFile2 = open("CarsHashed.dat", "ab")
Address = hash(Cars[2].vehID) 
CarFile2.seek(Address)
pickle.dump(Cars[2], CarFile2)

CarFile2.close()

CarFile2 = open("CarsHashed.dat", "rb")
Address = hash(Cars[2].vehID)
CarFile2.seek(Address)

ThisCar = car("","","")
ThisCar = pickle.load(CarFile2)

print(ThisCar.getID())
