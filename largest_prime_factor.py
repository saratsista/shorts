'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

y = [i for i in range(1,600851475143) if 600851475143%i is 0]
#print y
z = []
priFac = []
for fac in y:
  if fac>=2:
    [z.append(i) for i in range(2,fac) if fac%i is 0]
  if any(z): 
    del z[:]
    continue
  else:
    priFac.append(fac)
print max(priFac)
    