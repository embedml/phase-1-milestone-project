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
- Braking (deceleration)
- Check velocity
- Check miles traveled 

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
- `braking_deceleration(deceleration, time)`

You are free to add other functions to help you reduce duplication and increase understandability and readability of your code. 

It is recommended to start from the top of the list then work your way down. 

Remember to comment as you go! 

<br><br>
## The Tests

You can see all the tests on your code in the test_car.py. Go look at them! It is good practice to write test cases *first* before developing any logic. That is done for you here. In this section we will walk you through each test and give you tips and hints on how to pass them. You are also more than welcome to create your own tests as you work in that file. 

Your instructor will know if you maliciously modified your tests, as well as forced your code to pass the existing test. In other words, your instructor will know if you are trying to cheat. 


<br><br>

## Saving and Grading your Code

As you work on this project you can test your code locally under the **Welcome to the Mile Stone** section, but can also upload your code for it to be graded. Your grade will determine if you get the EML Python Basics certificate. You must get a 100% to get the certificate. 

How do you upload your code? 
<br><br>

One way you got this starter template was through using Github. Github is a place where code is stored online and shared in *repos*. It helps other developer's not reinvent the wheel, and use other people's Python tools to accelerate their works. 

We will being using Github to upload your code to your personal repo.

There are 3 basic steps to uploading your code, and they are are placed in terminal. 

1.) Adding to stage

2.) Committing from stage

3.) Pushing commit to online repo

`git add -A`

This means: github add -A (all) files to *stage*

Stage is where files can then be committed.
You can check what is staged by using `git status` in terminal. 

`git commit -m "<some message>" `

This will commit any code you have staged. If you forget the -m and message, press `:q!` and try again.  

Then finally 
`git push` 
will push your commit to the github repo. 

Your code will then be graded automatically. 

<br><br>
Another way to think about this:

A *commit* is a package we would like to upload online.

*stage* is like a temporary places to hold what we want to commit. 

We create the package using the `add` command to add code to *stage*

Once we are done adding code to *stage*, we can then seal the package with the `commit` command. We give the commit a message like `commit -m "some message"`

We then need to send the package online, so we call `push`, which pushes your code into your repo 

<br><br>
All 4 commands used in order: 

`git status`, can be called anytime to see what is in stage

`git add <file path>` or `git add -A`, can stage specific files or use `-A` to stage all files (-A is recommended for now)

`git commit -m "some message"`, sealing stage in a commit with an attached message

`git push` push the commit to online branch. 

You can call as many commits before a push as you would like. You can also push as many new commits as you want. 

Here is a general workflow:

Modify car.py

You want to grade car.py

`git add -A`

`git commit -m "new: implemented acceleration forward function"`

`git push`

car.py is then graded


## One More thing! 

Once you have started to make good progress, go checkout turtle_testing.py to drive your car! 


## Passing your first test!

Lets start by passing your first test `test_get_car_type`

### `test_get_car_type`

Here is what the test looks like:
```python
def test_get_car_type():
    letters = string.ascii_letters
    car_type = ''.join(random.choice(letters) for i in range(10))
    temp_car = Car(car_type, "body", "motor",)
    assert temp_car.get_car_type() == car_type
```

This test creates a random string called `car_type`. It then creates a car using the `Car()` class call. 

The check is then preformed with the `assert` keyword. It asserts that `temp_car.get_car_type() == car_type` evaluates to `True`. Right now, since the function is not implemented the expression `temp_car.get_car_type() == car_type` is evaluating to `False` . 

All `assert`s must evaluate to `True` in order to pass a test.
  

You will be editing `car.py` to pass your tests. You can see this in the test file with `from car import Car`. This is saying "from car.py bring in the Car class call".      

Now go into `car.py` and have the function `get_car_type(self)` return `self.type`. This will return the car's body attribute. If this does not make sense, try visiting Unit 1D again, or ask your instructor/peers.   


