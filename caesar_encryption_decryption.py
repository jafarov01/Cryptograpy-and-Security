import random

#function definition for encryption
def encrypt (inputText, key):
    '''
    The function gets a text as a string
    and a key. 
    The function returns the encrypted text.
    '''
    encrypted = ""
    for i in range (len(inputText)):
        ch = inputText[i]
        if (ch.isupper()):
            encrypted += chr((ord(ch) + key - 65) % 26 + 65)
        else:
            encrypted += chr((ord(ch)+ key - 97) % 26 + 97)
    return encrypted

def decrypt (encrypted, key):
    '''
    The function gets the encrypted text 
    as a string and the key. 
    The function returns the decrypted text.
    '''
    actualText = ""
    for i in range (len(encrypted)):
        char = encrypted[i]
        if (char.isupper()):
            actualText += chr((ord(char) - key - 65) % 26 + 65)
        else:
            actualText += chr( (ord(char) - key - 97) % 26 + 97)
    return actualText

#prompt the user to enter the text to be sent
inputText = input("Enter the text: ")

#the key value is randomly found
#it will be sent to the receiver in other means of contacting
key = random.randint(0, 25) #between 0 and 25

#encrypt the input text with the defined key
#the encrypted text is assigned to the new variable
encryptedText = encrypt(inputText, key)

print('\n=-=-=-=-= Encryption =-=-=-=-=\n')
print("The text to be sent: ", inputText, '\n')
print("The encrypted text: ", encryptedText, '\n\n')

print('\n=-=-=-=-= Decryption =-=-=-=-=\n')
print("The encrypted text: ", encryptedText, '\n')
print("The decrypted actual text: ", decrypt(encryptedText, key))