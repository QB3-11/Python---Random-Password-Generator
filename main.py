import random 

'''
Defining a function named shuffle, which takes a string as input and then converts it 
into a list and then shuffles the list and then joins it again and returns the shuffled
order of the words
'''
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

sign_list = (33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126)

# Selecting 8 characters two random uppercase, two random lowercase, two random numerics and two random signs

chr1 = chr(random.randint(65,90))
chr2 = chr(random.randint(65,90))
chr3 = chr(random.randint(97,122))
chr4 = chr(random.randint(97,122))
chr5 = chr(random.randint(48,57))
chr6 = chr(random.randint(48,57))
chr7 = chr(random.choice(sign_list))
chr8 = chr(random.choice(sign_list))

temppass = chr1 + chr2 + chr3 + chr4 + chr5 + chr6 + chr7 + chr8

password = shuffle(temppass)
print(password)

