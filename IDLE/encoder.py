# encoder.py
message = input("What is the message you would like to encode? \n")
key = eval(input("And what key would you like to use? \n"))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter)
        codedLetter = value + key
        letter = chr(codedLetter)
        if not letter.isupper():
            codedLetter -= 26
            letter = chr(codedLetter)
            
    output += letter

print("Output message: ", output)
