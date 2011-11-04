# -*- coding: utf-8 -*-

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(s):
  ''' given a string s, return true or false to whether s is a palindrome '''
  if len(s) == 0 or len(s) == 1:
    return True
  else:
    return (s[0] == s[len(s) - 1]) and is_palindrome(s[1:len(s)-1])

def largest_three_digit_product_palindrome():
  ''' determine the largest palindrome formed by the product of 2 three digit numbers'''
  palindromes = []
  frst = 999
  flag = False
  while frst > 99:
    scnd = 999
    
    while scnd > 99:
      s = str(frst * scnd)
      if is_palindrome(s) == True:
        palindromes.append(frst*scnd)
        #return s
      scnd -= 1
    
    frst -= 1

  palindromes.sort()
  return palindromes

if __name__ == "__main__":
  lst = largest_three_digit_product_palindrome()
  print lst[-1]