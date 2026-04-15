import multiprocessing
import time

def square_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"square:{i*i}")

def cube_numbers():
  for i in range(5):
    time.sleep(1)
    print(f"cube:{i*i*i}")
  
if __name__ == "__main__": # Ye line ensure karti hai ki code sirf ek baar run ho, aur child processes mein dobara execute na ho.
  
## create 2 process 
  p1= multiprocessing.Process(target=square_numbers)
  p2= multiprocessing.Process(target=cube_numbers)

  ## time start
  start_time = time.time()
  ## start the process
  p1.start()
  p2.start()

  ## wait for the process to complete
  p1.join()
  p2.join()

  finished_time = time.time() - start_time
  print(finished_time)