import numpy;

list = numpy.sort([3, 4, 5, 7, 1, 12, 15, 16])

print(f'Sort list: {list}')

dict = {
  'start': 'a',
  'a': 'b',
  'b': 'c',
  'c': 'd',
  'd': 'e',
  'e': 'f',
  'g': 'e',
  'h': 'a',
}

pointer = 'start'

while pointer in dict:
  print(f'Jumping to {dict[pointer]}')
  pointer = dict[pointer]

unique_entries = set();

for key in dict:
  unique_entries.update(dict[key])

print(f'All unique keys in dict {unique_entries}')

def find_next_three_items(dict, pointer):
  arr = []
  while pointer in dict and len(arr) < 3:
    arr.append(dict[pointer])
    pointer = dict[pointer]

  return (arr[0], arr[1], arr[2])

print(f'Returning tuple from a function {find_next_three_items(dict, "b")}');


print('f Demonstrating range loop')

for index in range(2, len(list), 2):
  print(f'index={index}, value={list[index]}')