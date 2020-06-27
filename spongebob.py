'''
Take input string and output it in the format of sarcastic spongebob meme
Sam Minix
6/23/20
'''
import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def spongebob(text):
    newText = '' #initialize new text
    choice = [True, False] #initialize choices
    
    for i in range(len(text)): #for each letter in text
        new = text[i]
        
        if new in lower: #if the new letter is lowercase, radomly make uppercase
            
            if random.choice(choice): #if the random choice is True
                new = upper[lower.index(new)] #change to upper case letter
                
        elif new in upper: #if uppercase, make lowercase
            new = lower[upper.index(new)]
            
        newText += new #add new letter to new text
        
    return newText 
                
                
            
