class Polynomial:
    coeffs = None
    max_degree = None

    def __init__(self, arg):
        self.coeffs = []
        supported_types = [int, list, tuple, Polynomial]

        if type(arg) not in supported_types:
            raise TypeError(
                f"Unsupported data type {type(arg).__name__}. Expected " +
                ", ".join(
                    [
                        type_.__name__ for type_ in supported_types]))

        if type(arg) in [list, tuple]:
            if len(arg) == 0:
                raise ValueError(f"An empty {type(arg).__name__} was given")
            for coef in arg:
                if not isinstance(coef, int):
                    raise TypeError(
                        f"Unsupported data type {type(coef).__name__}. Expected {int.__name__}")
                self.coeffs.append(coef)
        elif isinstance(arg, Polynomial):
            self.coeffs = arg.coeffs.copy()
        else:
            self.coeffs = [arg]

        self.max_degree = len(self.coeffs) - 1

    def __getattribute__(self, attrname):
        if attrname == "max_degree":
            return len(self.coeffs) - 1
        else:
            return object.__getattribute__(self, attrname)

    def __getattr__(self, attrname):
        if attrname == "max_degree":
            return self.max_degree
        elif attrname == "coeffs":
            return self.coeffs
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attrname}'")

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

        for i, coef in enumerate(self.coeffs):
            if coef == 1 and i != self.max_degree:
                string += f"{x_exp(self.max_degree - i)}"
            elif coef == -1 and i != self.max_degree:
                string += f"-{x_exp(self.max_degree - i)}"
            elif coef != 0:
                string += f"{'+' if coef > 0 else ''}{coef}{x_exp(self.max_degree - i)}"
        return string.lstrip("+")

    def __addition__(self, arg, op):
        self_ = Polynomial(self)
        arg_ = Polynomial(arg)

        if self_.max_degree > arg_.max_degree:
            tmp = [0 for i in range(self_.max_degree - arg_.max_degree)]
            tmp.extend(arg_.coeffs)
            arg_.coeffs = tmp
            arg_.max_degree = self_.max_degree
        elif self_.max_degree < arg_.max_degree:
            tmp = [0 for i in range(arg_.max_degree - self_.max_degree)]
            tmp.extend(self_.coeffs)
            self_.coeffs = tmp
            self_.max_degree = arg_.max_degree

        res = Polynomial([0 for i in range(self_.max_degree + 1)])

        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b
        }

        for i in range(self_.max_degree + 1):
            res.coeffs[i] = ops[op](self_.coeffs[i], arg_.coeffs[i])
        return res

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def __add__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(arg).__name__}'")
        return self.__addition__(arg, '+')

    def __radd__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(arg).__name__}'")
        if isinstance(arg, int):
            arg_ = Polynomial(arg)
        return arg_.__add__(self)

    def __sub__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(arg).__name__}'")
        return self.__addition__(arg, '-')

    def __rsub__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(arg).__name__}'")
        if isinstance(arg, int):
            arg_ = Polynomial(arg)
        return arg_.__sub__(self)

    def __mul__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(arg).__name__}'")
        self_ = Polynomial(self)
        arg_ = Polynomial(arg)

        res = Polynomial(
            [0 for i in range(self_.max_degree + arg_.max_degree + 1)])

        for i, l_coeff in enumerate(self_.coeffs):
            for j, r_coeff in enumerate(arg_.coeffs):
                res.coeffs[i + j] += l_coeff * r_coeff

        return res

    def __rmul__(self, arg):
        if type(arg) not in [Polynomial, int]:
            raise TypeError(
                f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(arg).__name__}'")
        if isinstance(arg, int):
            arg_ = Polynomial(arg)
        return arg_.__mul__(self)

    def __eq__(self, arg):
        if type(arg) not in [Polynomial, int]:
            return False
        arg_ = Polynomial(arg)
        self_ = Polynomial(self)

        while self_.coeffs[0] == 0:
            del self_.coeffs[0]
        while arg_.coeffs[0] == 0:
            del arg_.coeffs[0]

        return True if self_.coeffs == arg_.coeffs else False
