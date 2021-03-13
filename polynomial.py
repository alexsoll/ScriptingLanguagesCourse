class Polynomial:
    coefs = None
    max_degree = None

    def __init__(self, arg):
        supported_types = [int, list, tuple, Polynomial]

        if type(arg) not in supported_types:
            raise TypeError(f"Unsupported data type {type(arg).__name__}. Expected " + ", ".join([type_.__name__ for type_ in supported_types]))
        
        if type(arg) is Polynomial:
            self.coefs = arg.coefs.copy()
        else:
            if type(arg) in [list, tuple]:
                if len(arg) == 0:
                    raise ValueError(f"An empty {type(arg).__name__} was given")
                for coef in arg:
                    if type(coef) != int:
                        raise TypeError(f"Unsupported data type {type(coef).__name__}. Expected {int.__name__}")
                self.coefs = arg
            else:
                self.coefs = [arg]

        self.max_degree = len(self.coefs) - 1


    def __str__(self):

        string = ""

        def x_exp(degree):
            if degree == 0:
                r = ""
            elif degree == 1:
                r = "x"
            else:
                r = f"x^{degree}"
            return r

        for i, coef in enumerate(self.coefs):
            if coef == 1 and i != self.max_degree:
                string += f"{'+' if coef > 0 else ''}{x_exp(self.max_degree - i)}"
            elif coef != 0:
                string += f"{'+' if coef > 0 else ''}{coef}{x_exp(self.max_degree - i)}"
        return string.lstrip("+")

    
    def __addition__(self, arg, op):
        self_ = Polynomial(self)
        arg_ = Polynomial(arg)

        if self_.max_degree > arg_.max_degree:
            tmp = [0 for i in range(self_.max_degree - arg_.max_degree)]
            tmp.extend(arg_.coefs)
            arg_.coefs = tmp
            arg_.max_degree = self_.max_degree
        elif self_.max_degree < arg_.max_degree:
            tmp = [0 for i in range(arg_.max_degree - self_.max_degree)]
            tmp.extend(self_.coefs)
            self_.coefs = tmp
            self_.max_degree = arg_.max_degree

        res = Polynomial([0 for i in range(self_.max_degree + 1)])

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b
        }

        for i in range(self_.max_degree + 1):
            res.coefs[i] = ops[op](self_.coefs[i], arg_.coefs[i])
        return res
        

    def __repr__(self):
        return f"Polynomial({self.coefs})"

    
    def __add__(self, arg):
        return self.__addition__(arg, '+')


    def __radd__(self, arg):
        if type(arg) is int:
            arg_ = Polynomial(arg)
        return arg_.__add__(self)


    def __sub__(self, arg):
        return self.__addition__(arg, '-')


    def __rsub__(self, arg):
        if type(arg) is int:
            arg_ = Polynomial(arg)
        return arg_.__sub__(self)


if __name__ == "__main__":

    a = Polynomial([2, 1, -2, -4, 0])
    b = Polynomial([2, 3, 5, 1, 1])

    #print(repr(a))
    print(repr(b))
    c = 2 - b

    print(repr(c))
