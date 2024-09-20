import random

def encode_phrase(phrase):
  """Encodes a phrase by randomly altering characters."""
  encoded_phrase = ""
  for char in phrase:
    if char.isalpha():
      # Randomly shift the character by a random number of positions
      shift = random.randint(-5, 5)
      encoded_char = chr((ord(char) + shift - 97) % 26 + 97)
    else:
      encoded_char = char
    encoded_phrase += encoded_char
  return encoded_phrase

if __name__ == "__main__":
  phrase = input("Enter a phrase: ")
  encoded = encode_phrase(phrase)
  print("Encoded phrase:", encoded)
