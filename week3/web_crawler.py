import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import time


def is_http_url(s):
  regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

  if s is None:
    return False

  if regex.match(s):
    return True
  else:
    return False


class WebCrawler:
  def __init__(self, url, concurrent_count):
    self.__url = url
    self.__semaphore = asyncio.Semaphore(concurrent_count)
    self.__scanned_sites = []

  async def start(self):
    self.__scanned_sites = []

    async with aiohttp.ClientSession() as session:
      task = asyncio.create_task(self.__scan(session, self.__url))
      await task

  async def __scan(self, session, url):
    # if self.__semaphore.locked():
    #     print("Concurrency limit. Wait...")

    tasks = []
    soup = None

    async with self.__semaphore:
      try:
        async with session.get(url) as response:
          content = await response.text()
          soup = BeautifulSoup(content, "html.parser")
      except BaseException as ex:
        print(print("Error: {}".format(ex)))

      if soup is not None:
        for link in soup.find_all('a'):
          nav_url = link.get('href')

          if is_http_url(nav_url):
            if nav_url not in self.__scanned_sites:
              self.__scanned_sites.append(nav_url)
              print(nav_url)
              tasks.append(asyncio.create_task(self.__scan(session, nav_url)))

    await asyncio.gather(*tasks)


async def main():
  web_crawler = WebCrawler('http://python.org', 20)
  await web_crawler.start()


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
