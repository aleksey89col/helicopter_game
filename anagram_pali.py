from itertools import permutations
def palindrome(num):
    return num == num[::-1]

with open('dict.txt') as f:
    dic = f.read().splitlines()


palin_list = []

for word in dic :
    if palindrome(word) :
        palin_list.append(word)

for word in palin_list:
    perm_list = [''.join(p) for p in permutations(word)]

    for i in perm_list :
  
        if i in dic and i != word:
            print(i)
            break
  
            
        
        
  
