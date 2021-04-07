import unittest
from src.game import *
from src.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.rock = Player("Sheldon", "rock")
        self.paper = Player("Leonard", "paper")
        self.scissors = Player("Howard", "scissors")
        self.lizard = Player("Raj", "lizard")
        self.spock = Player("Penny", "spock")

#### Rock wins

    def test_decide_rock_over_scissors(self):
        result = get_preferred_option(self.scissors, self.rock)
        self.assertEqual(self.rock, result)
        

    def test_decide_rock_over_scissors__order_reversed(self):
        result = get_preferred_option(self.rock, self.scissors)
        self.assertEqual(self.scissors, result)
    

    def test_decide_rock_over_lizard(self):
        result = get_preferred_option(self.lizard, self.rock)
        self.assertEqual(self.rock, result)
        

    def test_decide_rock_over_lizard__order_reversed(self):
        result = get_preferred_option(self.rock, self.lizard)
        self.assertEqual(self.lizard, result)


#### Scissors wins  


    def test_decide_scissors_over_paper(self):
        result = get_preferred_option(self.paper, self.scissors)
        self.assertEqual(self.scissors, result)


    def test_decide_scissors_over_paper__order_reversed(self):
        result = get_preferred_option(self.scissors, self.paper)
        self.assertEqual(self.paper, result)
    

    def test_decide_scissors_over_lizard(self):
        result = get_preferred_option(self.lizard, self.scissors)
        self.assertEqual(self.scissors, result)


    def test_decide_scissors_over_lizard__order_reversed(self):
        result = get_preferred_option(self.scissors, self.lizard)
        self.assertEqual(self.lizard, result)


#### Paper wins        
    
    def test_decide_paper_over_rock(self):
        result = get_preferred_option(self.rock, self.paper)
        self.assertEqual(self.paper, result)


    def test_decide_paper_over_rock__order_reversed(self):
        result = get_preferred_option(self.paper, self.rock)
        self.assertEqual(self.rock, result)


    def test_decide_paper_over_spock(self):
        result = get_preferred_option(self.spock, self.paper)
        self.assertEqual(self.paper, result)


    def test_decide_paper_over_spock__order_reversed(self):
        result = get_preferred_option(self.paper, self.spock)
        self.assertEqual(self.spock, result)


#### Spock wins

    def test_decide_spock_over_rock(self):
        result = get_preferred_option(self.rock, self.spock)
        self.assertEqual(self.spock, result)


    def test_decide_spock_over_rock__order_reversed(self):
        result = get_preferred_option(self.spock, self.rock)
        self.assertEqual(self.rock, result)


    def test_decide_spock_over_scissors(self):
        result = get_preferred_option(self.rock, self.spock)
        self.assertEqual(self.spock, result)


    def test_decide_spock_over_scissors__order_reversed(self):
        result = get_preferred_option(self.spock, self.scissors)
        self.assertEqual(self.scissors, result)


#### Lizard wins

    def test_decide_lizard_over_spock(self):
        result = get_preferred_option(self.lizard, self.spock)
        self.assertEqual(self.spock, result)


    def test_decide_lizard_over_spock__order_reversed(self):
        result = get_preferred_option(self.spock, self.lizard)
        self.assertEqual(self.lizard, result)


    def test_decide_lizard_over_paper(self):
        result = get_preferred_option(self.lizard, self.paper)
        self.assertEqual(self.paper, result)


    def test_decide_lizard_over_paper__order_reversed(self):
        result = get_preferred_option(self.paper, self.lizard)
        self.assertEqual(self.lizard, result)
    

    ##### Draws

    def test_decide_paper_draw(self):
        result = get_preferred_option(self.paper, self.paper)
        self.assertEqual("draw", result)


    def test_decide_rock_draw(self):
        result = get_preferred_option(self.rock, self.rock)
        self.assertEqual("draw", result)
        

    def test_decide_scissors_draw(self):
        result = get_preferred_option(self.scissors, self.scissors)
        self.assertEqual("draw", result)


    def test_decide_lizard_draw(self):
        result = get_preferred_option(self.lizard, self.lizard)
        self.assertEqual("draw", result) 


    def test_decide_spock_draw(self):
        result = get_preferred_option(self.spock, self.spock)
        self.assertEqual("draw", result)     
    