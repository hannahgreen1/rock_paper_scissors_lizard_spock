import unittest
from src.game import *
from src.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.rock = Player("Sheldon", "rock")
        self.paper = Player("Leonard", "paper")
        self.scissors = Player("Howard", "scissors")

    def test_decide_rock_and_scissors(self):
        result = get_preferred_option(self.scissors, self.rock)
        self.assertEqual(self.rock, result)
        
    def test_decide_rock_and_scissors__order_reversed(self):
        result = get_preferred_option(self.rock, self.scissors)
        self.assertEqual(self.scissors, result)
        
    def test_decide_scissors_and_paper(self):
        result = get_preferred_option(self.paper, self.scissors)
        self.assertEqual(self.scissors, result)

    def test_decide_scissors_and_paper__order_reversed(self):
        result = get_preferred_option(self.scissors, self.paper)
        self.assertEqual(self.paper, result)
        
    def test_decide_paper_and_rock(self):
        result = get_preferred_option(self.rock, self.paper)
        self.assertEqual(self.paper, result)

    def test_decide_paper_and_rock__order_reversed(self):
        result = get_preferred_option(self.paper, self.rock)
        self.assertEqual(self.rock, result)

    def test_decide_paper_draw(self):
        result = get_preferred_option(self.paper, self.paper)
        self.assertEqual("draw", result)

    def test_decide_rock_draw(self):
        result = get_preferred_option(self.rock, self.rock)
        self.assertEqual("draw", result)
        
    def test_decide_scissors_draw(self):
        result = get_preferred_option(self.scissors, self.scissors)
        self.assertEqual("draw", result)    
    