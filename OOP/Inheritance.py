class Clock(object):
    
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def get_time(self):
        return f"{self.__hour}:{self.__minute}:{self.__second}"
    
# rolex = Clock(12,0,0)

class Calender(object):
    
    def __init__(self, day, month, year):
        self.set_date(day, month, year)
        
    def set_date(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
        
    def get_date(self):
        return f"{self.__month}/{self.__day}/{self.__year}"
    
# new_calender = Calender(12,4,2001)

class Day(Clock, Calender):
    
    def __init__(self, day, month, year, hour, minute, second):
        Calender.__init__(self,day, month, year)
        Clock.__init__(self, hour, minute, second)
        
    def today(self):
        return f"{self.get_time()} {self.get_date()}"
    
birthday = Day(12,4,2001,12,0,0)
print(birthday.today())