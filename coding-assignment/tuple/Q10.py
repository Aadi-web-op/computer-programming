# . Write a Python program to check whether an element exists within a tuple. 
word = input("Enter a word :")
tup = ('dog','cat','sky','people')
if word in tup:
    print(f'The word {word} is in the tuple.')
else:
    print(f'The word {word} is not in the tuple.')