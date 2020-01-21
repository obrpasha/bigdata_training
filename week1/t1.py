#! /usr/bin/env python
# -*- coding: utf-8 -*-

def print_kwargs(**kwargs):
  for key, value in kwargs.items():
    print("{}={}".format(key, value))


def print_args(*args):
  for idx, value in enumerate(*args):
    print("arg[{}]={}".format(idx, value))


def logger(func):
  def inner(*args, **kwargs):
    print("===============Call function: {}===============".format(func.__name__))
    print("*******positional args*******")
    print_args(args)
    print("*********keyword args********")
    print_kwargs(**kwargs)

    res = func(*args, **kwargs)
    print("Result: {}".format(res))
    print("==================================================")

    return res

  return inner


@logger
def adder(a, b, c):
  return a + b + c;


@logger
def adder_multi_params(*args, **kwargs):
  res = 0
  for value in args:
    res += value

  for value in kwargs.values():
    res += value

  return res


def main():
  a = adder(1, 2, 3)
  b = adder(a=2, b=3, c=4)

  c = adder_multi_params(1, 2, 3)
  d = adder_multi_params(x1=1, x2=2, x3=3)


if __name__ == "__main__":
  main()
