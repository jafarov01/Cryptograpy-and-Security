import random, string

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

def bruteForceGuess(chiperText):
    #create a list of English Lowercase Letters
    letters = string.ascii_lowercase

    #iterate over the indices of each letter of letters
    print("KEY\tGUESS\n")
    for key in range(len(letters)): # 0 - 25
        guess = ""
        #iterate over each characters of the encrypted word
        for ch in chiperText:
            if ch in letters: #if the character is lowercase English word
                index = letters.find(ch) #find the index of the character in the list
                #find the encrypted (guessed) character
                index = (index - key) % 26
                guess = guess + letters[index]
            else:
                guess = guess + ch
        print(key, "\t", guess)

###############################################

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

print('\n=-=-=-=-= Bruto Force Attack =-=-=-=-=\n')
bruteForceGuess(encryptedText)
