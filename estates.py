import random
import itertools

class Estate:
    def __init__(self, area):
        self.area = area;
        
    def get_area(self):
        return self.area
    
        
class House(Estate):
    def __init__(self, area):
        super().__init__(area)
    
    def __repr__(self):
        str_repr = 'House'
        return str_repr
    
        
class Flat(Estate):
    def __init__(self, area, level, total_levels):
        super().__init__(area)
        self.level = level
        self.total_levels = total_levels
        
    def __repr__(self):
        str_repr = 'Flat'
        return str_repr    

    def getLevel(self):
        return self.level
    
    def getTotalLevels(self):
        return self.total_levels
        
class Room(Estate):
    def __init__(self, area, level, total_levels, arearoom):
        super().__init__(area)
        self.level = level
        self.total_levels = total_levels
        self.arearoom = arearoom
        
    def __repr__(self):
        str_repr = 'Room'
        return str_repr   
    
    def getLevel(self):
        return self.level
    
    '''
    Делаем генераторы
    '''
random.seed(1) 
    
def random_area():  
    flat_area = random.randrange(10, 1000, 1)
    return flat_area

def random_levels():  
    total_levels = random.randrange(2, 9, 1) # Общее количество этажей
    level = random.randrange(1, total_levels, 1) # Этаж
    return (level, total_levels)

def random_arearoom(flat_area):  # Площадь комнаты не больше общей площади
    arearoom = random.randrange(5, flat_area, 1)
    return arearoom

def random_house(): 
    return House(random_area())

def random_flat():
    flat_area = random_area()
    flat_params = random_levels()
    
    return Flat(flat_area, flat_params[0], flat_params[1]) 

def random_room():
    flat_area = random_area()
    flat_params = random_levels()
    room_area = random_arearoom(flat_area)
    
    return Room(flat_area, flat_params[0], flat_params[1], room_area)

def get_estate():
    estate_constructors = [random_house, random_flat, random_room] 
    generator_function = random.choice(estate_constructors) # Из списка выбираем рандомно один элемент
    estate_object = generator_function()

    return estate_object
    
def random_price():
    return random.randrange(1000, 1000000, 1)
    
def random_estate():
    return (get_estate(), random_price())
    
#def estate_list():
    #estates = list()
    #for x in range(1, 50):
        #estates.append(random_estate()) # 50 раз вызываем random_estate
    #return estates
    
def estate_list():
    estate_count = 50
    counter = itertools.count()
    estates = list()

    while next(counter) < estate_count:
        estates.append(random_estate())

    return estates
