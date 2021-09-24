from concurrent.futures import ThreadPoolExecutor
import time

def do_something(seconds, status):
    time.sleep(seconds)
    print(status)

start_time = time.perf_counter()
executor = ThreadPoolExecutor(max_workers=2)
f1 = executor.submit(do_something, 4, 'f1')  # 通过submit提交执行的函数到线程池中
f2 = executor.submit(do_something, 1, 'f2')
f3 = executor.submit(do_something, 1, 'f3')

print(f1.result())
print(f2.result())
print(f3.result())
print(f'task1 is over: {f1.done()}')
print(f'task2 is over: {f2.done()}')

end_time = time.perf_counter() - start_time
print(f'total time: {round(end_time, 2)} sec')

