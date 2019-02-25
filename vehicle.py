class Vehicle:


    def __init__(self, year, price):
        self.year   = year
        self.price  = price




class Car(Vehicle):
    wheel_count = 4
    capacity    = 6

    def __init__(self, hour, year, price):
        self.hour   = hour
        Vehicle.__init__(self,year,price)
    
    def pay_tax(self):
        return (0.15*self.price)

    def park(self):
        if(self.capacity<=5):
            return((self.wheel_count*1250)*self.hour)
        if(self.capacity>5):
            return (((self.wheel_count*1250)*self.hour)+(5000*self.hour))



class Motorbike(Vehicle):
    wheel_count = 2
    capacity    = 2    

    def __init__(self, wheel, hour):
        self.hour   = hour
        self.wheel  = wheel
    
    def pay_tax(self):
        return (0.1*self.price)

    def park(self, hour):
        if(self.capacity<=5):
            return((self.wheel_count*1250)*self.hour)
        if(self.capacity>5):
            return (((self.wheel_count*1250)*self.hour)+(5000*self.hour))

 

class Bicycle(Vehicle):
    wheel_count = 2
    capacity    = 2

    def __init__(self, tax, wheel, hour):
        self.tax    = tax
        self.wheel  = wheel
        self.hour   = hour

    def pay_tax(self):
        return 0

    def park(self):
        if(self.capacity<=5):
            return((self.wheel_count*1250)*self.hour)
        if(self.capacity>5):
            return (((self.wheel_count*1250)*self.hour)+(5000*self.hour))



