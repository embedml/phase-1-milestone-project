[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8118754&assignment_repo_type=AssignmentRepo)
# phase-1-milestone-begin
Phase 1 Milestone beginner template meant to give students starter code and tests to code against

## Welcome to the Milestone Project! 

Passing all test cases is required for you to finish this workshop. 

You can run your tests in terminal by doing the following:

Make sure your terminal is in this directory. You can confirm that is true by typing `pwd` in terminal. 

Then run `pip install pytest` in terminal 

Now run `pytest` in terminal. 

^ If that does not work try `python -m pytest`

You will see every test is failing. Your goal is to pass every test with the instructions below. Happy coding! 

<br><br>
## Milestone Objectives

In this milestone your goal is to create a virtual car. 

The car will have multiple functions:
- Start the Car 
- Turn off the Car
- Accelerate Forward
- Accelerate Backwards
- Braking (deacceleration)
- Check speed
- Check miles traveled 
- Set max forward and reverse speed

The main functions you need to implement are:
- `get_body_type()`
- `get_car_type()`
- `get_motor_type()`
- `__str__()`
- `start_car()`
- `turn_off_car()`
- `check_distance()`
- `check_velocity()`
- `turn_right(degrees)`
- `turn_left(degrees)`
- `get_end_steering_angle()`
- `accelerate_forward(acceleration, time)`
- `accelerate_reverse(acceleration, time)`
- `braking_deacceleration(deacceleration, time)`

You are free to add other functions to help you reduce duplication and increase understandability and readability of your code. 

It is recommended to start from the top of the list then work your way down. 

Remember to comment as you go! 

<br><br>
## The Tests

You can see all the tests on your code in the test_car.py. Go look at them! It is good practice to write test cases *first* before developing any logic. That is done for you here. In this section we will walk you through each test and give you tips and hints on how to pass them. You are also more than welcome to create your own tests as you work in that file. 

Your instructor will know if you maliciously modified your tests, as well as forced your code to pass the existing test. In other words, your instructor will know if you are trying to cheat. 


<br><br>

## Passing your first test!

Lets start by passing your first test `test_get_car_type`

### `test_get_car_type`

Here is what the test looks like:
```python
def get_car_type():
    letters = string.ascii_letters
    car_type = ''.join(random.choice(letters) for i in range(10))
    temp_car = Car(car_type, "body", "motor",)
    assert temp_car.get_car_type() == car_type
```

This test creates a random string called `car_type`. It then creates a car using the `Car()` class call. 

The check is then preformed with the `assert` keyword. It asserts that `temp_car.get_car_type() == car_type` evaluates to `True`. Right now, since the function is not implemented the expression `temp_car.get_car_type() == car_type` is evaluating to `False`  
  

You will be editing `car.py` to pass your tests. You can see this in the test file with `from car import Car`. This is saying "from car.py bring in the Car class call".      

Now go into `car.py` and have the function `get_car_type(self)` return `self.type`. This will return the car's body attribute. If this does not make sense, try visiting Unit 1D again, or ask your instructor/peers.   


Now try running the test again. You should be passing one test! Congrats! 

### `test_get_car_body`

Next is to pass the `test_get_car_body` test. This is the same as teh `test_get_car_type` test, but this time you want to return the car's body attribute. 

### `test_get_motor_type`

Try doing this test on your own! I should be very similar to the previous two tests. 

### `test__str__()`

`__str__()` is a hidden function like `__init__()`. `__str__()` is called when the `Car` object is converted to a string. Like in the `print()` call. 

Once `__str__()` expects a string to be returned. When `print(car_object)` is called it is equivelent to `print(car_object.__str__())`. `print()` does the conversion to a string internally. 

The returned string can be anything, but in this case we want it to return something like: `f"Type: {self.type}, Body: {self.body}, Motor: {self.motor}"`. 

Once you have the return working, you can see it by creating and printing a car object at the bottom of the car.py file. 

Now see if your test case has passed! 

### `test_start_car_basic`


