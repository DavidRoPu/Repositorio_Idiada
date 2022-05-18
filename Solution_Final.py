# Coding Problem Solution Idiada David Romero Puyal

nrovers = 2
actual_rover = 0


# Plateu class to save the limits of the plateau grid's.
class Plateau:
    def __init__(self, xmaxplateau, ymaxplateau):
        self.xmin = 0
        self.ymin = 0
        self.xmax = xmaxplateau
        self.ymax = ymaxplateau


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

# Open the file and save the first line (Plateau size).
with open("data", "r") as fname:
    size_plateau = fname.readline().rstrip()
    # It is necessary to ensure that the rover does not go off the grid.
    plateau = Plateau(int(size_plateau[0]), int(size_plateau[2]))

# Loop to analyze the movement of the rover
    while actual_rover < nrovers:

        rover_position_in = fname.readline().rstrip()
        rover_instruction_in = fname.readline().rstrip()

# Save the values in new variable to operate.
        actual_rover_position = rover_position_in
        actual_rover_instruction = rover_instruction_in
        rover_error = 0
# In case of error, rover_error change the state and prevents the result of being printed.
# Instead of writting the result in the file, the error is written

# Execution of the instructions.
# For loop to make the rover instructions. The for loop iterates the number of statements unless a statement is wrong.
# If a statement is wrong the program exits the loop and print error.
        for index in range(len(actual_rover_instruction)):
            if actual_rover_instruction[index] == "M":                          # M --> Move function.
                actual_rover_position = move(actual_rover_position)
                if actual_rover_position == 'X':
                    rover_error = 1
                    print("ERROR, ROVER 1 POSITION OUT OF RANGE")
                    break
            elif actual_rover_instruction[index] == "L":
                actual_rover_position = rotate_left(actual_rover_position)      # L --> Rotate left.
            elif actual_rover_instruction[index] == "R":
                actual_rover_position = rotate_right(actual_rover_position)     # R --> Rotate right.
            else:
                rover_error = 1     #Invalid command
                print("ERROR, NOT VALID ROVER 1 INSTRUCTION")
                break

        # If not error, print the final position.
        if rover_error == 0:
            rover_position_out = actual_rover_position
            with open('solution', 'a') as fsol:
                fsol.write(rover_position_out)
                fsol.write('\n')
            print(rover_position_out)

        actual_rover = actual_rover + 1


# Things to change.
    # Position enters as 2 integers and 1 character.
    # Optimize functions.
