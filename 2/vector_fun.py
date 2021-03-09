import numpy
import math

# S


def mag(vec):
    # Pythagoras
    return numpy.array(math.sqrt(vec[0] ** 2 + vec[1] ** 2))

# S


def mag1(vec):
    return numpy.linalg.norm(vec)

# T


def unit(vec):
    x = vec[0]
    y = vec[1]
    length = mag(vec)
    print(length)
    return numpy.array([x/length, y/length])

# T


def unit1(vec):
    return vec/mag(vec)

# U


def rot90(vec):
    x = vec[0]
    y = vec[1]
    return numpy.array([-y, x])

# V


def scalar_multiply(scalar: float, vec):
    return numpy.array([scalar * v_i for v_i in vec])


def add(vec1, vec2):
    x1 = vec1[0]
    y1 = vec1[1]
    x2 = vec2[0]
    y2 = vec2[1]
    return numpy.array([x1 + x2, y1+y2])

# W
def sub(vec1, vec2):
    x1 = vec1[0]
    y1 = vec1[1]
    x2 = vec2[0]
    y2 = vec2[1]
    return numpy.array([x1 - x2, y1 - y2])

# W
a = [3, 2]
b = [8,7]
c = [1,5]


print(mag1(a))    # S
print(unit1(a))   # T
print(rot90(a))     # U
print(scalar_multiply(2, a))  # V
print(sub(add(a, b), b)) # W
print(numpy.dot(a, a)) # Y
print(mag(a) * mag(a)) # Y
print(numpy.dot(a,b)) # Z
print(numpy.dot(a, rot90(a))) # Æ
