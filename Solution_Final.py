# Coding Problem Solution
# David Romero Puyal
# davidrompuy99@gmail.com
# 679034125
# FINAL SOLUTION


nrovers = 0                 # Variable to store the rovers number (according to the result of the function num_rovers).
solution_file = "solution"  # Name of the solution file where de result has to be store.
data_file = "data"          # Name of the data input file.


# Function for calculate the number of rovers.
def num_rovers(data_name):
    with open(data_name, 'r') as fdname:
        nrov = len(fdname.readlines())
    if nrov % 2 != 1:                   # 1 line of grid dimensions and 2 lines for every rover
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


#Rotate function
def rotate(ori, direction):
    v = ["N", "E", "S", "W"]    #Cardinal points in clockwise direction
    index_act = v.index(ori)    #Obtaining actual orientation position in v list
    if direction == "R":        #Right rotation
        index_act += 1          
    elif direction == "L":      #Left rotation
        index_act -= 1
    ori = v[index_act % 4]
    return ori


# Advance 1 square function.
def move(x, y, ori, plateau):
    if ori == 'N':
        y += 1
        if y > plateau.ymax:
            raise Exception("Rover Outside Plateau North Direction")
    elif ori == 'E':
        x += 1
        if x > plateau.xmax:
            raise Exception("Rover Outside Plateau Est Direction")
    elif ori == 'S':
        y -= 1
        if y < plateau.ymin:
            raise Exception("Rover Outside Plateau South Direction")
    elif ori == 'W':
        x -= 1
        if x < plateau.xmin:
            raise Exception("Rover Outside Plateau West Direction")
    return x, y


# Calculate the final position of each rover.
def solution(rovers, data_name, solution_name):
    actual_rover = 0

    with open(data_name, 'r') as fname:            # Open the file and save the first line (Plateau size).
        
        xmax, ymax = fname.readline().rstrip().split()
        try:
            plateau = Plateau(int(xmax), int(ymax))     # It is necessary to ensure that the rover does not go off the grid.
        except:
            raise Exception("Wrong Plateau Size")
        

        while actual_rover < rovers:             # Loop to analyze the movement of the rover
            x, y, orientation = fname.readline().rstrip().split()   # Initial Position
            orientation = orientation.upper()     # if orientation is in lower case convert to upper case
            x = int(x)
            y = int(y)
            rover_instruction = fname.readline().rstrip()           # Commands

            for command in rover_instruction:       # For every letter of rover instruction string...
                command = command.upper()           # if command is in lower case convert to upper case
                if command == 'M':
                    x, y = move(x, y, orientation, plateau)     # M -> move
                elif command == 'L' or command == 'R':
                    orientation = rotate(orientation,command)      # R or L -> Rotate Function
                else:
                    raise Exception("Not valid rover instruction")  # If wrong letter

            with open(solution_name, 'a') as fsol:  # Store in the solution file the final coordinates and orientation.
                fsol.write("%s %s %s\n" % (x, y, orientation))

            actual_rover = actual_rover + 1


if __name__ == "__main__":
    nrovers = num_rovers("data")   # Obtain number of rovers.
    with open(solution_file, 'w') as fsname:
        fsname.write('OUTPUT\n')
    solution(nrovers, data_file, solution_file)
