# Coding Problem Tests of FUNCTIONS
# David Romero Puyal
# davidrompuy99@gmail.com
# 679034125

# TESTING USING UNITTEST

import unittest
from Solution_Final import Plateau
from Solution_Final import num_rovers
from Solution_Final import rotate
from Solution_Final import move
from Solution_Final import solution



#FUNCTIONS TESTS

class Tests_Rotate(unittest.TestCase):
    def test_1_rotate_left(self):
        result = rotate('N','L')
        self.assertEqual(result, 'W')
    def test_1_rotate_right(self):
        result = rotate('N','R')
        self.assertEqual(result, 'E')


class Tests_move(unittest.TestCase):
    plateau = Plateau(5, 5)
    def test_2_move(self):
        (resultx, resulty) = move(1, 2, 'N', self.plateau)
        self.assertEqual([resultx, resulty],[1,3])
    def test_1_move(self):
        (resultx, resulty) = move(1, 2, 'E', self.plateau)
        self.assertEqual([resultx, resulty],[2,2])


class Tests_num_rovers(unittest.TestCase):
    def test_1_numrovers(self):
        result = num_rovers("data")
        self.assertEqual(result, 2)


#Solution with data1.
#Compare the results from solutionX with the expected (saved in expectedsolutionX.txt)
class Tests_problems(unittest.TestCase): 
    
    #data1 Solutio1 test
    def test_data1_sol1(self):
        i = 0
        expected_lines = 4
        nrov = num_rovers("Problems/data1")
        with open("Problems/solution1", 'w') as fsname: #Write a tittle.
            fsname.write('OUTPUT\n')
        solution(nrov, "Problems/data1", "Problems/solution1")  #Solution with case 1. data1 solution1
        with open("Problems/solution1", 'r') as fsolution1: # Open solution1 file. 
            with open("Problems/expectedsolution1", 'r') as fexpectedsolution1: # Open expected results file.
                nlines = len(fexpectedsolution1.readlines())
                fexpectedsolution1.seek(0)  # Move fexpectedsolution file pointer to the beginnig of the file
                self.assertEqual(nlines, expected_lines) # 3 rovers -> Tittle + 3 lines = 4 lines
                tittle_solution = fsolution1.readline().rstrip()            #tittle_solution = OUTPUT
                tittle_expected = fexpectedsolution1.readline().rstrip()    #tittle_expected = OUTPUT
                self.assertEqual(tittle_solution, tittle_expected)          #Compare tittles of the files
                i += 1
                while i<nlines: #Compare the solution results with the expected results of each rover.
                    xs, ys, oris = fsolution1.readline().rstrip().split()           # Solution coordinates and orientation
                    xe, ye, orie = fexpectedsolution1.readline().rstrip().split()   # Expected coordinates and orientation
                    self.assertEqual([int(xs), int(ys), oris],[int(xe), int(ye), orie]) # Each line has to be equal
                    i += 1

    #data2 solution2 test
    def test_data1_sol2(self):
            i = 0
            expected_lines = 4
            nrov = num_rovers("Problems/data2")
            with open("Problems/solution2", 'w') as fsname: #Write a tittle.
                fsname.write('OUTPUT\n')
            solution(nrov, "Problems/data2", "Problems/solution2")  #Solution with case 2. data2 solution1
            with open("Problems/solution2", 'r') as fsolution1: # Open solution2 file. 
                with open("Problems/expectedsolution2", 'r') as fexpectedsolution1: # Open expected results file.
                    nlines = len(fexpectedsolution1.readlines())
                    fexpectedsolution1.seek(0)  # Move fexpectedsolution file pointer to the beginnig of the file
                    self.assertEqual(nlines, expected_lines) # 3 rovers -> Tittle + 3 lines = 4 lines
                    tittle_solution = fsolution1.readline().rstrip()            #tittle_solution = OUTPUT
                    tittle_expected = fexpectedsolution1.readline().rstrip()    #tittle_expected = OUTPUT
                    self.assertEqual(tittle_solution, tittle_expected)          #Compare tittles of the files
                    i += 1
                    while i<nlines: #Compare the solution results with the expected results of each rover.
                        xs, ys, oris = fsolution1.readline().rstrip().split()           # Solution coordinates and orientation
                        xe, ye, orie = fexpectedsolution1.readline().rstrip().split()   # Expected coordinates and orientation
                        self.assertEqual([int(xs), int(ys), oris],[int(xe), int(ye), orie]) # Each line has to be equal
                        i += 1


if __name__ == "__main__":
    unittest.main()
    