
'''
Welcome to the turtle testing file! 

This is where you can see your car move! 

You can see an existing sample below. 

Create your car with the control_car variable, then create a list 
of tuples, where each tuple holds the car function command and 
its two attributes in the right order.

Then run this file! If you are interested in how this works, reach 
out to your instructor, with enough interest there may be a 
bonus lecture on this file. 

'''
import turtle
from car import Car
import time

# Build your car object here. 

control_car = Car("fill me", "fill me", "fill me!") # Fill in the values for the car :)

car_commands = [ # car_commands should only be start, off, acceleration, deceleration commands, and steering commands, on and off commands must have an extra na param see example
    (control_car.start_car),
    (control_car.turn_right, 90),
    (control_car.accelerate_forward, 10 , 4), # this will be called like temp_car.accelerate_forward(10, 10)
    (control_car.turn_right, 40),
    (control_car.accelerate_forward, 10 , 8), # this will be called like temp_car.accelerate_reverse(10, 10)
    (control_car.braking_deceleration, 10, 4)
    ] 

def run(car_commands):
    global control_car
    print(f"Starting simulation of: ", control_car)
    time.sleep(3)
    vel = 0
    for func_tuple in car_commands:
        try:
            function_call = func_tuple[0]
        except:
            function_call = func_tuple
        if function_call == control_car.start_car:
            control_car.start_car()
        elif function_call == control_car.turn_off_car:
            control_car.turn_off_car()
        elif function_call == control_car.accelerate_forward:
            acceleration = func_tuple[1]
            acc_time = func_tuple[2]
            control_car.accelerate_forward(acceleration, acc_time)
            assert acc_time % 1 == 0, "Time must be a whole number"
            for time_unit in range(1, acc_time+1):
                vel += acceleration * 1
                print("Velocity:", vel)
                turtle.right(control_car.get_end_steering_angle()/acc_time)
                turtle.forward(vel * 1)
                time.sleep(.3)
            control_car.end_steering_angle = 0
        elif function_call == control_car.accelerate_reverse:
            acceleration = func_tuple[1]
            acc_time = func_tuple[2]
            control_car.accelerate_reverse(acceleration, acc_time)
            assert acc_time % 1 == 0, "Time must be a whole number"
            for time_unit in range(1, acc_time + 1):
                vel += -acceleration 
                print("Velocity:", vel)
                turtle.right(control_car.get_end_steering_angle()/acc_time)
                turtle.forward(vel * 1) # This is actually forward distance, but vel * 1 time unit = distance
                time.sleep(.3)
            control_car.end_steering_angle = 0
        elif function_call == control_car.braking_deceleration:
            deceleration = func_tuple[1]
            decel_time = func_tuple[2]
            start_vel = control_car.check_velocity()
            control_car.braking_deceleration(deceleration, decel_time)
            end_vel = control_car.check_velocity()
            assert decel_time % 1 == 0, "Time must be a whole number"
            for time_unit in range(1, decel_time + 1):
                vel += (end_vel-start_vel)/decel_time
                print("Velocity:", vel)
                turtle.right(control_car.get_end_steering_angle()/decel_time)
                turtle.forward(vel * 1)
                time.sleep(.3)
            # Reset steering angle 
            control_car.end_steering_angle = 0
        elif function_call == control_car.turn_right:
            degrees = func_tuple[1]
            control_car.turn_right(degrees)
        elif function_call == control_car.turn_left:
            degrees == func_tuple[1]
            control_car.turn_left(degrees)
    time.sleep(3)
    turtle.done()
    print(control_car.type, "traveled:", control_car.check_distance(), "units")

run(car_commands)
