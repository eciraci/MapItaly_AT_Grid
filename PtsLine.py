#!/usr/bin/env python
u"""
Written by Enrico Ciraci'
January 2024

Set of Classes to compute and process a line passing through two points.
"""
# - Python Dependencies
import numpy as np


class PtsLine:
    """
    Class to compute the equation of a line passing through two points.
    """
    def __init__(self, x_pt1: float, y_pt1: float,
                 x_pt2: float, y_pt2: float) -> None:
        if x_pt1 == x_pt2 and y_pt1 == y_pt2:
            raise ValueError("The input points are the same. "
                             "A line cannot be defined by a single point.")
        self.x_1 = x_pt1
        self.y_1 = y_pt1
        self.x_2 = x_pt2
        self.y_2 = y_pt2
        self.m_val = (y_pt2 - y_pt1) / (x_pt2 - x_pt1)
        self.q_val = y_pt1 - (self.m_val * x_pt1)

    def y_val(self, x_pt: float | np.ndarray) -> float | np.ndarray:
        """Return the y coordinate of the line at the given x coordinate."""
        return self.m_val * x_pt + self.q_val

    def x_val(self, y_pt: float | np.ndarray) -> float | np.ndarray:
        """Return the x coordinate of the line at the given y coordinate."""
        if self.m_val == 0:
            return np.inf
        return (y_pt - self.q_val) / self.m_val

    @property
    def slope(self) -> float:
        return self.m_val

    @property
    def intercept(self) -> float:
        return self.q_val

    @property
    def distance(self) -> float:
        return np.sqrt((self.x_2 - self.x_1)**2 + (self.y_2 - self.y_1)**2)

    @property
    def midpoint(self) -> tuple[float, float]:
        return (self.x_1 + self.x_2) / 2, (self.y_1 + self.y_2) / 2

    def is_parallel_to(self, other_line: 'PtsLine') -> bool:
        return np.isclose(self.m_val, other_line.m_val)

    def is_perpendicular_to(self, other_line: 'PtsLine') -> bool:
        return np.isclose(-1, self.m_val * other_line.m_val)


class PtsLineIntersect:
    """
    Class to compute the intersection point of two lines passing through
    two points.
    """
    def __init__(self, line_1: PtsLine, line_2: PtsLine) -> None:
        self.m_1 = line_1.m_val
        self.q_1 = line_1.q_val
        self.m_2 = line_2.m_val
        self.q_2 = line_2.q_val

    @property
    def intersection(self) -> tuple[float, float]:
        """
        Compute the intersection point of two lines.
        Returns: Coordinates of the intersection point tuple[float, float].
        """
        x_c = None
        y_c = None
        try:
            x_c = (self.q_2 - self.q_1) / (self.m_1 - self.m_2)
            y_c = self.m_1 * x_c + self.q_1
        except ZeroDivisionError:
            print("# - Lines are parallel.")
        return x_c, y_c
