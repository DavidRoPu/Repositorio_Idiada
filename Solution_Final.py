# Coding Problem Solution Idiada David Romero Puyal


# Plateu class to save the limits of the plateau grid's.
class Plateau:
    def __init__(self, xmaxplateau, ymaxplateau):
        self.xmin = 0
        self.ymin = 0
        self.xmax = xmaxplateau
        self.ymax = ymaxplateau


# Rover class to create as many rover objects as rovers are necessary.
# rover_position_in is made to save the initial position of the rover.
# rover_position_in is made to operate.
# rover_position_out is made to save the final position of the rover.
# rover_position_instructions is made to save the instructions of the rover.
class Rover:
    def __init__(self, rpin, rp, rpout, rins):
        self.rover_position_in = rpin
        self.rover_position = rp
        self.rover_position_out = rpout
        self.rover_position_instruction = rins
        self.rover_error = 0


# The following function allows to rotate the rover to the left.
# To change the character of rover_position string I have used lists and join() function.
def rotate_left(rover_position):
    if rover_position[4] == 'N':
        lst = list(rover_position)
        lst[4] = 'W'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'W':
        lst = list(rover_position)
        lst[4] = 'S'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'S':
        lst = list(rover_position)
        lst[4] = 'E'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'E':
        lst = list(rover_position)
        lst[4] = 'N'
        rover_position = ''.join(lst)
    return rover_position


# The following function allows to rotate the rover to the right.
# To change the character of rover_position string I have used lists and join() function.
def rotate_right(rover_position):
    if rover_position[4] == 'N':
        lst = list(rover_position)
        lst[4] = 'E'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'E':
        lst = list(rover_position)
        lst[4] = 'S'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'S':
        lst = list(rover_position)
        lst[4] = 'W'
        rover_position = ''.join(lst)
    elif rover_position[4] == 'W':
        lst = list(rover_position)
        lst[4] = 'N'
        rover_position = ''.join(lst)
    return rover_position


# The following function allows the rover to advance 1 square in the direction indicated by the orientation.
def move(rover_position):
    if rover_position[4] == 'N':
        aux = int(rover_position[2])
        aux = aux + 1
        if aux > plateau.ymax:
            return 'X'
        lst = list(rover_position)
        lst[2] = str(aux)
        rover_position = ''.join(lst)
    elif rover_position[4] == 'E':
        aux = int(rover_position[0])
        aux = aux + 1
        if aux > plateau.xmax:
            return 'X'
        lst = list(rover_position)
        lst[0] = str(aux)
        rover_position = ''.join(lst)
    elif rover_position[4] == 'S':
        aux = int(rover_position[2])
        aux = aux - 1
        if aux < plateau.ymin:
            return 'X'
        lst = list(rover_position)
        lst[2] = str(aux)
        rover_position = ''.join(lst)
    elif rover_position[4] == 'W':
        aux = int(rover_position[0])
        aux = aux - 1
        if aux < plateau.xmin:
            return 'X'
        lst = list(rover_position)
        lst[0] = str(aux)
        rover_position = ''.join(lst)
    return rover_position


# Indicate the size of the Plateau.
# It is necessary to ensure that the rover does not go off the grid.
size_plateau = input("Upper-Right Coordinates of the Plateau: ")
plateau = Plateau(int(size_plateau[0]), int(size_plateau[2]))

# ROVER 1. Initial Position and Instructions.
# ROVER 1 Object creation.
roposin = input("Rover 1 Initial Position: ")
roins = input("Rover 1 Instructions: ")
rover1 = Rover(roposin, roposin, roposin, roins)

# ROVER 2. Initial Position and Instructions
# ROVER 2 Object creation.
roposin = input("Rover 2 Initial Position: ")
roins = input("Rover 2 Instructions: ")
rover2 = Rover(roposin, roposin, roposin, roins)


# ROVER 1. Execution of the instructions.
# For loop to make the rover 1 instructions. The for loop iterates the number of statements unless a statement is wrong.
# If a statement is wrong the program exits the loop and print error.
# M --> Move function.
# L --> Rotate left.
# R --> Rotate right.
for index in range(len(rover1.rover_position_instruction)):
    if rover1.rover_position_instruction[index] == "M":
        rover1.rover_position = move(rover1.rover_position)
        if rover1.rover_position == 'X':
            rover1.rover_error = 1
            print("ERROR, ROVER 1 POSITION OUT OF RANGE")
            break
    elif rover1.rover_position_instruction[index] == "L":
        rover1.rover_position = rotate_left(rover1.rover_position)
    elif rover1.rover_position_instruction[index] == "R":
        rover1.rover_position = rotate_right(rover1.rover_position)
    else:
        rover1.rover_error = 1
        print("ERROR, NOT VALID ROVER 1 INSTRUCTION")
        break

# ROVER 1. If not error, print the final position.
if rover1.rover_error == 0:
    rover1.rover_position_out = rover1.rover_position
    print(rover1.rover_position_out)
rover1.rover_error = 0

# ROVER 2. Execution of the instructions.
# For loop to make the rover 2 instructions. The for loop iterates the number of statements unless a statement is wrong.
# If a statement is wrong the program exits the loop and print error.
# M --> Move function.
# L --> Rotate left.
# R --> Rotate right.
for index in range(len(rover2.rover_position_instruction)):
    if rover2.rover_position_instruction[index] == "M":
        rover2.rover_position = move(rover2.rover_position)
        if rover2.rover_position == 'X':
            rover2.rover_error = 1
            print("ERROR, ROVER 2 POSITION OUT OF RANGE")
            break
    elif rover2.rover_position_instruction[index] == "L":
        rover2.rover_position = rotate_left(rover2.rover_position)
    elif rover2.rover_position_instruction[index] == "R":
        rover2.rover_position = rotate_right(rover2.rover_position)
    else:
        rover2.rover_error = 1
        print("ERROR, NOT VALID ROVER 2 INSTRUCTION")
        break

# ROVER 2. If not error, print the final position.
if rover2.rover_error == 0:
    rover2.rover_position_out = rover2.rover_position
    print(rover2.rover_position_out)
rover2.rover_error = 0