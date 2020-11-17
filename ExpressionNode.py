class ExpressionNode:

    def __init__(self, expression, order):
        if len(order) > 0:
            operator_index = (order[-1]*2)+1
            self.operator = expression[operator_index]
            
            left_expr = expression[:operator_index]
            right_expr = expression[operator_index+1:]
            
            left_order = [i for i in order if i < order[-1]]
            right_order = [(i-order[-1]-1) for i in order if i > order[-1]]

            self.lhs = ExpressionNode(left_expr, left_order)
            self.rhs = ExpressionNode(right_expr, right_order)
            self.value = None
        else:
            self.value = expression[0]
            self.operator = None


    def __str__(self):
        if self.operator is None:
            return str(self.value)

        l_string = ("%s" if self.lhs.operator is None else "(%s)") % self.lhs
        r_string = ("%s" if self.rhs.operator is None else "(%s)") % self.rhs

        if self.operator == "-r" or self.operator == "r/":
            return r_string + self.operator[0] + l_string
        else:
            return l_string + self.operator + r_string


    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.eval() == other.eval()

    def eval(self):
        if self.value is not None:
            return self.value
        
        #operator validation
        lvalue = self.lhs.eval()
        rvalue = self.rhs.eval()
        if lvalue < 1 or rvalue < 1:
            return -1
        
        if self.operator == "+":
            self.value = lvalue + rvalue
            return lvalue + rvalue
        elif self.operator == "-":
            self.value = lvalue - rvalue
            return lvalue - rvalue
        elif self.operator == "*":
            self.value = lvalue * rvalue
            return lvalue * rvalue
        elif self.operator == "/":
            self.value = lvalue / rvalue
            return lvalue / rvalue
        elif self.operator == "-r":
            self.value = rvalue - lvalue
            return rvalue - lvalue
        else:
            self.value = rvalue / lvalue
            return rvalue / lvalue

    def findTarget(self, target, verbose=False):
        
        if self.operator is not None:
            lhs = self.lhs.findTarget(target, verbose)
            rhs = self.rhs.findTarget(target, verbose)

            if lhs.eval() == target:
                return lhs
            elif rhs.eval() == target:
                return rhs

        return self

