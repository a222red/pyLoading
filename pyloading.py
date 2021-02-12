from platform import system as os
from os import system as console
from sys import stdout
from time import time
from threading import Thread
from queue import Queue

def load(function, text="Loading...", etime=True):
  if os() == "Linux":
    def loadtext(start):
      print(text)
      console("tput civis")
      if etime == True:
        while funcvalue == None:
          stdout.write(f"\rTime Elapsed: {round(time()-start, 3)} seconds")
          stdout.flush()
      console("tput cnorm")

    def wrapper(*args, **kwargs):
      global funcvalue
      funcvalue = None
      que = Queue()
      funcThread = Thread(target=lambda q, arg1: q.put(function(arg1)), args=(que, *args))
      starttime = time()
      textThread = Thread(target=loadtext, args=(starttime,))
      funcThread.start()
      textThread.start()
      funcThread.join()
      funcvalue = que.get()
      textThread.join()
      console("cls")
      return funcvalue
    return wrapper
  else:
    def loadtext(start):
      print(text)
      if etime == True:
        while funcvalue == None:
          stdout.write(f"\rTime Elapsed: {round(time()-start, 3)} seconds")
          stdout.flush()

    def wrapper(*args, **kwargs):
      global funcvalue
      funcvalue = None
      que = Queue()
      funcThread = Thread(target=lambda q, arg1: q.put(function(arg1)), args=(que, *args))
      starttime = time()
      textThread = Thread(target=loadtext, args=(starttime,))
      funcThread.start()
      textThread.start()
      funcThread.join()
      funcvalue = que.get()
      textThread.join()
      console("cls")
      return funcvalue
    return wrapper