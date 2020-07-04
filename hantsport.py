from itertools import permutations 
import ast

equations =[
'w+i+n+g+s = 56',
'p+i+z+z+a                  =67',
's+u+b	                  =42',
'x+l+s+u+b             =90',
'j+r+s+u+b                  =	83',
'p+e+p+p+e+r+o+n+i	                  =116',
'g+r+e+e+k                  =	63',
'h+a+w+a+i+i+a+n	                  =127',
'v+e+g+g+i+e                  =66',
'b+b+q	                  =45',
'w+o+r+k+s                  =57',
'c+h+e+e+s+e	                  =78',
'h+a+m               =36',
't+u+r+k+e+y                  =	80',
'r+o+a+s+t+b+e+e+f	                  =126',
'b+l+t                  =38',
'c+l+u+b                  =	59',
'd+e+l+i	                  =81',
'd+o+n+a+i+r                  =	99',
'f+r+i+e+s                  =92',
'p+o+p	                  =30',
'l+g+d+o+n+a+i+r                  =	130',
'p+o+u+t+i+n+e=75',
'j+r                 =41',
'x+l                 =48',
'l+g                 =31',
'h+a                  =34',
'v+o+o+m                 =15',
'd+r               =49',
'x+x+l                  =	74'
]    

equations = [equation.replace('=','==') for equation in equations] # Just changes single = to == because I'm going to use this as python code later.

alphabet = [] # Will contain [A,B,C,D]
tests = [] # Will contain executable tests

for equation in equations:
    for character in ast.walk(ast.parse(equation)): # This just reads through the typed in equations
        if isinstance(character, ast.Name) and character.id not in alphabet:
            alphabet.append(character.id) # It saves one copy of each letter in a list. e.g. [A,B,C,D]
    tests.append(compile(equation, '<string>', 'eval'))

alphabet.sort() # put letters in alphabetical order
numbers = [n for n in range(1,len(alphabet) + 1)] # Gets me numbers 1,2,3...n where n is how many letters were found in the equations

out = 'Output: '
for permutation in permutations(numbers,len(alphabet)): 
    letterNumberCombo = zip(alphabet,list(permutation))
    for letter,number in letterNumberCombo:
        locals()[letter] = number
    for test in tests:
        if not eval(test): break
    else:
        for letter,number in letterNumberCombo:
            out += '{}-{}, '.format(letter,number)
        break
        
print(out) 
