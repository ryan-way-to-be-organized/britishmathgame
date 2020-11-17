import sys
import itertools
from expressionNode import ExpressionNode

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

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("7 Arguments Required")
        sys.exit(1)

    nums = [int(sys.argv[i]) for i in range(1, 7)]
    target = int(sys.argv[-1])

    g = Generator()
    print(str(g.findTarget(nums, target)) + "=" + str(target))

