import asyncio
import time
from queue import Queue
from threading import Thread

import requests


class Worker(Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as e:
                # An exception happened in this thread
                print(e)
            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """Add a list of tasks to the queue"""
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


class CAsync:
    def __init__(self):
        self.error = None
        #  Creating a session
        self.session = requests.Session()
        self.results = {}

    @classmethod
    def fetch_async(cls, urls):
        """Fetch list of web pages asynchronously."""
        now = time.time()
        loop = cls.get_or_create_eventloop()  # event loop
        future = asyncio.ensure_future(cls.fetch_all(urls, loop))  # tasks to do
        done = loop.run_until_complete(future)  # loop until done
        time_taken = time.time() - now
        print(time_taken)
        print("---------------DATA-FETCH")
        for d in done:
            print(d.json())
        return done

    def get_or_create_eventloop():
        """Open thread."""
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(
                ex
            ) or "Event loop is closed" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return asyncio.get_event_loop()

    async def fetch_all(urls, loop):
        """Responses."""
        tasks = []  # dictionary of start times for each url
        for url in urls:
            task = loop.run_in_executor(None, requests.get, url)
            tasks.append(task)  # create list of tasks
        done = await asyncio.gather(*tasks)  # gather task responses
        return done

    def fetch_async_thread(self, urls):
        pool = ThreadPool(len(urls))
        now = time.time()
        pool.map(self.get_url, urls)
        pool.wait_completion()
        time_taken = time.time() - now
        return self.results
        print(time_taken)

    def get_url(self, url):
        i = url.split("/")[-1]
        r = self.session.get(url)
        self.results[i] = r.json()
