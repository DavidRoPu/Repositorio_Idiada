# Coding Problem Tests of FUNCTIONS
# David Romero Puyal
# davidrompuy99@gmail.com
# 679034125

# TESTING USING UNITTEST

import unittest
from Solution_Final import Plateau
from Solution_Final import num_rovers
from Solution_Final import rotate_right
from Solution_Final import rotate_left
from Solution_Final import move



#FUNCTIONS TESTS

class Tests_Rotate_Right(unittest.TestCase):
    def test_1_rotate_right(self):
        result = rotate_right('N')
        self.assertEqual(result, 'E')

class Tests_Rotate_Left(unittest.TestCase):
    def test_1_rotate_right(self):
        result = rotate_left('N')
        self.assertEqual(result, 'W')

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
        result = num_rovers()
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
