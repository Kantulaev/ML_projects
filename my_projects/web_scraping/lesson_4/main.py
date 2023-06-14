class Car():
  def __init__(self,model,year):
    self.year = year
    self.model = 10
  def drive(self):
    print(self.model,"run")
    print(self.year,"run")
    print(self)
    print(type(self))



car1 = Car('camry',2015)
car2 = Car('camry2',20152)
Car.drive(car1)
Car.drive(car2)