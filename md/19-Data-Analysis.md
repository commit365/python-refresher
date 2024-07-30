
## 19. Data Analysis: Introduction to NumPy and Pandas 

NumPy and Pandas are fundamental libraries for data analysis in Python. NumPy provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions. Pandas offers data structures and operations for manipulating numerical tables and time series. 

### NumPy 

NumPy is the foundation for numerical computing in Python. 

#### Installation 

```bash 
pip install numpy
```

## Basic Usage

```python
import numpy as np 

# Creating arrays 
arr1 = np.array([1, 2, 3, 4, 5]) 
arr2 = np.zeros((3, 3)) 
arr3 = np.ones((2, 4)) 
arr4 = np.arange(10) 

# Array operations 
print(arr1 * 2)  # Element-wise multiplication 
print(arr1 + arr1)  # Element-wise addition 

# Mathematical functions 
print(np.sqrt(arr1)) 
print(np.sin(arr1)) 

# Indexing and slicing 
print(arr1[2])  # Third element 
print(arr1[1:4])  # Slice 

# Reshaping 
arr5 = np.arange(12).reshape(3, 4)
```

## Multi-dimensional Arrays

```python
import numpy as np

# Creating 2D array 
arr2d = np.array([[1, 2, 3], [4, 5, 6]]) 

# Accessing elements 
print(arr2d[0, 1])  # Second element of first row 

# Basic linear algebra 
a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6], [7, 8]]) 
print(np.dot(a, b))  # Matrix multiplication
```

## Pandas

Pandas is built on top of NumPy and provides high-performance, easy-to-use data structures and data analysis tools.

## Installation

```bash
pip install pandas
```

## Series

A Series is a one-dimensional labeled array.

```python
import pandas as pd 

s = pd.Series([1, 3, 5, np.nan, 6, 8]) 
print(s)
```

## DataFrame

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

```python
import pandas as pd

# Creating a DataFrame 
df = pd.DataFrame({     
	'A': [1, 2, 3],    
	'B': ['a', 'b', 'c'],    
	'C': [4.5, 5.5, 6.5] }) 
	
# Reading from CSV 
df = pd.read_csv('example.csv') 

# Basic info 
print(df.head()) 
print(df.describe()) 

# Selecting data 
print(df['A'])  # Select column 
print(df.loc[0])  # Select row by label 
print(df.iloc[1:3])  # Select rows by integer index 

# Filtering 
print(df[df['A'] > 2]) 

# Adding a new column 
df['D'] = df['A'] + df['C'] 

# Grouping and aggregation 
grouped = df.groupby('B').mean() 

# Merging DataFrames 
df2 = pd.DataFrame({
	'B': ['a', 'b', 'd'], 
	'E': [1, 2, 3]
}) 
merged = pd.merge(df, df2, on='B', how='left')
```

## Data Manipulation with Pandas

```python
import pandas as pd
import numpy as np

# Handling missing data 
df.dropna()  # Drop rows with missing values 
df.fillna(value=0)  # Fill missing values with 0 

# Applying functions 
df['A'].apply(lambda x: x * 2) 

# Pivot tables 
pivot = df.pivot_table(values='A', index='B', columns='C', aggfunc=np.sum) 

# Time series 
dates = pd.date_range('20230101', periods=6) 
ts = pd.Series(np.random.randn(6), index=dates)
```

## Practical Example: Analyzing Sales Data

```python
import pandas as pd 
import numpy as np 

# Create sample sales data 
data = {     
	'Date': pd.date_range('20230101', periods=10),    
	'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],   
	'Quantity': np.random.randint(1, 50, size=10),    
	'Price': np.random.uniform(10, 100, size=10) 
} 
	
df = pd.DataFrame(data) 
df['Total'] = df['Quantity'] * df['Price'] 

# Analysis 
print(df.groupby('Product')['Total'].sum()) 
print(df.resample('W', on='Date')['Total'].sum())
```

## Exercise

1. Use NumPy to create a 5x5 matrix of random integers between 1 and 100.
2. Using Pandas, read a CSV file of your choice and perform basic data analysis (e.g., summary statistics, grouping, filtering).
3. Create a time series of daily temperatures for a month and calculate the 7-day rolling average.

## Key Points

- NumPy is efficient for numerical operations on arrays.
- Pandas provides powerful data structures (Series and DataFrame) for data manipulation.
- Both libraries are essential for data analysis and scientific computing in Python.
- Pandas excels at handling structured data and time series.
- NumPy and Pandas work well together and with other data science libraries.
