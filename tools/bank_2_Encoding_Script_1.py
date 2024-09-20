import random
import string

def encode_phrase(phrase, key):
  """Encodes a phrase using a key, expanding it to approximately 10 times its original size."""
  encoded_phrase = ""
  for char in phrase:
    # Randomly insert between 0 and 5 random characters before each character
    encoded_phrase += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0, 5)))
    # Encode the character using a simple shift cipher based on the key
    shift = ord(key[len(encoded_phrase) % len(key)]) % 26
    encoded_char = chr((ord(char) + shift - 97) % 26 + 97)
    encoded_phrase += encoded_char
  # Add random characters at the end
  encoded_phrase += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(0, 20)))
  return encoded_phrase

if __name__ == "__main__":
  phrase = input("Enter a phrase: ")
  key = "your_secret_key"  # Replace with your desired key
  encoded = encode_phrase(phrase, key)
  print("Encoded phrase:", encoded)