Now try running the test again, as mentioned before in **Welcome to the Milestone Project** section. You should be passing one test! Congrats! 

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
When we start our car, we want `self.isOn` to be set to `True` we also want to know if we were able to turn on the car. However if the car was already on, then we want to know that we did not turn on the car. 

If the car turned on then the function `start_car()` should return `True`, if not then the function should return `False`. 

### `test_turn_off_car_basic`
When the car is on, we want to be able to turn it off with `turn_off_car()`. We also want to know if the car was turned off or not based on the return of a `True` or `False`. 

### `test_check_distance`
When a car is first created, it should start with zeros miles. Implement the `check_distance()` method to return the car's distance value.

### `test_check_velocity`
Before we start our car, we need to check to make sure the car is not moving! In order to do that we need to check the car's velocity. Implement `check_velocity()` to return the car's velocity.   

### `test_cannot_turn_off_car_when_moving`
Now are going to combine the two previous tests. We want to make sure the car cannot turn off while the car is moving. The car can only turn off if the velocity is zero. Update the `turn_off_car()` method with this functionalitiy. 

### `test_turn_right`
Since this is a simulated car, we will be simulating the movement of the car after it as already happened. We care about the end results of the car. So if we turn the car 90 degrees right, we want to update the car's angle to 90 degrees immediately. This can be thought of rotating the car's wheel when it is not moving. Later when we start moving, we will rotate the wheels as we send a move command. For this function create an attribute called `end_steering_angle`. When we turn right it will be denoted as a positive turn. If we turn the wheel 20 degrees right then 40 degree right, we expect the wheel to be turned a total of 60 degrees. We also cannot turn a negative degrees, so if a negative degrees is passed we need to throw an error. 

Hint: Use `assert <expression>` to throw an error!

### `test_turn_left`
Turning left is like turing right, except we denote left turns with negative degrees internal to our class. However the user should still only put in positive degrees. If the user puts in a negative degrees an error should be raised. 

### `test_get_end_steering_angle`
Implement `get_end_steering()`, where it will return the car's `end_steering_angle`

### `test_forward_acceleration_basic`

This is where things might start to get a little trickier, but you can do it! 
As mentioned before our car only worries about updating values *after* they happened. For example, if the car accelerated for 2 kilometer per hour^2 for 2 seconds then the car's velocity would update to 4 kilometers per hour. Same thing with distance. We only want to worry about updating values after the time has passed. 

Here are the two equations we will use. 

final_distance = 0.5 * acceleration * time**2 + initial_velocity * time + initial_distance
Note: **2 means ^2 or squared in python

final_velocity = acceleration * time + initial_velocity

In the method `accelerate_forward(acceleration, time)`, update the `distance` and `velocity` attributes of the car. 

Velocity and distance should accumulate. If the car accelerates 4 m/s^2 for 2 seconds then 2 m/s^2 for 2 seconds it should be going 12 m/s. 

Hint: User your `check_velocity()` and `check_distance()` functions to get velocity and distance! 

Also! The car has to be on to accelerate of course! If you try to accelerate before the car is one throw an error with `assert`

### `test_forward_acceleration_basic_neg_velocity`

One scenario we need to consider is when the starting velocity is negative. If our starting velocity is negative and we want to accelerate forward, we are slowing down. This means we are still traveling some distance (but that distance is not negative). What change needs to be made to the distance calculation? 


### `test_accelerate_forward_neg_values_basic`

Since the `accelerate_forward()` function has the name forward in it. We will assume if the user passes in an negative value, then made a mistake. Instead of throwing an error we would rather have the car accelerate forward with that value.

If the acceleration passed in is negative make it positive before making calculations. 

Hint: Use the built-in `abs()` function to get the absolute value of a number! It can be called by itself like the `print()` function. 


### `test_reverse_acceleration_basic`

