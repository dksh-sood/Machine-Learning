### multiprocessing with ProcessPoolExecutor ==> execute the process fast

from concurrent.futures import ProcessPoolExecutor
import time

def sqaure_number(number):
  time.sleep(2)
  return f"square:{number * number}"

numbers=[1,2,3,4,5]
if __name__=="__main__":
  with ProcessPoolExecutor(max_workers=3) as executor:
    results=executor.map(sqaure_number,numbers)

  for result in results:
    print(result)

