alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#define a function that checks if input message contains aplphabate only
def contains_only_alphabets (input_str):
    for char in input_str:
        if not char.isalpha():
            return False
    return True

#input plaintext containing only alphabets
while True:
    try:
        msg=input("Input message:")
        #checkingif input string contains alphabets only :dines
        if contains_only_alphabets(msg):
            break
        else:
            print("input message doesnot contain alphabets only")
    except ValueError:
        print("Input is not an alphabet,Try again")
        
        
#input a positive integer (between 1 to 26) as key(shift)
while True:
    try:
        key=int(input("enter a number between 1 and 26"))
        if 1<=key <= 26:
            break
        else:
            print("input is not between 1 and 26,Try again")
    except ValueError:
        print("input is not an integer ,Try again")
        
def caesar_encryption(text,shift):
    encrypted_text=''
    text=text.upper()
    n=len(text)
    for i in range(n):
        c=text[i]
        loc=alpha.find(c)
        newloc = (loc + shift)%26
        encrypted_text += alpha[newloc]
        return encrypted_text
    
def caesar_decryption (encrypted_text, shift):
    decrypted_text=''
    n=len(encrypted_text)
    
    for i in range(n):
        c=encrypted_text[i]
        loc=alpha.find(c)
        newloc = (loc - shift) % 26
        decrypted_text += alpha[newloc]
    return decrypted_text

ciphertext = caesar_encryption(msg,key)
decrypted_text = caesar_decryption(ciphertext,key)
print("Plaintext:",msg)
print("Shift key",key)
print("Ciphertext",ciphertext)
print("Decrypted_text",decrypted_text)

