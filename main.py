from typing import List

import aiohttp
from bs4 import BeautifulSoup as bs
import asyncio


async def get_response(url_one_of: str):

    url = ('http://' + url_one_of)
    async with aiohttp.ClientSession as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return response.text()



async def get_title(html):
    soup = bs(html, "lxml").title
    return soup


async def get_range_url():
    list_url = []
    list_text = []
    with open("news_sites.txt", "r") as f:
        list_url = f.read().strip('').split('\n')
    for url in list_url:
        list_text.append((url, loop.create_task(get_response(url))))
    for url, t in list_text:
        html = await t
        title = get_title(html)
        if title != None:
            print(url + ' - ' + title)
        else:
            print(url + ' - ' + 'None')

def main():
    global loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_range_url())



if __name__=='__main__':
    main()
# class AsyncIter:
#     def __init__(self, items):
#         self.items = items
#
#     async def __aiter__(self):
#         for item in self.items:
#             yield item
#
#
#
# async def print_url_title(list_url: List, data: asyncio.Queue):
#     for url in list_url:
#             response = ''
#             try:
#                 response = requests.get('http://' + url)
#                 soup = bs(response.text, "lxml").title
#             except requests.exceptions.ConnectionError or AttributeError :
#                 soup =None
#                 print("No connect")
#             if soup!=None:
#                 print(url+' - '+soup.text)
#             else:
#                 print(url+' - '+'None')
#             await asyncio.sleep(0)
# if __name__=='__main__':
#     loop = asyncio.get_event_loop()
#     data = asyncio.Queue()
#     list_url = []
#     with open("news_sites.txt", "r") as f:
#         list_url = f.read().strip('').split('\n')
#
#     task1 = loop.create_task(print_url_title(list_url, data))
#     finaly_task = asyncio.gather(task1)
#     loop.run_until_complete(finaly_task)
#     loop.close()


