
## 26. Deployment: Packaging and Deploying Python Applications 

Deploying Python applications involves packaging your code and making it available for use in different environments. This section covers various aspects of packaging and deployment. 

### Packaging Python Applications 

#### Creating a Package Structure

```
my_package/  
│  
├── my_package/  
│   ├── __init__.py  
│   ├── module1.py  
│   └── module2.py  
│  
├── tests/  
│   ├── __init__.py  
│   ├── test_module1.py  
│   └── test_module2.py  
│  
├── setup.py  
├── README.md  
└── LICENSE
```

#### Writing `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "dependency1>=1.0.0",
        "dependency2>=2.1.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of the package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
```

## Building the Package

```bash
python setup.py sdist bdist_wheel
```

## Installing the Package Locally

```bash
pip install .
```

## Virtual Environments

Virtual environments isolate project dependencies.

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On Unix or MacOS:
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

## Dependency Management

### Using `requirements.txt`

```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

### Using `Pipenv`

```bash
# Install Pipenv
pip install pipenv

# Install dependencies
pipenv install

# Activate the Pipenv shell
pipenv shell

# Generate Pipfile.lock
pipenv lock
```

## Containerization with Docker

### Basic `Dockerfile`

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Building and Running Docker Container

```bash
# Build the Docker image
docker build -t my-python-app .

# Run the Docker container
docker run -p 5000:5000 my-python-app
```

## Deploying to Cloud Platforms

### Heroku Deployment

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Deploy to Heroku:
   ```bash
   git push heroku master
   ```

### AWS Elastic Beanstalk

1. Install the EB CLI:
   ```bash
   pip install awsebcli
   ```

2. Initialize and deploy:
   ```bash
   eb init
   eb create
   eb deploy
   ```

## Continuous Integration/Continuous Deployment (CI/CD)

### GitHub Actions Example

```yaml
name: Python CI/CD

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: python -m unittest discover tests
    - name: Deploy to Heroku
      if: github.ref == 'refs/heads/main'
      env:
        HEROKU_API_KEY: ${{ secrets.HEROKU_API_KEY }}
      run: |
        git push https://heroku:$HEROKU_API_KEY@git.heroku.com/your-app-name.git main
```

## Best Practices

1. Use version control (e.g., Git) for your project.
2. Implement proper error handling and logging.
3. Use configuration management for different environments.
4. Implement automated testing before deployment.
5. Monitor your application's performance and errors in production.
6. Keep dependencies updated and use a dependency vulnerability scanner.

## Exercise

1. Create a simple Flask web application and package it using `setuptools`.
2. Containerize your Flask application using Docker and run it locally.
3. Set up a CI/CD pipeline using GitHub Actions to test and deploy your application to Heroku.

## Key Points

- Proper packaging makes distribution and installation of your application easier.
- Virtual environments help manage project-specific dependencies.
- Containerization with Docker ensures consistency across different environments.
- Cloud platforms like Heroku and AWS provide easy deployment options for Python applications.
- CI/CD pipelines automate the testing and deployment process.
- Always follow best practices for security and maintainability when deploying applications.