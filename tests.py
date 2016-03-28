import unittest
from pattern_matching import match, empty

class PatternMatchingTests(unittest.TestCase):

    def test_simple(self):
        n = 10
        m = match(n) \
        | (5, 'it is a five!') \
        | (lambda x: x <= 10, 'it is a ten!')
        r = m()
        self.assertEqual('it is a ten!', r)

    def test_list(self):
        n = list(range(1, 10))
        m = match(n) \
        | ((), (lambda h, t: (h, t)))
        r = m()
        self.assertEqual((1, [2, 3, 4, 5, 6, 7, 8, 9]), r)


    def test_fact(self):
        def fact(x):
            return (match(x) \
            | (1, 1) \
            | ((), lambda x: x * fact(x -1)))()
        self.assertEqual(120, fact(5))

    def test_filtered_list(self):
        n = list(range(1, 10))
        def sum_even(x, a):
            return (match(x) \
            | (lambda h, t: h % 2 == 0, lambda h, t: sum_even(t, a + h))
            | (empty, a)
            | ((), lambda h, t: sum_even(t, a)))()
        self.assertEqual(20, sum_even(n, 0))

    def test_type(self):
        m = match() \
        | (int, 'it is an integer') \
        | (str, 'it is a string')
        self.assertEqual('it is an integer', m(5))
        self.assertEqual('it is a string', m('hello'))

    def test_multiple(self):
        m = match() \
        | ([1, 2, 3], 'below 4') \
        | ([4, 5, 6], 'above 3')
        self.assertEqual('below 4', m(2))
        self.assertEqual('above 3', m(6))