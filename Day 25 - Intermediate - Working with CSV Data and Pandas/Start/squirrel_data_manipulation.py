import pandas

# Now we need to get hold of the fur color column and find out how many are grey, black, and cinnamon

data = pandas.read_csv("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 25 - Intermediate - Working with CSV Data and Pandas/Start//2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

gray_squirrels = [data[data["Primary Fur Color"] == "Gray"]]
print(gray_squirrels)

num_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
print(f"Number of gray squirrels: {num_gray_squirrels}")

num_cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(f"Number of red/cinnamon squirrels: {num_cinnamon_squirrels}")

num_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(f"Number of black squirrels: {num_black_squirrels}")

# Now that we have our data let's create our data frame
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
}
print(data_dict)

# now create the data frame from our dictionary
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Sorted Squirrel Data CSV.csv")