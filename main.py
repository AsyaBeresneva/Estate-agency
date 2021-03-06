#!/usr/bin/env python3
import itertools   
from estates import (Estate, House, Flat, Room, estate_list,)


class Estates_db:
    
    def __init__(self):
        self.est_db = estate_list()

    def __iter__(self):  
        for element in self.est_db:
            yield element
            
    def set_db(self, db):
        self.est_db = db        
        
    def getEstates(self, estate_type):
        return (list(filter(lambda element: str(element[0]) == estate_type, self)))
           
    #def getEstates(self, estate_type):  # переиспользуем в query
        #estates = list()
        #for element in self:
            #if str(element[0]) == estate_type:
                #estates.append(element) 
        #return estates
            
    def getHouses(self): 
        return self.getEstates('House')

    def getByPrice(self, price):  # переиспользуем в query
        return list(itertools.filterfalse(lambda element: element[1] >= price, self))
        
        #estates = list()
        #for element in self:
            #if element[1] < price:
                #estates.append(element)
        #return estates

    def getByLevel(self, level): 
        return list(filter(lambda element: element[0].getLevel() == level, self.getEstates('Flat')))
        
        #estates = list()
        #for element in self.getEstates('Flat'):
            #if element[0].getLevel() == level:
                #estates.append(element)
        #return estates
    
    def getExceptBounds(self):
        estates = list()
        for element in self.getEstates('Flat'):
            current_level = element[0].getLevel() 
            if current_level > 1:
                if current_level < element[0].getTotalLevels():
                    estates.append(element)
        return estates
    
    def getByArea(self, area):  # переиспользуем в query
        return list(itertools.filterfalse(lambda element: element[0].get_area() > area, self))
        
        #estates = list()
        #for element in self:
            #if element[0].get_area() <= area:
                #estates.append(element)
        #return estates
    
    def getPerfLevel(self, level):  # используем в query
        estates = list()
        for element in self:
            if str(element[0]) == 'House':
                continue
            elif element[0].getLevel() <= level:
                estates.append(element)
        return estates
    
def main():
    
    database = Estates_db()
    
    '''
    Реализация query
    '''
    
    request_dict = {'perfect_type': 'Room', 'perfect_area': 500, 
                    'perfect_price': 900000, 'perfect_level': 3} # словарь требований
            
    func_list = [database.getEstates, database.getByArea, 
                 database.getByPrice, database.getPerfLevel,]        
    
    query = zip(func_list, request_dict.items())
    
    #for f, (k, v) in query:
        #cur = f(v)
        #print("current = ", cur)
        #print('quantity of objects =', len(cur))
        #database.set_db(f(v))
    
    #for element in database:
        #print(element)

    '''
    Вывод функций по первым 4 заданиям
    '''
    
    #for element in database.getHouses():
        #print(element)
        
    #for element in database.getByPrice(1000000):
        #print(element)
        
    for element in database.getByLevel(3):
        print(element)    
        
    #for element in database.getExceptBounds():    
        #print(element)
        
    #for element in database:    
        #print(element)

if '__main__': main()
    
