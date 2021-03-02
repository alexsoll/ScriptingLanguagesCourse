class Polynomial:
    coefs = None

    def __init__(self, *args):
        supported_types = [int, list, tuple]
    
        if len(args) != 1:
            raise TypeError("Invalid number of arguments. 1 argument is expected")

        if type(args[0]) not in supported_types:
            raise TypeError("Unsupported data type {}. Expected {}".format(type(args), ", ".join([type_.__name__ for type_ in supported_types])))

        if type(args[0]) in [list, tuple]:
            if len(args[0]) == 0:
                raise ValueError("An empty {} was given".format(type(args[0]).__name__))
            for coef in args[0]:
                if type(coef) != int:
                    raise TypeError("Unsupported data type {0}. Expected {1}".format(type(coef), int))
            self.coefs = args[0]
        else:
            self.coefs = [args[0]]


#a = Polynomial([])
#a = Polynomial(())
b = Polynomial()