
## 25. Databases: Interacting with Databases using SQLite and SQLAlchemy 

Databases are essential for storing and managing structured data. This section covers working with SQLite, a lightweight relational database, and SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library. 

### SQLite 

SQLite is a C library that provides a lightweight disk-based database. Python includes built-in support for SQLite through the `sqlite3` module. 

#### Basic SQLite Operations 

```python
import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))

# Query data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Commit changes and close connection
conn.commit()
conn.close()
```

## Using Context Manager

```python
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name=?", ("Alice",))
    print(cursor.fetchone())
```

## SQLAlchemy

SQLAlchemy is a comprehensive set of tools for working with databases in Python, including an ORM and a core SQL abstraction layer.

## Installation

```bash
pip install sqlalchemy
```

## Defining Models

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
```

## Creating the Database

```python
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
```

## Basic CRUD Operations

```python
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create
new_user = User(name="Bob", email="bob@example.com")
session.add(new_user)
session.commit()

# Read
user = session.query(User).filter_by(name="Bob").first()
print(user)

# Update
user.email = "newemail@example.com"
session.commit()

# Delete
session.delete(user)
session.commit()

# Query all users
users = session.query(User).all()
for user in users:
    print(user)

session.close()
```

## Using Relationships

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

User.posts = relationship("Post", order_by=Post.id, back_populates="user")
```

## Querying with Relationships

```python
# Add a post for a user
user = session.query(User).filter_by(name="Alice").first()
new_post = Post(title="First Post", content="Hello, World!", user=user)
session.add(new_post)
session.commit()

# Query posts for a user
user_with_posts = session.query(User).filter_by(name="Alice").first()
for post in user_with_posts.posts:
    print(f"{post.title}: {post.content}")
```

## Practical Example: Blog Application

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

# Create the database
engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a user and a post
new_user = User(username="blogger")
new_post = Post(title="My First Blog Post", content="Hello, World!", author=new_user)
session.add(new_user)
session.add(new_post)
session.commit()

# Query and display
user = session.query(User).filter_by(username="blogger").first()
print(f"Posts by {user.username}:")
for post in user.posts:
    print(f"- {post.title}: {post.content}")

session.close()
```

## Exercise

1. Create a SQLite database for a library system with tables for books and authors.
2. Implement the same library system using SQLAlchemy, including a many-to-many relationship between books and authors.
3. Write a script that performs CRUD operations on your library database using both SQLite and SQLAlchemy.

## Key Points

- SQLite is a lightweight, serverless database engine included with Python.
- SQLAlchemy provides both a SQL abstraction layer and an ORM for working with databases.
- The ORM allows you to work with database records as Python objects.
- SQLAlchemy supports various database systems beyond SQLite.
- Always close database connections and sessions to free up resources.
- Use relationships in SQLAlchemy to model connections between different tables.
