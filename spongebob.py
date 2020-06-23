'''
Take input string and output it in the format of sarcastic spongebob meme
Sam Minix
6/23/20
'''
import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def spongebob(text, count):
    if count == 250:
        return text #return input if 50 recursions
    newText = '' #initialize new text
    choice = [True, False] #initialize choices
    for i in range(len(text)): #for each letter in text
        new = text[i]
        if new in lower: #if the new letter is lowercase
            if random.choice(choice): #if the random choice is True
                new = upper[lower.index(new)] #change to upper case letter
        elif new in upper: #same if uppercase
            if random.choice(choice):
                new = lower[upper.index(new)]
        newText += new #add new letter to new text
    #print(newText)
    return spongebob(newText, count + 1) #recursive call to help randomize


print(spongebob('Who lives in a Pineapple Under the Sea', 0))
                
                
            
