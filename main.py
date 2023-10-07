from concurrent.futures import ThreadPoolExecutor
import threading
import hashlib
import signal
import time

text = "abc"
md5 = "aaaa5d16ca437bd4564f25ec0cb71c9d" 
thread_count = 24
shared_bool = threading.Event()


def handler(sig_num, frame):
    print("Caught sigint")
    shared_bool.set()
    exit(1)
 
signal.signal(signal.SIGINT, handler)

def find_appendix_for_md5(thread_nr, total_threads):
  counter = thread_nr

  while True:
    appendix = text + hex(counter)
    file_with_appendix = text + appendix
    
    md5_guess = hashlib.md5(file_with_appendix.encode()).hexdigest()

    if shared_bool.is_set():
      break

    if md5_guess == md5:
      shared_bool.set()
      print(hex(counter))
      break

    counter += total_threads

    if counter % total_threads ** 5 == thread_nr:
      print(f"Thread {thread_nr} => {counter} => {appendix} ?= {md5_guess}");


with ThreadPoolExecutor(max_workers=thread_count) as executor:  
  for i in range(thread_count):
    executor.submit(find_appendix_for_md5, i, thread_count)