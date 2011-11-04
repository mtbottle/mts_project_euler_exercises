# -*- coding: utf-8 -*-

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6^(th) prime is 13.

#What is the 10001^(st) prime number?

def get_th_prime_slow(n):
  ''' return the n'th prime, not efficient '''
  lst_primes = []
  i = 2
  
  while len(lst_primes) != n:
    not_prime = False
    for k in lst_primes:
      if i%k == 0:
        not_prime = True
    if not_prime == False:
      lst_primes.append(i)
      print i
    i += 1
  
  return lst_primes

if __name__ == "__main__":

  # even getting 20 takes a couple of seconds =.=
  print get_th_prime_slow(10001)