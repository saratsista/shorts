#! /usr/bin/python


def caesar(cInput,s):
  cOutput = []
  for char in cInput:
    if ord(char) == 32:
      cOutput.append(char)
    else:
      newChar= chr(s+ord(char))
      cOutput.append(newChar)
  output = ''.join(cOutput)
  return output
  
  
def main():
  shift = input('Enter Caesar Shift\n')
  if shift > 26:
    print "Wrong shift value. Please enter a shift value between 1 and 26"

  plain = raw_input('Enter the plain text you want to encrypt\n')
  plainLower = plain.lower() 

  caesarInput = list(plainLower)
  caesarOutput = caesar(caesarInput,shift)
  print caesarOutput
  
if __name__=='__main__':
  main()







