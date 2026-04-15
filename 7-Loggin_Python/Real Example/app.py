import logging

## logging settings
logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
  datefmt='%Y-%m-%d %H:%M:%S',
  force = True,  # this reset existing config
  handlers=[
    logging.FileHandler("app.log"), # create a separate log file
    logging.StreamHandler() # responsible for all the logs shoulb be available in this file 
  ]
)

logger = logging.getLogger("ArithmrticApp")

def add(a,b):
  result = a+b
  logger.debug(f"Adding {a} + {b} = {result}")
  return result

def subtract(a,b):
  result = a-b
  logger.debug(f"Subtracting {a} - {b} = {result}")
  return result

def multiply(a,b):
  result = a*b
  logger.debug(f"Multiplying {a} * {b} = {result}")
  return result

def divide(a,b):
  try:
    result = a/b
    logger.debug(f"Dividing {a} / {b} = {result}")
    return result
  except ZeroDivisionError:
    logger.error("Division by zero error")
    return None
  
add(10,15)
subtract(15,10)
multiply(10,20)
divide(10,2)
