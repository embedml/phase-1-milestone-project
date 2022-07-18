class Car: # Creating car class
  '''
  Car object that simulates a car in code!
  '''
  def __init__(self, car_type, body_type, motor_type):
    print("Created a car!") # Shows we are in the __init__ function
    self.motor = motor_type # Assigns the Car object's motor attribute to motor_type
    self.body = body_type # Assigns the Car object's body attribute to body_type
    self.type = car_type  # Assigns the Car objects' type attribute to car_type
    self.isOn = False
  
  def get_car_type(self):
    '''Implement this function, see README.md'''
    pass

  def get_body_type(self):
    '''Implement this function, see README.md'''
    pass

  def get_motor_type(self):
    '''Implement this function, see README.md'''
    pass

  def __str__(self):
    '''This is a function is hidden like init, except it lets you use the print() function on your car object.'''
    '''Implement this function, see README.md'''
    pass

  def start_car(self): # Notice the self that is passed in 
    '''
    Checks if the car is started, 
    if is on, tells user it is on
    if not then starts car
    '''
    if self.isOn:
      print("Car is already on!")
      return True
    else: # Else car is off
      print("Starting Car")
      self.isOn = True
      return True

  def turn_off_car(self):
    '''
    Checks if the car is started, 
    if is on, tells user it is on
    if not then starts car
    '''   
    if self.isOn:
      print("Turning car off")
      self.isOn = False
      return True
    else: # Else car is off
      print("Car is alread off!")
      return True
  
  def check_distance(self):
    '''Implement this function, see README.md'''
    pass
  
  def check_velocity(self):
    '''Implement this function, see README.md'''
    pass

  def turn_right(self, degrees):
    '''Implement this function, see README.md'''
    assert degrees >=0, "Degrees must be positive"
    pass

  def turn_left(self, degrees):
    '''Implement this function, see README.md'''
    pass
  
  def get_end_steering_angle(self):
    '''Implement this function, see README.md'''
    pass
  
  def accelerate_forward(self, acceleration, time):
    '''Implement this function, see README.md'''
    pass
  
  def accelerate_reverse(self, acceleration, time):
    '''Implement this function, see README.md'''
    # Add an assert car is on here! Has form, above too: assert <expression>, "message"
    pass
  
  def braking_deacceleration(self, deacceleration, time):
    '''Implement this function, see README.md'''
    pass

if __name__ == "__main__":
  temp_car = Car("Tesla", "Sedan", 'EV')
  pass