
import pytest
import random
import string
from instructor_car import Car


@pytest.fixture()
def car_object_basic():
    return Car(car_type="Tesla", body_type="Sedan", motor_type="Electric", starter_miles=0)

def test_get_car_type():
    letters = string.ascii_letters
    car_type = ''.join(random.choice(letters) for i in range(10))
    temp_car = Car(car_type, "body", "motor",)
    assert temp_car.get_car_type() == car_type

def test_get_car_body():
    letters = string.ascii_letters
    car_body = ''.join(random.choice(letters) for i in range(10))
    temp_car = Car("type", car_body, "motor")
    assert temp_car.get_car_body() == car_body

def test_get_motor_type():
    letters = string.ascii_letters
    motor_type = ''.join(random.choice(letters) for i in range(10))
    temp_car = Car( "type", "body", motor_type)
    assert temp_car.get_motor_type() == motor_type

def test__str__():
    letters = string.ascii_letters
    car_body = ''.join(random.choice(letters) for i in range(10))
    motor_type = ''.join(random.choice(letters) for i in range(10))
    car_type = ''.join(random.choice(letters) for i in range(10))
    car_temp_1 = Car(car_type, car_body, motor_type)
    assert car_temp_1.__str__() == f"Type: {car_type}, Body: {car_body}, Motor: {motor_type}"
    

def test_start_car_basic(car_object_basic):
    '''This test should pass automatically'''
    assert car_object_basic.start_car() == True
    assert car_object_basic.isOn == True
    assert car_object_basic.start_car() == False
    assert car_object_basic.isOn == True
    
    
def test_turn_off_car_basic(car_object_basic):
    assert car_object_basic.turn_off_car() == False
    assert car_object_basic.isOn == False
    car_object_basic.isOn = True
    assert car_object_basic.turn_off_car() == True
    assert car_object_basic.isOn == False


def test_start_velocity_check(car_object_basic):
    vel = car_object_basic.check_velocity()
    assert vel == 0

def test_cannot_turn_off_car_when_moving(car_object_basic):
    car_object_basic.start_car()
    car_object_basic.velocity = random.randint(1, 1000)
    assert car_object_basic.turn_off_car() == False
    car_object_basic.velocity = random.randint(-1000, -1)
    assert car_object_basic.turn_off_car() == False

def test_turn_right(car_object_basic):
    deg = random.randint(0, 100)
    car_object_basic.turn_right(deg)
    assert car_object_basic.end_steering_angle == deg
    with pytest.raises(Exception) as e: 
            car_object_basic.turn_right(-deg) 

def test_turn_left(car_object_basic):
    deg = random.randint(0, 100)
    car_object_basic.turn_left(deg)
    assert car_object_basic.end_steering_angle == -deg
    with pytest.raises(Exception) as e: 
            car_object_basic.turn_left(-deg) 


    
def test_forward_acceleration_basic(car_object_basic):
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_forward(2.4,10) # Should fail due to car not being on
    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(10,10)
    assert car_object_basic.check_distance() == 1000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(100,0)
    assert car_object_basic.check_distance() == 1000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(0,10)
    assert car_object_basic.check_distance() == 2000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(3,2)
    assert car_object_basic.check_distance() == 2218
    assert car_object_basic.check_velocity() == 106


def test_reverse_acceleration_basic(car_object_basic):
    with pytest.raises(Exception) as e:
            car_object_basic.accelerate_reverse(1.2,10)  # Should fail due to car not being on
    assert car_object_basic.start_car()
    car_object_basic.accelerate_reverse(5,5)
    assert car_object_basic.check_distance() == 125
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(100,0)
    assert car_object_basic.check_distance() == 125
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(0,10)
    assert car_object_basic.check_distance() == 375
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(7,3)
    assert car_object_basic.check_distance() == 597
    assert car_object_basic.check_velocity() == -46
    pass

