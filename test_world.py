import sys
import unittest
from unittest.mock import patch
from io import StringIO
from world.text import world

class TestingTextWorld(unittest.TestCase):
    sys.stdout = StringIO()

    def testing_show_position(self):
        name = 'HAL'
        self.assertEqual(world.show_position(name),f' > {name} now at position ({str(world.position_x)},{str(world.position_y)}).' )


    def testing_is_position_allowed_within_range(self):
        self.assertTrue(world.is_position_allowed(40, 60), (40, 60))
    

    def testing_is_position_allowed_outside_range(self):
        self.assertFalse(world.is_position_allowed(101, 201), None)


    def testing_update_position(self):
        self.assertTrue(world.update_position(10), True)
        self.assertFalse(world.update_position(205), False)
        self.assertFalse(world.update_position(-900), False)
        


if __name__ == '__main__':
    unittest.main()