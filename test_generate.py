import unittest
from generate import Generator
from ExpressionNode import ExpressionNode

class GeneratorTest(unittest.TestCase):

    def test_permuatations(self):
        g = Generator()
        self.assertEqual(sum(1 for i in g.getOperatorPermutations()), 120)

    def test_opertatorset(self):
        g = Generator()
        self.assertTrue(any((i == ['+']*5) for i in g.getOperatorSet()))

    def test_permutation_example1(self):
        g = Generator()
        self.assertTrue(any((i[0] == "*") for i in g.getOperatorSet()))

    def test_solve_example1(self):
        g = Generator()
        nums = [ 50, 6, 4, 10, 7 ]
        target = 300
        ops = ["*"]*5
        perms = [0 for i in range(5)]
        equation = [j for i in zip(nums[:-1], ops) for j in i] + [nums[-1]]
        #print(g.solve(perms, equation, target))

    def test_generate_example1(self):
        g = Generator()
        node = g.findTarget([50,2, 6, 4, 10, 7], 300)
        self.assertEqual(node.eval(), 300)

    def test_generate_example2(self):
        g = Generator()
        node = g.findTarget([25, 7, 10, 2, 1, 6], 175)
        self.assertEqual(node.eval(), 175)

    def test_generate_example3(self):
        g = Generator()
        node = g.findTarget([25, 26, 10, 3, 2, 1], 311)
        self.assertEqual(node.eval(), 311)

    def test_generate_example4(self):
        g = Generator()
        node = g.findTarget([5, 6, 4, 50, 75, 25], 184)
        self.assertEqual(node.eval(), 184)
