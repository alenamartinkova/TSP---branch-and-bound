from math import sqrt


class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other) -> float:
        a = self.x - other.x
        b = self.y - other.y

        return sqrt(a ** 2 + b ** 2)