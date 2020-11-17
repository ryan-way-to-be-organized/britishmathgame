import itertools
from ExpressionNode import ExpressionNode

class Generator:

    def getOperatorPermutations(self):
        for i in itertools.permutations([i for i in range(5)]):
            yield list(i)

    def getOperatorSet(self):
        for i in itertools.combinations_with_replacement([ "+", "-", "*", "/", "-r", "/r"], 5):
            yield list(i)

    def findTarget(self, numbers, target):
        for nums in itertools.permutations(numbers):
            for ops in self.getOperatorSet():
                equation = [ j for i in zip(nums[:-1], ops) for j in i] + [nums[-1]]

                for perms in self.getOperatorPermutations():

                    e = ExpressionNode(equation, perms) 
                    node = e.findTarget(target)

                    if node.eval() == target:
                        return node
        return None
