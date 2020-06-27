'''
Accept user input to determine string to modify and if they want a picture modified
Sam Minix
6/26/20
'''
import spongebob
import shop
text = input('Enter a quote: ')
newText = spongebob.spongebob(text)
print(newText)
photo = input('Would you like it on a photo, Y/N? ')
while True:
    if (photo not in ['Y', 'y', 'yes', 'N', 'n', 'no']):
        photo = input('Enter a valid input. would you like a photo Y/N? ')
    else:
        break

if (photo in ['Y', 'y', 'yes']):
    shop.shop(newText)

print("Thanks!")
