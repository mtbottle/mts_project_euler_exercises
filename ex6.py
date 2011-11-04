# -*- coding: utf-8 -*-

#The sum of the squares of the first ten natural numbers is,
#1^(2) + 2^(2) + ... + 10^(2) = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^(2) = 55^(2) = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
  ''' given a natural number n, return the sum of squares of all the numbers in range of 1 to n '''
  sum = 0
  for i in range(1,n+1):
    sum += i**2
  return sum

def square_of_sum(n):
  ''' given a natural number n, return the square of the sume of all the numbers in range of 1 to n '''
  s = sum(range(1,n+1))
  return s**2

if __name__ == "__main__":
  print square_of_sum(100) - sum_of_squares(100)