# -*- coding: utf-8 -*-

from math import *

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^(2) + b^(2) = c^(2)

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def get_lst_primes_slow(n):
  ''' Get a list of prime numbers less than n '''
  lst_primes = []
  #lst_primes.append(1)
  i = 2
  while i <= n:
    not_prime = False
    for k in lst_primes:
      if i%k == 0:
        not_prime = True
    if not_prime == False:
      lst_primes.append(i)
      print i
    i += 1

  return lst_primes

def primes(n):
  '''  '''
  ns = range(3,n+1,2)
  lst_of_primes = ns[:]
  i = 3
  
  while i < n:
    for c in ns:
      if c%i == 0 and c/i != 1:
        lst_of_primes.remove(c)
    ns = lst_of_primes[:]
    i += 1
  return lst_of_primes

def sum_prime_sieve2(num):
   primes = range(1, num, 2) # gets rid of primes, but need to append 2
   primes.insert(1, 2)

   i = 3
   while i < sqrt(num):
     primes = [x for x in primes if x % i != 0]
     i += 1   

   return sum(primes)

def sum_prime_sieve(num):
   ''' Given the bound, give the sum of all the primes under num '''
   primes = []
   primes.append(2)

   for n in range(3, num, 2):     
     prime = True
     for i in primes:
       if n % i == 0:
         prime = False
         break
     if prime:
       primes.append(n)
       print n,

   return sum(primes)

if __name__ == "__main__":
  #primes = get_lst_primes_slow(2000000)
  #print sum(primes) + 1
  #print primes(2000000)
  #print sum(primes(100))
  #print sum_prime_sieve2(100)
  print sum_prime_sieve(200)
