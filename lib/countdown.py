# your code goes here!
import time

def countdown(number):
    count = number

    while count >= 0:
        if count == 0:
            print("HAPPY NEW YEAR!")
        else:
            print(f"{count} SECOND(S)!")
        count -= 1



def countdown_with_sleep(number) :
  count = number

  while count != 0:
      print(f"{count} SECOND(S)!")
      count -= 1
      time.sleep(1)
  print('HAPPY NEW YEAR!')

