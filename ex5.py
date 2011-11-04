# -*- coding: utf-8 -*-

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

################################################################################
''' Method 1, take the min the number of prime factors shared between all terms '''

def get_prime_factors(num):
  ''' returns a list of the primes factors up to num '''

def get_rid_of_multiples(lst):
  ''' removes values in list if they are a direct factor of a larger number'''
  lst.sort()
  new_lst = lst[:] # [:] is to copy the lst
  lst.reverse()
  
  for n in lst:
    i = 0
    while i < len(new_lst) - 1 and n > new_lst[i]:
      if n%new_lst[i]==0:
        new_lst.remove( new_lst[i] )
      else:
        i += 1

  return new_lst

def least_common_multiple(lst):
  ''' return the least common multiple of the numbers in lst
  also assumes that all values appear only once in list
  should hold lists of prime factors in dictionaries?'''
  return True

###############################################################################
''' Method 2: brute force... not useful '''

def product_of_lst(lst):
  product = 1
  for i in lst:
    product *= i
  return product

def hacked_least_common_multiple(lst):
  ''' Not the most efficient way of calculating the least common multiple...
  This is brute force and takes > 30secs at least to compute...'''
  i = max(lst)
  while True:
    k = 0
    for n in lst:
      if i%n == 0:
        k += 1
    
    if k == len(lst) - 1:
      return i
    else:
      i += 1
      print i

if __name__ == "__main__":
  print product_of_lst(range(10,21))
  #print hacked_least_common_multiple(range(1,21))

  # Did this on paper, should find a way to automate this...
  num = 11 * 2**4 * 13 * 17 * 19 * 3**2 * 7 * 5
  for i in range(1,21):
    print num%i
  print num