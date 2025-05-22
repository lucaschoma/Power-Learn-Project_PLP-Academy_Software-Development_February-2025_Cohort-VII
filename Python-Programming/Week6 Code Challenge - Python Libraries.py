# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
print("Task 1: NumPy Mean")
arr = np.arange(1, 11)  # Array from 1 to 10
mean_value = np.mean(arr)
print("Array:", arr)
print("Mean:", mean_value)
print()

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
print("Task 2: Pandas DataFrame Summary")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'Score': [88, 92, 85, 90, 95]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print()

# Task 3: Fetch data from a public API using requests and print a key piece of information
print("Task 3: API Request")
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")  # Bitcoin price API
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_price = bitcoin_data['bpi']['USD']['rate']
    print("Current Bitcoin Price in USD:", usd_price)
else:
    print("Failed to fetch data from API")
print()

# Task 4: Plot a simple line graph using matplotlib
print("Task 4: Line Graph")
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
