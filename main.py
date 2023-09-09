import tailer
import re
import argparse

parser = argparse.ArgumentParser(
    prog='Usb Log Parser',
    description='Parses syslog logs for new usb connections'
)

parser.add_argument('--file', default="/var/log/syslog")

args = parser.parse_args()

# used named regex groups
regexp_lines = [
    r'.*usb 1-2.*new full-speed USB device number (?P<device_number>\d+) using (?P<driver>\w+).*',
    r'.*usb 1-2.*New USB device found, idVendor=(?P<id_vendor>\w+), idProduct=(?P<id_product>\w+), bcdDevice= (?P<bcd_device>\d+\.\d+).*',
    r'.*usb 1-2.*New USB device strings: Mfr=(?P<mfr>\d+), Product=(?P<product_nr>\d+), SerialNumber=(?P<serial_number>\d+).*',
    r'.*usb 1-2.*Product: (?P<product>(\w+\s?)+).*'
]

usb_device_state = {}

for line in tailer.follow(open(args.file)):
    for reg_index, reg_exp in enumerate(regexp_lines):
        match = match = re.match(reg_exp, line)

        if not match:
            continue

        for group_name, group_value in match.groupdict().items():
            usb_device_state[group_name] = group_value

        # when the last line has been matched we print out results and reset state
        if len(regexp_lines) == reg_index + 1:
            print(f'usb device state {usb_device_state}')
            usb_device_state = {}
