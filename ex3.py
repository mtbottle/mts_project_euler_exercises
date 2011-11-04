# -*- coding: utf-8 -*-

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

from math import *

def get_factors(num):
  ''' get a list of prime factors of integer num '''
  lst_of_factors = []
  rt = sqrt(num)
  
  for n in range(1,int(rt)):
    if num%n == 0:
      lst_of_factors.append(n)
      lst_of_factors.append(num/n)

  lst_of_factors.sort()

  return lst_of_factors

def get_primes_from_lst(lst):
  ''' given a list of integers, lst, return a list of the primes in that list '''
  primes = []
  for n in lst:
    i = 2
    prime = True
    while i < n/2 and prime == True:
      if n%i==0:
        #print str(n) + " is divisible by " + str(i)
        prime = False
      i += 1
    
    if prime == True:
      primes.append(n)

  primes.sort()
  return primes

if __name__ == "__main__":
  lst = get_factors(600851475143)
  #print lst[len(lst) - 1]
  #print get_primes_from_lst(lst)
  prime = get_primes_from_lst(lst)
  print prime[len(prime) - 1]