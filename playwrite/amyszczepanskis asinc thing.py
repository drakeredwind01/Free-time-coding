
'''
Based on its name, it is not suprising that asyncio is commonly used for asynchronous I/O.
The key idea here is that if a task is waiting for something to happen (such as network access or reading from a file), then it can allow other parts of the program to run while it is waiting.
Python can't guess when it's OK to wait or what else we can do while waiting, so we need to tell it. Additionally, our task needs to know how to wait (and how to resume). This is part of what makes asyncio more complicated than our usual functions and methods.
In asyncio, we have coroutines. They look a lot like functions and methods, but they are different in ways that don't matter right now. :)
In order to take advantage of asyncio's ability to schedule tasks, we need an event loop. The event loop keeps track of all of the tasks that we want to run. Tasks indicate that they are OK with being pre-empted by using the "await" keyword.
One typical design pattern is to define our tasks, have the event loop start them running, and then wait for them to finish. If our tasks want to communicate with each other, one way to do this is with a queue. For example, if we have tasks that read from files and tasks that process the data from those files, the readers will put the data that they've read into a queue, and the processers will take data from that queue.
It's fairly common to launch the tasks with asyncio.gather and then wait for them to complete.
'''


"""
Small example that illustrates the speedup from letting something else execute
while waiting for I/O. In this case we are waiting for data from the web.
We can access the sites one at a time (blocking I/O), or we can start each new
request before the previous one returns (non-blocking I/O).


There are two toggles in this example code:
    * Using requests vs. aiohttp (without asyncio).
      Both are blocking in this implementation, so there is no speedup.
    * Using blocking I/O vs. an event loop with tasks launched by asyncio.
      This demonstrates the speedup.

This example does not process the results of the web requests. This is left as
an exercise for the reader. :)

Good resources to learn more: superfastpython.com, realpython.com,
Fluent Python (Luciano Romalho), Effective Python (Brett Slatkin)

This example code is inspired by:
    https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1
    https://superfastpython.com/python-asyncio/
    https://realpython.com/async-io-python/
"""

import aiohttp
import asyncio
from aiohttp import ClientSession
import requests
import time


def get_requests_data(site: str) -> None:
    """Uses requests to get the data with blocking I/O."""
    print(f"Sending HTTP request to {site} with requests")
    requests.get(site)


async def get_aiohttp_data(site: str, session: ClientSession) -> None:
    """Uses aiohttp to get the data with potentially non-blocking I/O."""
    print(f"Sending HTTP request to {site} with aiohttp")
    async with session.get(site) as resp:
        await resp.text()


async def get_data(websites: list[str], session: ClientSession) -> None:
    """Gets data from multiple websites. Does not take advantage of non-blocking I/O.
    You can get the data with either requests or aiohttp by changing which one is
    commented out."""
    for site in websites:
        # switch between these options to see that the performance is the same if you don't have an event loop
        get_requests_data(site)
        # await get_aiohttp_data(site, session)


async def get_data_with_asyncio(websites: list[str], session: ClientSession) -> None:
    """Gets data from multiple websites. Takes advantage of non-blocking I/O."""
    tasks = []
    for site in websites:
        tasks.append(get_aiohttp_data(site=site, session=session))
    await asyncio.gather(*tasks)


async def main():
    """Gets data from websites. Examples of blocking and non-blocking I/O.
    You can get_data, which is blocking, or get_data_with_asyncio, which is non-blocking.
    """

    websites = [
        "http://beastacademy.com",
        "http://census.gov",
        "http://www.amazon.com",
        "http://cnn.com",
        "http://nytimes.com",
        "http://www.gap.com",
    ]

    start = time.time()
    async with ClientSession() as session:
        # Switch between these two options to see the speedup from asyncio
        await get_data(websites, session)
        # await get_data_with_asyncio(websites, session)
    end = time.time()
    print(f"It took {end - start} seconds to get data from the sites")


asyncio.run(main())