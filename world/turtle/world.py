from world.obstacles import draw_obstacles, is_path_blocked
import turtle

obs = []
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0
new_x, new_y = 0, 0
is_obs = False

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

def creating_a_screen():
    """This function creates an instance of the
    the screen.
    Returns:
        instance: a screen
    """   
    window = turtle.Screen()
    window.title('Toy Robot 4')
    window.screensize(500, 500)
    return window


def make_turtle():
    """This function creates an instance of 
    the turtle
    Returns:
        turtle: an instance of a turtle
    """   
    bot = turtle.Turtle()
    bot.color('green')
    bot.shape('turtle')
    return bot


def make_boundary(bot):
    """This function draws the boundary.
    Args:
        bot (turtle): an instance of a turtle
                        that draws the boundary
    """    
    bot.penup()
    bot.goto(-100, 200)
    bot.pendown()
    bot.pencolor('red')
    for i in range(2):
        bot.forward(200)
        bot.right(90)
        bot.forward(400)
        bot.right(90)
    bot.pencolor('green')
    bot.penup()
    bot.goto(0, 0)
    bot.left(90)
    

robot = make_turtle()
window = creating_a_screen()
make_boundary(robot)



def show_position(robot_name):
    """This function moves the robot to the intended 
    coordinates.
    """    
    robot.goto(position_x, position_y)


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y, new_x, new_y
    new_x = position_x
    new_y = position_y
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    if is_path_blocked(position_x, position_y, new_x, new_y, obs) == True:
        global is_obs
        is_obs = True
    if is_position_allowed(new_x, new_y) and not is_path_blocked(position_x, position_y, new_x, new_y, obs):
        position_x = new_x
        position_y = new_y
        return True
    
    return False

