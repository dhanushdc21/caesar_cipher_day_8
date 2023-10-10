from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

print(logo)
restart=""
def ceasar(direction,text,shift):
  if direction[0]=='e':
    if shift>26:
      shift=shift%26    #If the person entors a shift number greater than 26, we will modify it to be such thst to which we can calculate
    cipher_text=""
    for letter in text:
      if letter in alphabet:
        if (shift+alphabet.index(letter))>=26:  #If the letter need to go back to the beginning because it exceeds its limit
            cipher_text+=alphabet[shift-(26-alphabet.index(letter))]
        else:
            cipher_text+=alphabet[alphabet.index(letter)+shift]
      else:
        cipher_text+=letter
    print(f"The encoded text is {cipher_text}")
    
  elif direction[0]=='d':
     if shift>26:
       shift=shift%26  #If the person entors a shift number greater than 26, we will modify it to be such thst to which we can calculate
     plain_text=""
     for letter in text:
       if letter in alphabet:
         if (alphabet.index(letter)-shift)<0: #If the letter goes below "a" then we execute as a circular loop and start from the end
           plain_text+=alphabet[26-(shift-alphabet.index(letter))]
         else:
           plain_text+=alphabet[alphabet.index(letter)-shift]
       else:
         plain_text+=letter
     print(f"The decoded text is {plain_text}") 
  else:
    print("Wrong choice my friend, \nWrong Choice.")
end=False
while not end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(direction,text,shift)
  restart=input("Do you want to run again? :").lower()
  if restart[0]!='y':
    end=True
    print("GoodBye.")
    