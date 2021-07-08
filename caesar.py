import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
def caeser(text,shift,direction):
  if(direction == "decode"):
    shift *= -1
  cipher_text = ""
  for letter in text:
    if letter  in alphabet:
      position = alphabet.index(letter)
      new_position = (position + shift+ 26)%26
      new_letter = alphabet[new_position]
      cipher_text +=  new_letter
    else:
      cipher_text += letter
  print(f"{direction} text is {cipher_text}")

want_to_decode = True
while want_to_decode:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(text,shift,direction)
  con_tinue = input("Type yes to continue and no to stop:\n")
  print("\n")
  if(con_tinue.lower() == "no"):
    print("Good bye")
    want_to_decode = False

