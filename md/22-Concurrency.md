
# Concurrency in Python: Multithreading and Multiprocessing

Concurrency in Python allows for parallel execution of code, which can significantly improve performance for certain types of tasks. Python provides two main approaches to concurrency: **multithreading** and **multiprocessing**.

## Multithreading

Multithreading allows multiple threads to run concurrently within a single process. It's particularly useful for **I/O-bound tasks**.

### Basic Threading Example

```python
import threading
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All workers finished")
```

### Thread Synchronization

When using threads, it's essential to manage shared resources to avoid race conditions. Here’s an example using a lock for synchronization:

```python
import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        current = counter
        time.sleep(0.1)
        counter = current + 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter}")
```

## Multiprocessing

Multiprocessing runs multiple processes in parallel, each with its own Python interpreter and memory space. This approach is beneficial for **CPU-bound tasks**.

### Basic Multiprocessing Example

```python
import multiprocessing
import time

def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")

if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All workers finished")
```

### Sharing Data Between Processes

You can share data between processes using `Value` and `Array`:

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
```

### Process Pools

Process pools are useful for distributing tasks across multiple processes:

```python
from multiprocessing import Pool

def f(x):
    return x * x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

## Choosing Between Threading and Multiprocessing

- **Use threading** for I/O-bound tasks (e.g., network operations, file I/O).
- **Use multiprocessing** for CPU-bound tasks (e.g., complex computations).
- Threading is lighter weight but limited by the **Global Interpreter Lock (GIL)**.
- Multiprocessing has more overhead but can utilize multiple CPU cores.

## Asynchronous Programming

For I/O-bound tasks, consider using asynchronous programming with `asyncio`:

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

## Best Practices

1. Use threading for I/O-bound tasks and multiprocessing for CPU-bound tasks.
2. Be cautious with shared resources in multithreading; use locks when necessary.
3. Avoid sharing mutable state between processes; use message passing or immutable data.
4. Consider using higher-level abstractions like `concurrent.futures` for simpler task management.
5. Profile your code to ensure concurrency is actually improving performance.

## Exercises

1. Create a multithreaded program that downloads multiple files concurrently.
2. Implement a multiprocessing solution to calculate the sum of large arrays in parallel.
3. Use `asyncio` to create a simple asynchronous web scraper that fetches multiple web pages concurrently.

## Key Points

- Multithreading is suitable for I/O-bound tasks but is limited by the GIL.
- Multiprocessing is effective for CPU-bound tasks and can utilize multiple CPU cores.
- Process pools simplify the distribution of tasks across multiple processes.
- Asynchronous programming with `asyncio` is an alternative for I/O-bound concurrency.
- Proper synchronization and data sharing techniques are crucial for concurrent programming.