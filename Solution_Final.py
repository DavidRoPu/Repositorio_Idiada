# Coding Problem Solution
# David Romero Puyal
# davidrompuy99@gmail.com
# 679034125
# SOLUTION V1


nrovers = 0                 # Variable to store the rovers number (according to the result of the function num_rovers).
solution_file = "solution"  # Name of the solution file where de result has to be store.
data_file = "data"          # Name of the data input file.


# Function for calculate the number of rovers.
def num_rovers():
    with open(data_file, "r") as fdname:
        nrov = len(fdname.readlines())
        if nrov % 2 != 1:
            raise Exception("Number of lines Wrong")
        else:
            return int((nrov - 1)/2)


# Plateu class to save the limits of plateau grid.
class Plateau:
    def __init__(self, xmaxplateau, ymaxplateau):
        self.xmin = 0
        self.ymin = 0
        self.xmax = xmaxplateau
        self.ymax = ymaxplateau


# Rotating left function.
def rotate_left(ori):
    if ori == 'N':
        return 'W'
    elif ori == 'W':
        return 'S'
    elif ori == 'S':
        return 'E'
    elif ori == 'E':
        return 'N'


# Rotating Right function.
def rotate_right(ori):
    if ori == 'N':
        return 'E'
    elif ori == 'W':
        return 'N'
    elif ori == 'S':
        return 'W'
    elif ori == 'E':
        return 'S'


# Advance 1 square function.
def move(x, y, ori, plateau):
    if ori == 'N':
        y += 1
        if y > plateau.ymax:
            raise Exception("Rovert Outside Plateau North Direction")
    elif ori == 'E':
        x += 1
        if x > plateau.xmax:
            raise Exception("Rovert Outside Plateau Est Direction")
    elif ori == 'S':
        y -= 1
        if y < plateau.ymin:
            raise Exception("Rovert Outside Plateau South Direction")
    elif ori == 'W':
        x -= 1
        if x < plateau.xmin:
            raise Exception("Rovert Outside Plateau West Direction")
    return x, y


# Calculate the final position of each rover.
def solution(rovers):
    actual_rover = 0

    with open("data", "r") as fname:            # Open the file and save the first line (Plateau size).
        xmax, ymax = fname.readline().rstrip().split()
        plateau = Plateau(int(xmax), int(ymax))     # It is necessary to ensure that the rover does not go off the grid.

        while actual_rover < rovers:             # Loop to analyze the movement of the rover
            x, y, orientation = fname.readline().rstrip().split()   # Initial Position
            x = int(x)
            y = int(y)
            rover_instruction = fname.readline().rstrip()           # Commands

            for command in rover_instruction:    # For every letter of rover instruction string...
                if command == "M":
                    x, y = move(x, y, orientation, plateau)     # M -> move
                elif command == "L":
                    orientation = rotate_left(orientation)      # L -> Rotate Left
                elif command == "R":
                    orientation = rotate_right(orientation)     # R -> Rotate Right
                else:
                    raise Exception("Not valid rover instruction")  # If wrong letter

            with open(solution_file, 'a') as fsol:  # Store in the solution file the final coordinates and orientation.
                fsol.write("%s %s %s\n" % (x, y, orientation))

            actual_rover = actual_rover + 1


if __name__ == "__main__":
    nrovers = num_rovers()   # Obtain number of rovers.
    with open(solution_file, "w") as fsname:
        fsname.write('OUTPUT\n')
    solution(nrovers)
