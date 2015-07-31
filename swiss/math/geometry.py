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
    return b[0] - a[0], b[1] - a[1]


def calculate_distance(a, b):
    """Calculate the geometrical distance between two points.
    
    Arguments:
        a (tuple): The x and y coordinates of the first point.
        b (tuple): The x and y coordinates of the second point.
    
    Returns:
        float: The geometric distance between the points a and b.

    Examples:
        >>> calculate_distance((1, 1), (1, 1))
        0.0
        >>> calculate_distance((1, 1), (3, 3))
        2.8284271247461903
        >>> calculate_distance((5, 2), (-3, 4))
        8.24621125123532
    """
    return math.hypot(*calculate_change(a, b))


def calculate_slope(a, b):
    """Calculate the gradient between two points.
    
    Arguments:
        a (tuple): The x and y coordinates of the first point.
        b (tuple): The x and y coordinates of the second point.
    
    Returns:
        float: The ratio between the change of the coordinates belonging to the
            two points.

    Examples:
        >>> calculate_slope((1, 1), (1, 1))
        None
        >>> calculate_slope((1, 1), (3, 3))
        1.0
        >>> calculate_slope((5, 2), (-3, 4))
        -0.25
    """
    dx, dy = calculate_change(a, b)
    return None if dx == 0 else dy / dx


def is_in_circle(point, center, radius):
    """Determine if a point lies within a defined circle.
    
    Arguments:
        point (tuple): The x and y coordinates of point to test against.
        center (tuple): The x and y coordinates of the center of the circle.
        radius (float): The radius of the circle. 
    
    Returns:
        bool: True if the point lies within the defined circle boundries,
            otherwise False.

    Examples:
        >>> is_in_circle((1,1), (0, 0), 1)
        True
        >>> is_in_circle((3,3), (1, 1), 1)
        False
        >>> is_in_circle((5,2), (-3, 4), 11)
        True
    """
    return calculate_distance(center, point) <= radius


def is_in_range(a, b, radius):
    """Determine if two points are within a defined radius of each other.
    
    Arguments:
        a (tuple): The x and y coordinates of the first point.
        b (tuple): The x and y coordinates of the second point.
        radius (tuple): The maximum distance between the two points that can be
            considered within the range of acceptability. 
    
    Returns:
        bool: True if either point is within the given radius of the other,
            otherwise False.

    Examples:
        >>> is_in_range((1,1), (0, 0), 1)
        True
        >>> is_in_range((3,3), (1, 1), 1)
        False
        >>> is_in_range((5,2), (-3, 4), 11)
        True
    """
    return all(map(lambda (x, y): abs(x - y) < radius, zip(a, b)))


def rotate_point(center, point, theta):
    """
    
    Arguments:
        name (type):
    
    Returns:
        type:

    Examples:
        >>> function
        result
    """
    dx, dy = calculate_change(point, center)
    x = (dx * math.cos(theta)) - (dy * math.sin(theta))
    y = (dy * math.cos(theta)) + (dx * math.sin(theta))
    return x + center[0], y + center[1]


def sort_clockwise(center, points):
    """
    
    Arguments:
        name (type):
    
    Returns:
        type:

    Examples:
        >>> function
        result
    """
    return sorted(points, key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))


def translate_point(tail, head, distance):
    """Translate a point a specific distance along a vector starting from the
        vector's tail.
    
    Arguments:
        tail (tuple): The x and y coordinates of the tail of the vector.
        head (tuple): The x and y coordinates of the head of the vector.
        distance (float): The geometric distance to translate the point by.
    
    Returns:
        tuple: The x and y coordinates of a point translated by 'distance'
            along the defined vector, relative to it's tail.

    Examples:
        >>> translate_point((0, 0), (1, 1), 1)
        (0.7071067811865475, 0.7071067811865475) 
        >>> translate_point((1, 1), (3, 3), -1)
        (0.29289321881345254, 0.29289321881345254) 
        >>> translate_point((5, 2), (-3, 4), 3)
        (2.089572499564004, 2.7276068751089992) 
    """
    distance_old = calculate_distance(tail, head)
    x = head[0] + (((head[0] - tail[0]) / distance_old) * (distance - distance_old))
    y = head[1] + (((head[1] - tail[1]) / distance_old) * (distance - distance_old))
    return x, y
