import sys
import unittest
from unittest.mock import patch
from io import StringIO
import random
from world.obstacles import *

class TestingObstacles(unittest.TestCase):
    sys.stdout = StringIO()

    def testing_number_obstacles(self):
        random.randint = lambda a, b : 1
        self.assertTrue(generate_number(), 1)


    def testing_generate_obstacles(self):
        random.randint = lambda a, b: 25
        self.assertEqual(get_obstacles(1), [(25, 25)])


    def testing_square_obstacles_one(self):
        cords = [(23,8)]
        self.assertEqual(square_obstacles(cords), [[(23,8), (27,8), (27,12), (23,12), (23,8)]])


    def testing_square_obstacles_multiple(self):
        cords = [(-17,-92), (22,-127), (-17,-5)]
        self.assertEqual(square_obstacles(cords), [[(-17,-92), (-13,-92), (-13,-88), (-17,-88), (-17, -92)], 
        [(22,-127), (26,-127), (26, -123), (22, -123), (22,-127)], 
        [(-17,-5), (-13,-5), (-13,-1), (-17,-1), (-17,-5)]])


    def testing_is_position_blocked_True(self):
        cords = [(2,0)]
        self.assertEqual(is_position_blocked(3,0,cords), True)


    def testing_is_position_blocked_False(self):
        cords = [(2, 0)]
        self.assertEqual(is_position_blocked(8,10,cords), False)


    def testing_is_position_blocked_multiple_obs_False(self):
        cords = [(-2,7),(-1,-2),(4,2)]
        self.assertEqual(is_position_blocked(2,6,cords), False)
    
    
    def testing_is_position_blocked_multiple_obs_True(self):
        cords = [(-2,7),(-1,-2),(4,2)]
        self.assertEqual(is_position_blocked(6,2,cords), True)


    def testing_is_path_blocked_False(self):
        cords = [(2,7),(-1,-2),(4,2)]
        self.assertEqual(is_path_blocked(-3,4,0,4,cords), False)


    def testing_is_path_blocked_True(self):
        cords = [(2,7), (-1,-2), (66, 77)]
        self.assertEqual(is_path_blocked(-3,0,5,0,cords), True)


if __name__ == '__main__':
    unittest.main()