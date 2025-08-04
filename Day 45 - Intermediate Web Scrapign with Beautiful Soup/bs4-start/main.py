from bs4 import BeautifulSoup
# from bs4 import lxml


# open html file to start parsing data
with open("C:/Users/Zeilhan Co/Desktop/Study/100 Days of Code Python/Code/Day 45 - Intermediate Web Scrapign with Beautiful Soup/bs4-start/website.html") as file: 
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") # pass in the text we want to turn into soup (content or our website url) and the parser or that tells beautiful soup the language of our doc. Sometimes you might need to use lxml
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup)
print(soup.prettify)
print(soup.a)

# with all these we only get hold of the first p or a or title tag. to get all
all_anchor_tags = soup.find_all(name="a") # gives all the anchor tags
print(all_anchor_tags)

# How to get all the text in all the anchor tags
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href")) # get the value of any attribute. this gives all the links

# findAll returns all the values that matches the query meanwhile find returns only the first one
heading = soup.find(name= "h1", id="name")
print(heading)

# section_heading = soup.find(name= "h3", class="heading") returns an error because 'class' is a reserved keyword. Therefore use class_
section_heading = soup.find(name= "h3", class_="heading")
print(section_heading) # can also do section_heading.getText to get the text in that h3 or if we want the name of that tag we can use section_heading.name
# or section_heading.get("class") to get the value of that class

# How to get a specific tag.
# For example the href tag in the html doc on line 11 sits in an anchor tag that sits in a strong tag that sits in an emphasis tag that sits in a p tag that sits in a body tag
# Beatiful soup can work similarly to css selectors:
company_url = soup.select_one(selector="p a")
print(company_url)

# we can also class and id selectors in addition to html tags
company_url1 = soup.select_one(selector="#name") # or soup.select_one("#name")
print(company_url1)

headings = soup.select(".heading") # or soup.select(selector=".heading") --> returns a list
print(headings)


# how to scrape a live website
