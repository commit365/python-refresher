
## APIs: Working with REST APIs and Web Services

APIs (Application Programming Interfaces) allow different software applications to communicate with each other. REST (Representational State Transfer) is a popular architectural style for designing networked applications.

### Introduction to REST APIs

REST APIs typically use HTTP methods to perform operations on resources:

- **GET**: Retrieve data
- **POST**: Create new data
- **PUT/PATCH**: Update existing data
- **DELETE**: Remove data

### Making API Requests with `requests` Library

The `requests` library is commonly used for making HTTP requests in Python.

#### Installation

```bash
pip install requests
```

### Basic GET Request

```python
import requests

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### POST Request

```python
data = {'key': 'value'}
response = requests.post('https://api.example.com/create', json=data)
print(response.json())
```

### PUT Request

```python
data = {'updated_key': 'updated_value'}
response = requests.put('https://api.example.com/update/1', json=data)
print(response.json())
```

### DELETE Request

```python
response = requests.delete('https://api.example.com/delete/1')
print(response.status_code)
```

### Authentication

Many APIs require authentication. Common methods include API keys and OAuth.

#### API Key Authentication

```python
headers = {'Authorization': 'Bearer YOUR_API_KEY'}
response = requests.get('https://api.example.com/protected', headers=headers)
```

#### Basic Authentication

```python
response = requests.get('https://api.example.com/protected', auth=('username', 'password'))
```

### Handling Pagination

Some APIs return paginated results. You'll need to handle multiple requests to get all data.

```python
def get_all_pages(url):
    all_data = []
    while url:
        response = requests.get(url)
        data = response.json()
        all_data.extend(data['results'])
        url = data['next']  # Assuming the API provides a 'next' URL
    return all_data
```

### Rate Limiting

Respect API rate limits to avoid being blocked.

```python
import time

def rate_limited_request(url, max_retries=3):
    for _ in range(max_retries):
        response = requests.get(url)
        if response.status_code == 429:  # Too Many Requests
            time.sleep(int(response.headers.get('Retry-After', 5)))
        else:
            return response
    raise Exception("Max retries reached")
```

### Working with JSON Data

Most APIs return data in JSON format.

```python
import json

# Parsing JSON
data = json.loads('{"name": "John", "age": 30}')

# Creating JSON
json_string = json.dumps(data)
```

### Asynchronous API Requests

For improved performance, use asynchronous requests with `aiohttp`.

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, f'https://api.example.com/item/{i}') for i in range(10)]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())
```

### Error Handling

Always handle potential errors when working with APIs.

```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
except requests.RequestException as e:
    print(f"An error occurred: {e}")
```

### Practical Example: Working with GitHub API

```python
import requests

def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(f"Repository: {repo['name']}, Stars: {repo['stargazers_count']}")
    else:
        print(f"Error: {response.status_code}")

get_user_repos('octocat')
```

### Exercises

1. Create a function that fetches weather data for a given city using a public weather API.
2. Implement a script that posts a new resource to a RESTful API and then retrieves and displays it.
3. Write an asynchronous function that fetches data from multiple endpoints of an API concurrently.

### Key Points

- REST APIs use standard HTTP methods for operations on resources.
- The `requests` library is commonly used for making HTTP requests in Python.
- Always handle authentication, pagination, and rate limiting when working with APIs.
- Use error handling to manage potential issues with API requests.
- Asynchronous requests can improve performance when dealing with multiple API calls.
- JSON is the most common data format for API responses.
