#decoder.py
message = input("What is the message you would like to decode? \n")
key = eval(input("And what key would you like to use? \n"))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) - key
        letter = chr(value)
        if not letter.isupper():
            value = ord(letter) + 26
            letter = chr(value)
    output += letter

print(output)    
        
