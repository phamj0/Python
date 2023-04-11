import math

def sumArray(listA, listB):
    listC = []
    sumC = 0
    for x in range(len(listA)):
        newCvalue = listA[x] * listB[x]
        listC.append(newCvalue)
        sumC += newCvalue
    return listC, sumC

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sumArray(a, b))



class Vehicle:

    def __init__(self, name, year, price):
        self._name = name
        self._year = year
        self._price = price

    def get_name(self):
        '''Returns the name of the vehicle'''
        return self._name
    
    def get_year(self):
        '''Returns the year of the vehicle'''
        return self._year
    
    def get_price(self):
        '''Returns the price of the vehicle'''
        return self._price
    
    def set_name(self, name):
        '''Sets new name for vehicle'''
        self._name = name 

    def set_year(self, year):
        '''Sets new year for vehicle'''
        self._year = year

    def set_price(self, price):
        '''Sets new price for vehicle'''
        self._price = price


##########Testing#########
carA = Vehicle('Honda Civic', 2018, 26000)
print('Model: ' + carA.get_name())
print('Year: ' + str(carA.get_year()))
print('Price: ' + str(carA.get_price()))
carA.set_name('Ford Mustang')
carA.set_year(2023)
carA.set_price(45000)
print('Model: ' + carA.get_name())
print('Year: ' + str(carA.get_year()))
print('Price: ' + str(carA.get_price()))


def findX(list1, target):
    for i in list1:
        if i == target:
            return list1[target]
        else:
            return None
    
           
S = [6, 2, 5, 7, 9, 12, 1, 10, 8, 4]
print(findX(S, 10))