def test_accelerate_forward_neg_values_basic(car_object_basic):
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_forward(10,8) # Should fail due to car not being on
    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(-10,10)
    assert car_object_basic.check_distance() == 1000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(-100,0)
    assert car_object_basic.check_distance() == 1000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(0,10)
    assert car_object_basic.check_distance() == 2000
    assert car_object_basic.check_velocity() == 100
    car_object_basic.accelerate_forward(-3,2)
    assert car_object_basic.check_distance() == 2218
    assert car_object_basic.check_velocity() == 106


def test_reverse_acceleration_neg_values_basic(car_object_basic):
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_reverse(-7,10) # Should fail due to car not being on
    assert car_object_basic.start_car()
    car_object_basic.accelerate_reverse(-5,5)
    assert car_object_basic.check_distance() == 125
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(-100,0)
    assert car_object_basic.check_distance() == 125
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(0,10)
    assert car_object_basic.check_distance() == 375
    assert car_object_basic.check_velocity() == -25
    car_object_basic.accelerate_reverse(-7,3)
    assert car_object_basic.check_distance() == 597
    assert car_object_basic.check_velocity() == -46
    pass


def test_forward_then_reverse_acceleration_basic(car_object_basic):
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_reverse(1,1) # Should fail due to car not being on
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_forward(3.3,5) # Should fail due to car not being on

    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(1.2,7)
    car_object_basic.accelerate_reverse(1.2,7)
    assert car_object_basic.check_velocity() == 0
    assert round(car_object_basic.check_distance(), 2) == 58.8
    car_object_basic.accelerate_forward(-5,3)
    car_object_basic.accelerate_reverse(3, 1)
    assert car_object_basic.check_velocity() == 12
    assert round(car_object_basic.check_distance(), 3) == 139.8
    pass

def test_reverse_then_forward_acceleration_basic(car_object_basic):
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_reverse(-1,0) # Should fail due to car not being on
    with pytest.raises(Exception) as e: 
            car_object_basic.accelerate_forward(4,2) # Should fail due to car not being on

    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(1.2,7)
    car_object_basic.accelerate_reverse(1.2,7)
    assert car_object_basic.check_velocity() == 0
    assert round(car_object_basic.check_distance(), 2) == 58.8
    car_object_basic.accelerate_forward(-5,3)
    car_object_basic.accelerate_reverse(3, 1)
    assert car_object_basic.check_velocity() == 12
    assert round(car_object_basic.check_distance(), 3) == 139.8

def test_turn_off_car_advanced(car_object_basic):
    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(5,10)
    assert car_object_basic.turn_off_car() == False

def test_braking_deacceleration_forward(car_object_basic):
    assert car_object_basic.start_car()
    car_object_basic.accelerate_forward(5,10)
    car_object_basic.braking_deacceleration(5, 10)
    assert car_object_basic.check_velocity() == 0
    assert car_object_basic.check_distance() == 500
    car_object_basic.accelerate_forward(2.5,5)
    car_object_basic.braking_deacceleration(1, 3)
    assert car_object_basic.check_velocity() == 9.5
    assert car_object_basic.check_distance() == 565.75
    car_object_basic.braking_deacceleration(200, 2)
    assert car_object_basic.check_velocity() == 0
    assert car_object_basic.check_distance() == 591.875

def test_braking_deacceleration_reverse(car_object_basic):
    assert car_object_basic.start_car()
    car_object_basic.accelerate_reverse(2,12)
    car_object_basic.braking_deacceleration(2, 12)
    assert car_object_basic.check_velocity() == 0
    assert car_object_basic.check_distance() == 288
    car_object_basic.accelerate_reverse(3.1, 18)
    assert car_object_basic.check_distance() == 460.98
    assert round(car_object_basic.check_velocity(), 3) == -55.8
    car_object_basic.braking_deacceleration(1.1, 7)
    assert car_object_basic.check_distance() == 843.11
    assert car_object_basic.check_velocity() == -48.1
    car_object_basic.braking_deacceleration(100, 11)
    assert car_object_basic.check_velocity() == 0
    assert round(car_object_basic.check_distance(), 4) == 1161.8818

    
    




