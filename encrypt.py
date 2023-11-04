import random
import argparse

def encrypt(input_file_name, output_file_name, key_file_name):
  input_file = open(input_file_name, 'rb')
  output_file = open(output_file_name, 'wb')
  otp_key_file = open(key_file_name, 'wb')

  mod = 255

  while True:
    curr_byte = input_file.read(1);

    if not curr_byte:
      input_file.close()
      otp_key_file.close()
      break

    curr_key = random.randint(0, mod)

    enc_val = (int.from_bytes(curr_byte) + curr_key) % mod
    print(f"{int.from_bytes(curr_byte)} + {curr_key} => {enc_val}")

    otp_key_file.write(curr_key.to_bytes())
    output_file.write(enc_val.to_bytes())


args = argparse.ArgumentParser()

args.add_argument("-i", "--input-file", help="file name for input file")
args.add_argument("-o", "--output-file", help="file name for output file")
args.add_argument("-k", "--key-file", help="file name for otp key")

parsed_args = args.parse_args()

encrypt(parsed_args.input_file, parsed_args.output_file, parsed_args.key_file)
