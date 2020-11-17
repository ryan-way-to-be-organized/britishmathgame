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


    def generate(self, numbers, target):
        for nums in itertools.permutations(numbers):
            for ops in self.getOperatorSet():
                equation = [ j for i in zip(nums[:-1], ops) for j in i] + [nums[-1]]

                for perms in self.getOperatorPermutations():

                    ret = self.solve(perms, equation[:], target)
                    if ret is not None:
                        print(ret)
                        return


    def solve(self, perms_in, equation, target):
        result_equation = ""
        perms = perms_in

        for i in range(len(perms)):
            for j in range(i, len(perms)):
                    if perms[i] < perms[j]:
                        perms[j] -= 1

        for i in perms:
            i *= 2
            i += 1
            result = 0
            if equation[i] == "+":
                result = equation[i-1] + equation[i+1]
            elif equation[i] == "-":
                result = equation[i-1] - equation[i+1]
            elif equation[i] == "*":
                result = equation[i-1] * equation[i+1]
            elif equation[i] == "/":
                if equation[i-1] % equation[i+1] != 0:
                    break
                result = equation[i-1] / equation[i+1]
            elif equation[i] == "-r":
                result = equation[i+1] - equation[i-1]
            else:
                if equation[i+1] % equation[i-1] != 0:
                    break
                result = equation[i+1] / equation[i-1]

            if result == 0 or result < 0:
                break

            result_equation += "(%s %s %s)" % (equation[i-1], equation[i], equation[i+1])
            equation = equation[:i-1] + [result] + equation[i+2:]


            if target in equation:

                return (result_equation)


