# -*- coding: utf-8 -*-

from math import *

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^(2) + b^(2) = c^(2)

#For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

if __name__ == "__main__":
  for i in range(1,999):
    for j in range(1,999):
      k = 1000 - i - j
      if k > 0:
        square = i**2 + j**2
        value = sqrt( float(square) )
        if i**2 + j**2 == k**2:
          print i, j, k
          print i*j*k

