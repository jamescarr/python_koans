#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a==b==c==0: raise TriangleError
    elif len([x for x in [a,b,c] if x < 0]): raise TriangleError
    # two sides are less than the value of one side
    elif a == b == c: return 'equilateral'
    elif a == b or b == c or a == c: 
        guard_against_invalid([a, b, c])
        return 'isosceles'
    elif a != b != c: return 'scalene'
    else: raise TriangleError

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass


def guard_against_invalid(points):
    #find the two alike
    two_equal = 0
    largest = 0

    p = points.pop()
    if points.count(p) > 0:
        points.remove(p)
        two_equal = p + p
        largest = points[0]
    else:
        largest = p
        two_equal = points.pop() + points.pop()
    
    if two_equal <= largest:
        raise TriangleError
