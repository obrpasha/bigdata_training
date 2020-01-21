#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def process_file():
  print("input file name or [x] for exit: ")
  file_name = str(input())

  if file_name == "x":
    return False

  try:
    with open(file_name, 'r', encoding='utf-8') as f:
      for line in f:
        print(line)

        print("Enter - continue/n - new file/x - exit")
        cmd = str(input())

        if cmd == "n":
          return True;

        if cmd == "x":
          return False
  except BaseException as ex:
    print("Error: {}".format(ex))
  except:
    print("Unknown error: {}".format(sys.exc_info()[1]))

  return True


def main_loop():
  process_file_res = True

  while process_file_res:
    process_file_res = process_file()

def main():
  main_loop()


if __name__ == "__main__":
  main()
