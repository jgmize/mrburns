from unittest import TestCase

from nose.tools import eq_, ok_

import lisa


class TestLisaHelpers(TestCase):
    def test_round_coord(self):
        """Should return a float rounded down to 1 decimal"""
        eq_(lisa.round_map_coord(12.345), 12.3)
        eq_(lisa.round_map_coord(12.888), 12.8)
        eq_(lisa.round_map_coord(-12.888), -12.9)
