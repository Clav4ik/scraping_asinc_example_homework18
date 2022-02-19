from typing import List
import aiohttp
from bs4 import BeautifulSoup as bs
import asyncio

global loop


async def print_url_title(url: str):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36',
        'referer': url
    }
    try:
        async with aiohttp.ClientSession()  as session:
            try:
                response = await session.get(url=url, headers=headers)
            except RuntimeError:
                print('RuntimeError !!!!!!!')
            if response:
                soup = bs(await response.text(), "lxml").title

            if soup != None:
                print(url + ' - ' + soup.text.strip())
            await asyncio.sleep(0)
    except aiohttp.client_exceptions.ClientConnectorError:
        print(url + ' - ' + "No connect")


async def gather_def(list_url: List):
    tasks = []
    for url_one_of in list_url:
        if url_one_of:
            url = ('http://' + url_one_of)
            task = asyncio.create_task(print_url_title(url))
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    list_url = []

    with open("news_sites.txt", "r") as f:
        list_url = f.read().strip(' ').split('\n')
    loop = asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(gather_def(list_url))


