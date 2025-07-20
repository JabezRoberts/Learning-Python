# with open("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/Start/weather_data.csv", mode="r") as file:
#     weather_data = file.readlines()
#     print(weather_data)
# This output gives us data in a string format separated by commas, that's still hard to work with because we need to remove the blank spaces, \n and organize it

# Here is a way to handle this
import csv
with open("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/Start/weather_data.csv", mode="r") as file:
    data = csv.reader(file)
    print(data) #this gives a csv reader object so use a for loop:
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
 
 # this was still a lot of code to get data from a simple table. To do this we use pandas
 # import pandas but it won't work until you run     pip install pandas

import pandas

data  = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/Start/weather_data.csv")
print(data)

# Convert data to a dictionary from a Panda 
data_dict = data.to_dict()
print(data_dict)

# Convert a data series or column to a list
temp_list = data["temp"].to_list()


# Calculate the average temperature in the list
temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# or use the Series.mean data function
print(data["temp"].mean())

# Get the max temperature
print(data["temp"].max())


# Get data in columns
print(data["condition"])

# or since Pandas converts all table headings to attributes you can use. If the table heading 'condition' was a capital C meaning Condition then the 
# syntax would change to be print(data["Condition"]) or print(data.Condition). It's like a dictionary with a key:value pair with the heading being the key
print(data.condition)


# Get data in rows - How to get the entire row of data for the day Monday
print(data[data.day == "Monday"])

# Get the row of data with the max temperature
print(data[data.temp == data["temp"].max()])
# data["temp"].max() can also be data.temp.max()

# print(data[data.day == "Monday"]) --> if in the square brackets of our data frame we only put the name of our column then we get the entire column data
# data["temp"].max() can also be data.temp.max() --> But if we filter that column by a condition, say when a particular column is equal to a particular value, we get the entire row instead

# When you get the entire row you can go a step further
monday = data[data.day == "Monday"]
print(monday.condition)

# convert Monday's temp to fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(f"Monday temp in fahrenheit: {monday_temp_F}")


# Create a data frame from scratch. Instead of readign from a CSV file we could use some data generated in Python
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data_in_csv.csv") # Convert to a CSV. Enter the name to save the CSV file as