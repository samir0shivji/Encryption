import copy
# encryption = "the" return 25, 28, 33
def start():
    question = raw_input("Would you like to Encrypt a message?(yes or no)")
    if question.lower().startswith('n'):
        print "Encryption Canceled"
        return False
    elif question.lower().startswith('y'):
        return True

def wordList():
    sent = raw_input("Enter a Sentence to Encrypt: ")
    words = sent.lower().split()
    return words

def encrypt(words):
    flattened = []
    encrypted = []
    for word in words:
        encrypted.append(encryptWord(word))
        encrypted.append(" ")
    encrypted.pop(len(encrypted)-1)
    for x in encrypted:
        for y in x:
            flattened.append(y)
    return encrypted

def encryptWord(word):
    prev = 0
    letters = []
    for i in range(len(word)):
        if i == 0:
            num = (alph.index(word[i])) + 1 + prev
            num += 5
        else:
            num = (alph.index(word[i])) + 1 + prev
        prev = num
        letters.append(num)
    return letters


def decryptWord(word):
    prev = 0
    letters = []

    i = len(word)
    if i ==1:
        word[0] -= 1
        letters.append(alph[word[0]])
        return letters
    for i in range(0, len(word)):
        if i == 0:
            prev = 0
        else:
            prev = word[i-1]
        temp = word[i] - prev -1
        letters.append(alph[temp])
        word[0] -= 5
    return letters



while start():
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    print encrypt(wordList())
    #print "Decryption: "
    #print decryptWord([13, 18, 30, 42, 57])
