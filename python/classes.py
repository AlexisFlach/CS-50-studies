class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

p = Point(1, 2)

class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []
  
  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True

  def open_seats(self):
    return self.capacity - len(self.passengers)
  

flight = Flight(3)

passengers = ["Alex", "Harry", "Bob", "Tom"]

for person in passengers:
  success = flight.add_passenger(person)
  if success:
      print(f"Added {person} to the flight")
  else:
    print(f"Not able to add {person} to the flight")