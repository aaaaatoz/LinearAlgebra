import math

from ._global import EPSILON

class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)


    def __add__(self, another):
        assert len(self) == len(another), "Error adding as length of vectors must be same"
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        assert len(self) == len(another), "Error adding as length of vectors must be same"
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        return Vector([k * element for element in self])

    def __rmul__(self, k):
        return self * k

    def __iter__(self):
        return self._values.__iter__()

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __pos__(self):
        return self

    def __neg__(self):
        return -1 * self

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def norm(self):
        return math.sqrt((sum( e**2 for e in self._values)))

    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("can't normalize the vector")
        return 1 / self.norm() * self

    def __truediv__(self, k):
        return (1/k) * self
