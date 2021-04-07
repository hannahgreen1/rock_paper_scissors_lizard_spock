import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Sheldon", "Rock")

    def test_player_has_name(self):
        self.assertEqual("Sheldon", self.player.name)
    
    def test_player_has_gesture(self):
        self.assertEqual("Rock", self.player.gesture)