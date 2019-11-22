import math

class Point():
    """
    A two-dimensional Point with an x and an y value

    >>> Point(0.0, 0.0)
    Point(0.0, 0.0)
    >>> Point(1.0, 0.0).x
    1.0
    >>> Point(0.0, 2.0).y
    2.0
    >>> Point(y = 3.0, x = 1.0).y
    3.0
    >>> Point(1, 2)
    Traceback (most recent call last):
        ...
    ValueError: both coordinates value must be float
    >>> a = Point(0.0, 1.0)
    >>> a.x
    0.0
    >>> a.x = 3.0
    >>> a.x
    3.0
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if type(self.x) != float and type(self.y) != float:
            raise ValueError('both coordinates value must be float')

    def __repr__(self):
        return f'{self.__class__.__name__}({str(self.x)}, {str(self.y)})'


def verifica(a, b):
    if type(a) != Point:
        raise ValueError('a must be a Point')
    elif type(b) != Point:
        raise ValueError('b must be a Point')
    

def euclidean_distance(a, b):
    """
    Returns the euclidean distance between Point a and Point b

    >>> euclidean_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    5.0
    >>> euclidean_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> euclidean_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """
    from math import sqrt

    verifica(a, b)
    dist = sqrt( (a.x - b.x)**2 + (a.y - b.y)**2 )

    return dist

def manhattan_distance(a, b):
    """
    Returns the manhattan distance between Point a and Point b

    >>> manhattan_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    7.0
    >>> manhattan_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> manhattan_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """
    from math import fabs

    verifica(a, b)
    dist = fabs( a.x - b.x) + fabs( a.y - b.y)

    return dist

if __name__ == "__main__":
    import doctest
    doctest.testmod()
