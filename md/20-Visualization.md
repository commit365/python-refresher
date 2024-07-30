
## 20. Visualization: Plotting with Matplotlib and Seaborn 

Data visualization is crucial for understanding and communicating insights from data. Matplotlib is the foundation for plotting in Python, while Seaborn builds on top of Matplotlib to provide a higher-level interface for statistical graphics. 

### Matplotlib Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 

#### Installation 

```bash 
pip install matplotlib
```

## Basic Line Plot

```python
import matplotlib.pyplot as plt 
import numpy as np 

# Generate data
x = np.linspace(0, 10, 100) 
y = np.sin(x) 

# Plot the data
plt.plot(x, y) 
plt.title('Sine Wave') 
plt.xlabel('x') 
plt.ylabel('sin(x)') 
plt.show()
```

## Multiple Lines and Customization

```python
import matplotlib.pyplot as plt 
import numpy as np 

# Generate data 
x = np.linspace(0, 10, 100) 

# Create the plot 
plt.figure(figsize=(10, 6)) 
plt.plot(x, np.sin(x), label='sin(x)') 
plt.plot(x, np.cos(x), label='cos(x)') 

# Customize the plot 
plt.title('Trigonometric Functions', fontsize=16) 
plt.xlabel('x', fontsize=14) 
plt.ylabel('y', fontsize=14) 
plt.legend() 
plt.grid(True) 

# Display the plot 
plt.show()
```

## Scatter Plot

```python
import matplotlib.pyplot as plt 
import numpy as np 

# Generate random data 
x = np.random.rand(50) 
y = np.random.rand(50) 
colors = np.random.rand(50) 
sizes = 1000 * np.random.rand(50) 

# Create the scatter plot 
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5) 

# Add a color bar 
plt.colorbar() 

# Display the plot 
plt.show()
```

## Bar Plot

```python
import matplotlib.pyplot as plt 

# Data for the bar plot 
categories = ['A', 'B', 'C', 'D'] 
values = [3, 7, 2, 5] 

# Create the bar plot 
plt.bar(categories, values) 

# Customize the plot 
plt.title('Bar Plot') 
plt.xlabel('Category') 
plt.ylabel('Value') 

# Display the plot 
plt.show()
```

## Subplots

```python
import matplotlib.pyplot as plt 
import numpy as np 

# Generate data (assuming x is not defined) 
x = np.linspace(0, 2*np.pi, 100) 

# Create a figure with two subplots side by side 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 

# First subplot: Sine 
ax1.plot(x, np.sin(x)) 
ax1.set_title('Sine') 

# Second subplot: Cosine 
ax2.plot(x, np.cos(x)) 
ax2.set_title('Cosine') 

# Adjust layout and display 
plt.tight_layout() 
plt.show()
```

## Seaborn

Seaborn is a statistical data visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Installation

```bash
pip install seaborn
```

## Basic Usage

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Set the style 
sns.set_style("whitegrid") 

# Create a scatter plot 
sns.scatterplot(x='total_bill', y='tip', data=tips) 

# Customize the plot 
plt.title('Tips vs Total Bill') 

# Display the plot 
plt.show()
```

## Regression Plot

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Create a regression plot 
sns.regplot(x='total_bill', y='tip', data=tips) 

# Customize the plot 
plt.title('Tips vs Total Bill with Regression Line') 

# Display the plot 
plt.show()
```

## Box Plot

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Create a box plot 
sns.boxplot(x='day', y='total_bill', data=tips) 

# Customize the plot 
plt.title('Total Bill by Day') 

# Display the plot 
plt.show()
```

## Violin Plot

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Create a violin plot 
sns.violinplot(x='day', y='total_bill', data=tips) 

# Customize the plot 
plt.title('Distribution of Total Bill by Day') 

# Display the plot 
plt.show()
```

## Heatmap

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Compute correlation matrix 
correlation = tips.corr() 

# Create a heatmap 
sns.heatmap(correlation, annot=True, cmap='coolwarm') 

# Customize the plot 
plt.title('Correlation Heatmap') 

# Display the plot 
plt.show()
```

## Pair Plot

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Create a pair plot 
sns.pairplot(tips, hue='time') 

# Customize the plot 
plt.suptitle('Pair Plot of Tips Dataset', y=1.02) 

# Display the plot 
plt.show()
```

## Combining Matplotlib and Seaborn

```python
import seaborn as sns 
import matplotlib.pyplot as plt 

# Load a built-in dataset 
tips = sns.load_dataset('tips') 

# Create a figure with a 2x2 grid of subplots 
fig, axes = plt.subplots(2, 2, figsize=(15, 12)) 

# Scatter plot 
sns.scatterplot(x='total_bill', y='tip', data=tips, ax=axes[0, 0]) axes[0, 0].set_title('Scatter Plot') 

# Box plot 
sns.boxplot(x='day', y='total_bill', data=tips, ax=axes[0, 1]) axes[0, 1].set_title('Box Plot') 

# Histogram with KDE 
sns.histplot(tips['total_bill'], kde=True, ax=axes[1, 0]) axes[1, 0].set_title('Histogram with KDE') 

# Correlation heatmap 
sns.heatmap(tips.corr(), annot=True, cmap='coolwarm', ax=axes[1, 1]) axes[1, 1].set_title('Correlation Heatmap') 

# Adjust layout and display the plot 
plt.tight_layout() 
plt.show()
```

## Exercise

1. Create a line plot showing the trend of a stock price over a month using Matplotlib.
2. Using Seaborn, create a box plot to compare the distribution of a variable across different categories in a dataset of your choice.
3. Combine Matplotlib and Seaborn to create a dashboard with at least four different types of plots using a dataset of your choice.

## Key Points

- Matplotlib provides a MATLAB-like plotting interface and fine-grained control over plot elements.
- Seaborn builds on Matplotlib to provide a more aesthetically pleasing and statistically-oriented plotting interface.
- Matplotlib is great for customized plots, while Seaborn excels in statistical visualizations.
- Both libraries can be used together to create complex and informative visualizations.
- Always consider the type of data and the story you want to tell when choosing a visualization method.
