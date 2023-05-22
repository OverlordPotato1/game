

class switch:
    def __init__(self, variable):
        self.variable = variable

    def case(self, test):
        return self.variable == test

    def __call__(self, test):
        return self.case(test)