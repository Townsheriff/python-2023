

def encrypt():
  letters = ["S", "E", "C", "R", "E", "T"];
  message_len = len(letters)
  key = ["F", "X", "I", "P", "U", "F"]
  mod = 255;


  encrypted = []
  decrypted = []

  for index in range(message_len):
    print(f"{ord(letters[index])} + {ord(key[index])}")
    enc_letter = (ord(letters[index]) + ord(key[index])) % mod;
    encrypted.append(chr(enc_letter))

  for index in range(message_len):
    
    dec_letter = (ord(encrypted[index]) - ord(key[index])) % mod;
    decrypted.append(chr(dec_letter))


  print(f"{encrypted} => {decrypted}")


encrypt()