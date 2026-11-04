class Calculator:
    def _negate(self, a):
        return 0 - a

    def _abs(self, a):
        return a if a >= 0 else self._negate(a)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(self._abs(b)):
            result = self.add(result, a)
        return result if b >= 0 else self._negate(result)

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        x, y = self._abs(a), self._abs(b)
        result = 0
        while x >= y:
            x = self.subtract(x, y)
            result += 1
        if (a < 0) != (b < 0):
            if x != 0:
                result += 1
            result = self._negate(result)
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("modulo by zero")
        x, y = self._abs(a), self._abs(b)
        while x >= y:
            x = x - y
        if x == 0:
            return 0
        if a >= 0 and b > 0:
            return x
        if a < 0 and b > 0:
            return y - x
        if a >= 0 and b < 0:
            return x - y
        return self._negate(x)


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))