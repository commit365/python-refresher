
## Asynchronous Programming: `asyncio` and Asynchronous Programming Concepts

Asynchronous programming allows for non-blocking execution of code, enabling efficient handling of I/O-bound tasks. Python's `asyncio` library provides the foundation for writing asynchronous code.

### Introduction to Asynchronous Programming

Asynchronous programming enables you to write code that can perform multiple tasks concurrently without waiting for each task to complete before starting the next one.

### `asyncio` Library

`asyncio` is a library to write concurrent code using the `async`/`await` syntax.

#### Installation

`asyncio` is included in Python's standard library (Python 3.4+).

### Basic Concepts

#### `async` and `await`

- **`async`** defines an asynchronous function.
- **`await`** pauses the execution of the function until the awaited task is complete.

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Running the coroutine
asyncio.run(say_hello())
```

### Creating and Running Coroutines

A coroutine is a function that can pause and resume its execution.

```python
import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")
    return "Data"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

### Concurrent Execution

Use `asyncio.gather()` to run multiple coroutines concurrently.

```python
import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

### Using `asyncio` for I/O-bound Tasks

Example: Fetching multiple web pages concurrently.

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://example.com", "https://example.org", "https://example.net"]
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

asyncio.run(main())
```

### Asynchronous Context Managers

Use `async with` for asynchronous context management.

```python
import asyncio

class AsyncContextManager:
    async def __aenter__(self):
        print("Enter context")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Exit context")

async def main():
    async with AsyncContextManager():
        print("Inside context")

asyncio.run(main())
```

### Handling Exceptions in Coroutines

```python
import asyncio

async def faulty_task():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")

async def main():
    try:
        await faulty_task()
    except ValueError as e:
        print(f"Caught an exception: {e}")

asyncio.run(main())
```

### Practical Example: Asynchronous Web Scraper

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        print(f"Title: {title}")

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    tasks = [scrape(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

### Exercises

1. Write an asynchronous function that fetches data from multiple APIs concurrently.
2. Create an asynchronous context manager that logs entry and exit times.
3. Implement an asynchronous task that retries on failure with exponential backoff.

### Key Points

- Asynchronous programming allows for non-blocking execution, ideal for I/O-bound tasks.
- `asyncio` provides the foundation for writing asynchronous code using `async` and `await`.
- Use `asyncio.gather()` to run multiple coroutines concurrently.
- Asynchronous context managers and exception handling are similar to their synchronous counterparts.
- Practical applications include concurrent web scraping, API calls, and more.
