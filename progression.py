class Progression:
    def __init__(self, start=0) -> None:
        self._current = start

    def advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self.advance()
            return answer
        
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0) -> None:
        super().__init__(start)
        self._increment = increment

    def advance(self):
        self._current += self._increment




class GeometricProgression(Progression):
    def __init__(self, base=2, start=1) -> None:
        super().__init__(start)
        self._base = base

    def advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1) -> None:
        super().__init__(first)
        self._prev = second - first

    def advance(self):
        self._prev, self._current = self._current, self._prev + self._current


def find_fib(n):
    f = FibonacciProgression(2, 2)
    res = [f.__next__() for j in range(n)]

    return res[-1]

    

    
    
    