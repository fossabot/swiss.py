#!/usr/bin/env python

import math    


def calculate_change(a, b):
    """ Calculate the difference between the x and y coordinates of two points.
  
    Arguments:
        a (tulpe): The x and y coordinates of the first point.
        b (tuple): The x and y coordinates of the second point.
    
    Returns:
        tuple: A new point containing the difference between the x and y
            coordinates of the points a and b.
            
    Examples:
        >>> calculate_change((1, 1), (1, 1))
        (0, 0)
        >>> calculate_change((1, 1), (3, 3))
        (2, 2)
        >>> calculate_change((5, 2), (-3, 4))
        (-8, 2)
    """
    return b[0] - a[0], b[1] - a[1])


def calculate_distance(a, b):
    """Calculate the geometrical distance between two points.
    
    Arguments:
        a (tuple): The x and y coordinates of the first point.
        b (tuple): The x and y coordinates of the second point.
    
    Returns:
        tuple: A new point containing the geometric distance between the points
            a and b.

    Examples:
        >>> calculate_distance((1, 1), (1, 1))
        0.0
        >>> calculate_distance((1, 1), (3, 3))
        2.8284271247461903
        >>> calculate_distance((5, 2), (-3, 4))
        8.24621125123532
    """
    return math.hypot(*calculate_change(a, b))


# calculate the gradient between two points.
# 
# @param  tuple  a the x and y coordinates of the first point.
# @param  tuple  b the x and y coordinates of the second point.
# 
# @returns  float  the ratio between the change of two points.
def calculate_slope(a, b):
  dx, dy = calculate_change(a, b)
  return dy / dx


# determine if a point lies within a defined circle.
# 
# @param  tuple  point  the x and y coordinates of point to test against.
# @param  tuple  center  the x and y coordinates of the center of the circle.
# @param  int  the radius of the circle. 
# 
# @returns  bool  True if the point lies within the defined circle boundries, 
#                 otherwise False.
def is_in_circle(point, center=(0, 0), radius=1):
    return calculate_distance(center, point) <= radius


def is_in_range(a, b, radius):
  return all(map(lambda (x, y): abs(x - y) < radius, zip(a, b)))


def rotate_point(center, point, theta):
  dx, dy = calculate_change(point, center)
  x = (dx * math.cos(theta)) - (dy * math.sin(theta))
  y = (dy * math.cos(theta)) + (dx * math.sin(theta))
  return x + center[0], y + center[1]


def sort_clockwise(center, points):
  return sorted(points, key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))


def translate_point(center, point, distance):
  distance_old = calculate_distance(center, point)
  x = point[0] + (((point[0] - center[0]) / distance_old) * (distance - distance_old))
  y = point[1] + (((point[1] - center[1]) / distance_old) * (distance - distance_old))
  return x, y
