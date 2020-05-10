from unittest import TestCase

from jackplan.game.shoe import Shoe

class TestShoe(TestCase):

    def test_constructor(self):
        shoe = Shoe(7)
        self.assertEqual(364, len(shoe.cards))
