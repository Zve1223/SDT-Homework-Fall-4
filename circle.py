import math


def area(r):
    """
    Returns area of circle
    :param r: radius of circle
    :type r: float

    :rtype: float
    :return: area of circle
    """
    return math.pi * r * r


def perimeter(r):
    """
    Returns perimeter if circle (length of circumference)
    :param r: radius of circle
    :type r: float

    :rtype: float
    :return: perimeter of circle
    """
    return r * math.pi * 2
