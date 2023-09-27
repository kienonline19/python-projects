import time
import random
import queue

from threading import Thread
from concurrent.futures import ThreadPoolExecutor

counter = 0
job_queue = queue.Queue()  # things to be printed out
counter_queue = queue.Queue()  # amounts by which to increase counter


def increment_manager():
    global counter
    while True:
        # this waits until an item available and then locks the queue
        increment = counter_queue.get()
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter + increment
        time.sleep(random.random())
        job_queue.put((f"New counter value is {counter}", "---------"))
        time.sleep(random.random())
        counter_queue.task_done()  # this unlocks queue


Thread(target=increment_manager, daemon=True).start()


def printer_manager():
    while True:
        for line in job_queue.get():
            time.sleep(random.random())
            print(line)

        job_queue.task_done()


Thread(target=printer_manager, daemon=True).start()


def increment_counter():
    counter_queue.put(1)
    time.sleep(random.random())


# worker_threads = [Thread(target=increment_counter) for _ in range(10)]
#
# for thread in worker_threads:
#     time.sleep(random.random())
#     thread.start()
#
# for thread in worker_threads:
#     time.sleep(random.random())
#     thread.join()
with ThreadPoolExecutor(max_workers=10) as pool:
    [pool.submit(increment_counter) for _ in range(10)]

counter_queue.join()
job_queue.join()
