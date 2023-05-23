
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_car(self):
        return f'the car is {self.name}'\
                f' and its {self.color}'
    
car1 = Car('BMW', 'GREEN')
print(car1.print_car())

def cars_init(self, name, color):
    self.name = name
    self.color = color

Cars = type('Car', (),
            {'__init__': cars_init,
             'print_car': lambda self:
             f'the car is {self.name}'
             f' and its {self.color} in color'})

car1 = Cars('Ford', 'Blue')
print(car1.print_car())