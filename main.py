import os


def traverse_dirs(path, depth=1):
  with os.scandir(path) as it:
    for entry in it:
      print(f'{"-" * depth} {entry.name}')

      if entry.is_dir():
        traverse_dirs(entry.path, depth=(depth + 1))


traverse_dirs('.')
