import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
print(soup)
all_titles = soup.find_all("h3", class_="title") # returns a list of all the movies. getText() doesn't work on lists
print(all_titles)

movie_titles = [movieTitle.getText() for movieTitle in all_titles]
print(movie_titles)
 # now to reverse the order
ordered_list = movie_titles[::-1]
print(f"Ordered List ***********************************************{ordered_list}")

with open("movie list.txt", mode="w", encoding="utf-8") as file:
    for movie in ordered_list:
        file.write(f"{movie}\n")