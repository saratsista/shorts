#! /usr/bin/python
import itertools

def nPrime(n):
  primes = [2]
  z=[]
  while len(primes) != n:
    for i in itertools.count(3):
      for j in itertools.count(2):
        if i%j is 0:
          z.append(j) 
        if j==i: break
      if any(z):
        del z[:]
        continue
      else: primes.append(i)
      if len(primes) == n:
        break
  print 'The {0} prime number is {1}'.format(n,primes[-1:])
  
def main():
 n = input('Enter the value of n for nth prime number\n')
 nPrime(n)
 
if __name__=='__main__':
  main()
    
  
        