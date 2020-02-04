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


visited_sites = []

sem = asyncio.Semaphore(20)




async def scan_site(session, url):
    # if sem.locked():
    #     print("!!!!!!!!!!!!!!!!!!!!LOCKED!!!!!!!!!!!!!!!!!!!")

    tasks = []
    async with sem:

        async with session.get(url) as response:
          site_content = await response.text()
          soup = BeautifulSoup(site_content, 'html.parser')

        for link in soup.find_all('a'):
          site_url = link.get('href')
          # print(site_url)

          if is_http_url(site_url):
            if site_url not in visited_sites:
              visited_sites.append(site_url)
              print(site_url)
              #print(f"1 task {time.strftime('%X')}")
              task = asyncio.create_task(
                scan_site(session, site_url))
              tasks.append(task)
              #print(f"2 task {time.strftime('%X')}")

    await asyncio.gather(*tasks)


async def main():
  async with aiohttp.ClientSession() as session:
    task = asyncio.create_task(scan_site(session, 'http://python.org'))
    await task


if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
