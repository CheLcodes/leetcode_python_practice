"""
Implementation 3: Use Semaphores
"""

import queue
import threading

orders = queue.Queue()
has_order = threading.Semaphore(value=0)  # ADDED THIS


def serving_line_or_consumer():
    while has_order.acquire():  # ADDED THIS: Acquire a Semaphore, or sleep until the counter of semaphore is larger than zero
        new_order = orders.get()
        # prepare meals from `new_order`, assuming GIL is released while preparing meals
        orders.task_done()


def order_line_or_producer():
    # Each staff in the serving line produces 200 orders
    for _ in range(2):
        orders.put("Order")
        has_order.release() # ADDED THIS: Release the Semaphore, increment the internal counter by 1


# Let's put 4 staff into the order line
order_line = [threading.Thread(target=order_line_or_producer, daemon=True) for _ in range(4)]
# Let's assign 6 staff into the serving line
serving_line = [threading.Thread(target=serving_line_or_consumer, daemon=True) for _ in range(6)]

# Put all staff to work
for t in order_line:
    t.start()
for t in serving_line:
    t.start()

# "join" the order, block until all orders are cleared
orders.join()
# print('orders', orders)
# print(orders.qsize())


# "join" the threads, ending all threads
for t in order_line:
    t.join(1)
for t in serving_line:
    t.join(1)

print('finished!!')