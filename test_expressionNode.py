import unittest
from ExpressionNode import ExpressionNode

class ExpressionNodeTest(unittest.TestCase):

    def test_init_value(self):
        expression = [9]
        order = []
        e = ExpressionNode(expression, order)

        self.assertEqual(e.operator, None)
        self.assertEqual(e.value, 9)

    def test_init_expression_simple(self):
        expression = [ 9, "+", 18 ]
        order = [0]
        e = ExpressionNode(expression, order)

        self.assertEqual(e.operator, "+")
        self.assertEqual(e.lhs.operator, None)
        self.assertEqual(e.rhs.operator, None)
        self.assertEqual(e.lhs.eval(), 9)
        self.assertEqual(e.rhs.eval(), 18)

        self.assertEqual(e.eval(), 27)

    def test_init_expression_complex(self):
        expression = [ 9, "+", 18, "-", 4, "+", 5 ]
        order = [0, 2, 1]
        e = ExpressionNode(expression, order)

        self.assertEqual(e.operator, "-")

        self.assertEqual(e.lhs.operator, "+")
        self.assertEqual(e.lhs.lhs.operator, None)
        self.assertEqual(e.lhs.rhs.operator, None)

        self.assertEqual(e.rhs.operator, "+")
        self.assertEqual(e.rhs.lhs.operator, None)
        self.assertEqual(e.rhs.rhs.operator, None)
        
        self.assertEqual(e.lhs.lhs.eval(), 9)
        self.assertEqual(e.lhs.rhs.eval(), 18)
        self.assertEqual(e.rhs.lhs.eval(), 4)
        self.assertEqual(e.rhs.rhs.eval(), 5)

        self.assertEqual(e.lhs.eval(), 27)
        self.assertEqual(e.rhs.eval(), 9)

        self.assertEqual(e.eval(), 18)
    
    def test_findTarget(self):

        expression = [ 9, "+", 18, "-", 5, "+", 5 ]
        order = [0, 2, 1]
        e = ExpressionNode(expression, order)

        node = e.findTarget(27)
        self.assertEqual(e.lhs.eval(), 27)

        node = e.findTarget(9)
        self.assertEqual(e.lhs.lhs.eval(), 9)
        
        node = e.findTarget(18)
        self.assertTrue(e.lhs.rhs.eval(), 18)
