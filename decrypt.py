import argparse

def decrypt(input_file_name, output_file_name, key_file_name):
  enc_file = open(input_file_name, 'rb')
  key_file = open(key_file_name, 'rb')
  dec_file = open(output_file_name, 'wb')

  mod = 255

  while True:
    enc_byte = enc_file.read(1)
    key_byte = key_file.read(1)

    if not enc_byte:
      enc_file.close()
      dec_file.close()
      key_file.close()
      break

    dec_val = (int.from_bytes(enc_byte) - int.from_bytes(key_byte)) % mod

    dec_file.write(dec_val.to_bytes())


args = argparse.ArgumentParser()

args.add_argument("-i", "--input-file", help="file name for input file")
args.add_argument("-o", "--output-file", help="file name for output file")
args.add_argument("-k", "--key-file", help="file name for otp key")

parsed_args = args.parse_args()

decrypt(parsed_args.input_file, parsed_args.output_file, parsed_args.key_file)