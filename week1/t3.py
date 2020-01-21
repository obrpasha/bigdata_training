#! /usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import threading

singleton_lock = threading.Lock()
lazy_singleton_lock = threading.Lock()
lock = threading.Lock()
lock = threading.Lock()


def synchronized(lock):
  def wrapper(f):
    @functools.wraps(f)
    def inner_wrapper(*args, **kw):
      with lock:
        return f(*args, **kw)

    return inner_wrapper

  return wrapper


def thread_func(n):
  for i in range(n):
    s = singleton();
    s.print_hello()
    lazy_singleton.get_instance().print_hello()


class singleton(object):

  @synchronized(singleton_lock)
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(singleton, cls).__new__(cls)
    return cls.instance

  def print_hello(self):
    print("singleton: ThreadID: {} self {}".format(threading.current_thread().ident, self))


class lazy_singleton:
  __instance = None

  # def __init__(self):
  #   if not lazy_singleton.__instance:
  #     print(" __init__ method called..")
  #   else:
  #     print("Instance already created:", self.get_instance())

  @classmethod
  @synchronized(lazy_singleton_lock)
  def get_instance(cls):
    if not cls.__instance:
      cls.__instance = lazy_singleton()
    return cls.__instance

  def print_hello(self):
    print("lazy_singleton: ThreadID: {} self {}".format(threading.current_thread().ident, self))


class Borg:
  __shared_state = {}

  def __init__(self, x):
    self.__dict__ = self.__shared_state

    self.x = x
    pass

  def print_hello(self):
    print("Borg: ThreadID: {} self {} x: {}".format(threading.current_thread().ident, self, self.x))


def main():
  b1 = Borg(1)
  b1.print_hello()

  b2 = Borg(2)

  b1.print_hello()
  b2.print_hello()

  threads_count = 10
  threads = []

  for i in range(threads_count):
    thread = threading.Thread(target=thread_func, args=(10000,))
    thread.start()
    threads.append(thread)

  for t in threads:
    t.join()

  print("thread finisheds...exiting")


if __name__ == "__main__":
  main()
