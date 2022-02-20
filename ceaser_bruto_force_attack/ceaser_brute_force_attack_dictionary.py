import string, random

def chooseRandomWordFromDict(fileName):
    #open the file
    words = open(fileName)

    #choose the word (line) to be encrypted randomly
    wordIndex = random.randint(0, 370102) #there are 370103 words in the file

    for lineNum, line in enumerate(words):
        if (lineNum == wordIndex):
            return line
    words.close()

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

def bruteForceGuess(fileName, chiperText):
    #create a list of English Lowercase Letters
    letters = string.ascii_lowercase

    #iterate over the indices of each letter of letters
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
        #open the file
        words = open(fileName, "r")
        #search for the guessed word in the file
        # for line in enumerate(words):
        #     word = line[1].strip()
        #     if (guess == word):
        guess = guess + '\n'
        if guess in words: #second way to seach
            print("Guessed word is \"", guess, "\". Key is ", key, ".")
            return key
        #close the file
        words.close()
    return -1 #unseccesful

#######################################################

#open the file
fileName = "words.txt"

#choose the word randomly from the file
randomWord = chooseRandomWordFromDict(fileName)
randomWord = randomWord.strip() #remove the newline character
print("Random word: ", randomWord, "\n")

#the key value is randomly found
#it will be sent to the receiver in other means of contacting
key = random.randint(0, 25) #between 0 and 25

#encrypt the input text with the defined key
#the encrypted text is assigned to the new variable
encryptedText = encrypt(randomWord, key)
print("encrypted: ", encryptedText, "\n")

#call the brute force attack
foundKey = bruteForceGuess(fileName, encryptedText)
print()
if (foundKey == key): #if the guessed key is correct
    print("SUCCESFUL!")
else:
    print("UNSUCCESFUL!")