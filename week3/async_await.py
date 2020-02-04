import asyncio
import time

async def say_after(delay, what):
    print(f"4 [{what}] say_after 1 at {time.strftime('%X')}")
    await asyncio.sleep(delay)
    #time.sleep(delay)
    print(f"5 say_after 2 at {time.strftime('%X')}")
    print(what)

# async def main():
#     print(f"1 started at {time.strftime('%X')}")
#
#     await say_after(10, 'hello')
#
#     print(f"2 midle at {time.strftime('%X')}")
#
#     await say_after(5, 'world')
#
#     print(f"3 finished at {time.strftime('%X')}")

async def main():
  print(f"1 at {time.strftime('%X')}")
  task1 = asyncio.create_task(
    say_after(5, 'hello'))

  print(f"2 at {time.strftime('%X')}")
  task2 = asyncio.create_task(
    say_after(5, 'world'))

  print(f"3 started at {time.strftime('%X')}")

  # Wait until both tasks are completed (should take
  # around 2 seconds.)
  await task1

  print(f"4 started at {time.strftime('%X')}")

  await task2

  print(f"5 started at {time.strftime('%X')}")

  print(f"finished at {time.strftime('%X')}")

asyncio.run(main())