def area(a, h): 
    """
    Returns area of trianlge
    :param a: size of one of sides
    :type a: float
    :param h: height of the triangle drawn to this side
    :type h: float

    :rtype: float
    :return: area of triangle
    """
    return a * h / 2 


def perimeter(a, b, c):
    """
    Returns perimeter of triangle
    :param a: size of first side
    :type a: float
    :param b: size of second side
    :type b: float
    :param c: size of third side
    :type c: float

    :rtype: float
    :return: perimeter of triangle
    """
    return a + b + c 