Next is the `accelerate_reverse(acceleration, time)` function. This will have the same logic as the `accelerate_forward(acceleration, time)` function, but with a few differences. 

One thing that stays the same is we only want to pass in positive values (as not to confuse the user), so we need to modify our equations around that constraint. 

The distance we are tracking is absolute distance. If we reverse, the distance attribute should increase. If we go forward, the distance attribute increases.

You can use the equation below:

final_distance = -acceleration * time**2 + initial_velocity * time + initial_distance

Note that the final distance must be made positive, so you will need to edit this equation. 

Velocity should be decreased when we accelerate backwards. 

Give it a go! 

### `test_reverse_acceleration_basic_positive_velocity`

One scenario to consider is when velocity is positive. If accelerating in reverse, the car's velocity should slow down, but the distance traveled should still be positive even if the car slows down to a stop and then accelerates backwards with a negative velocity.  


### `test_reverse_acceleration_neg_values_basic`

As mentioned before, if a negative value is passed in, we will assume the user put it in by mistake and will continue accelerating in reverse at the rate of the absolute value of the negative acceleration passed in. 


### `test_forward_then_reverse_acceleration_basic`

This test is testing how your `accelerate_forward()` and `accelerate_reverse()` functions are working together. First starting with forward acceleration then reverse acceleration.  

### `test_reverse_then_forward_acceleration_basic`

This test is testing how your `accelerate_forward()` and `accelerate_reverse()` functions are working together. First starting with reverse acceleration then forward acceleration.  

### `test_turn_off_car_advanced`

Now that we are moving with the acceleration functions, we want to make sure we cannot turn off the car if it is moving! If the car is moving, do not turn off the car when `turn_off_car()` is called. 

### `test_braking_deceleration_forward`

Braking is the same as accelerating in the opposite direction, the only exception is that once velocity is zero, we do not continue or build velocity in the opposite of the original direction. 

Here is is also important to remember that we only update the car's values at the end of an action. This will simplify our implementation significantly. 

Lets think about a few instances of braking as if we were going in the forward direction. 

If we are going 20 m/s, then decelerate at a rate of 3 m/s^2 for 2 seconds, then our final velocity is 20 m/s - 3 m/s^2 * 2 s = 14 m/s. 

If we are going 20 m/s, then decelerate at a rate of 15 m/s^2 for 3 seconds. 15 m/s^2 * 3 s = 45 m/s, since this is larger than our original positive velocity, then our new velocity is 0. This is as if we slammed on the breaks! The fasted we can break is one time unit. 

Remember distance still needs to be updated since as we brake we are still moving. 

To simply this a bit further, we will assume that if we brake until our velocity is 0, then we break at a steady deceleration from our current forward velocity to 0. 

For example, from our instance of starting at 20 m/s and decelerating at a rate of 15 m/s^2 for 3 seconds, we will assume we actually decelerated at a steady rate from 20 m/s to 0 m/s. 

This might seem to not make sense for the user, since they could call a deceleration of 100 m/s^2 over 2 second. This would put us at a velocity of 0 m/s after the first second. However for this coding exercise we will assume the user holds more weight in the length of time they brake, not necessarily how hard they brake, so in our example, we decelerate over the 2 seconds. (This also makes our math much simpler). If the user wants to decelerate in one second they could call a deceleration of 100 m/s^2 for 1 second. 



Hint: You can use the same calculations you used in reverse acceleration to calculate final velocity (and see if it is larger or smaller in magnitude than your current velocity). 

Hint Hint: Turn your calculations into functions to make it even easier! 


### `test_braking_deceleration_reverse`

This is the same as the previous test, but decelerating while moving in the reverse direction, aka negative velocity. 

Any tests you have not finished keep trying! You can do it! 

## End of Milestone

If you have not checked out turtle_testing.py, please do so now! You can watch your car move and try out a bunch of different command combinations. Share what you draw in your year's python learning slack channel! 

Once you have passed all tests, reach out to your instructor to verify!