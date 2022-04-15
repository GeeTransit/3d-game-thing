from __future__ import annotations

import math
from copy import copy
from dataclasses import dataclass

@dataclass
class Vector:
    x: float = 0
    y: float = 0
    z: float = 0

    @staticmethod
    def getMidpoint(
        a: Vector,
        b: Vector,
    ) -> Vector:
        return Vector(
            x=(a.x + b.x) / 2,
            y=(a.y + b.y) / 2,
            z=(a.z + b.z) / 2,
        )

    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __iadd__(self, other: Vector) -> Vector:
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def __add__(self, other: Vector) -> Vector:
        new = copy(self)
        new += other
        return new

    def __isub__(self, other: Vector) -> Vector:
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    def __sub__(self, other: Vector) -> Vector:
        new = copy(self)
        new -= other
        return new

    def __imul__(self, scalar: float) -> Vector:
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    def __mul__(self, scalar: float) -> Vector:
        new = copy(self)
        new *= scalar
        return new

    def __itruediv__(self, scalar: float) -> Vector:
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self
    def __truediv__(self, scalar: float) -> Vector:
        new = copy(self)
        new /= scalar
        return new
