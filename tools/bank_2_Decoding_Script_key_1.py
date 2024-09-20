import random
import string

def decode_phrase(encoded_phrase, key):
  """Decodes a phrase using a key."""
  decoded_phrase = ""
  i = 0
  while i < len(encoded_phrase):
    # Skip non-alphabetic characters
    if not encoded_phrase[i].isalpha():
      i += 1
      continue
    # Decode the character using the key
    shift = ord(key[i % len(key)]) % 26
    decoded_char = chr((ord(encoded_phrase[i]) - shift - 97) % 26 + 97)
    decoded_phrase += decoded_char
    i += 1
  return decoded_phrase

if __name__ == "__main__":
  encoded_phrase = input("Enter an encoded phrase: ")
  key = "your_secret_key"  # Replace with the correct key
  decoded = decode_phrase(encoded_phrase, key)
  print("Decoded phrase:", decoded)