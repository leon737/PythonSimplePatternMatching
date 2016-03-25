import unittest
from pattern_matching import match, myempty

class PatternMatchingTests(unittest.TestCase):

    def test_simple(self):
        n = 10
        r = match(n) \
        | (5, 'it is a five!') \
        | (lambda x: x <= 10, 'it is a ten!')
        print(r())

    def test_list(self):
        n = list(range(1, 10))
        r = match(n) \
        | ((), (lambda h, t: (h, t)))
        print(r())


    def test_fact(self):
        def fact(x):
            return (match(x) \
            | (1, 1) \
            | ((), lambda x: x * fact(x -1)))()
        print(fact(5))

    def test_filtered_list(self):
        n = list(range(1, 10))
        def sum_even(x, a):
            return (match(x) \
            | (lambda h, t: h % 2 == 0, lambda h, t: sum_even(t, a + h))
            | ((), lambda h, t: sum_even(t, a))
            | (myempty, a))()

        print(sum_even(n, 0))

