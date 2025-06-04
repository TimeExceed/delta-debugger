import unittest

def debug_ordered_set(inputs, trial):
    def one_round(xs):
        for s, w in ShrinkIndexIter(len(xs)):
            ys = xs.copy()
            del ys[s:s+w]
            if trial(ys):
                return ys
        return None

    while True:
        nxt = one_round(inputs)
        if nxt is None:
            return inputs
        else:
            inputs = nxt

class ShrinkIndexIter:
    def __init__(self, n):
        self.n = n
        self.w = n
        self.s = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.s += self.w
        if self.s >= self.n:
            self.w //= 2
            self.s = 0
        if self.w == 0:
            raise StopIteration()
        return (self.s, self.w)

class TestOrderedSet(unittest.TestCase):
    def test_one_point(self):
        inputs = [x for x in range(12)]
        res = debug_ordered_set(inputs, lambda x: 6 in x)
        self.assertListEqual(res, [6])

    def test_two_points(self):
        inputs = [x for x in range(12)]
        res = debug_ordered_set(inputs, lambda x: (3 in x) and (7 in x))
        self.assertListEqual(res, [3, 7])

    def test_zero_point(self):
        inputs = [x for x in range(12)]
        res = debug_ordered_set(inputs, lambda _: False)
        self.assertListEqual(res, inputs)

if __name__ == '__main__':
    unittest.main()
