from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

print(soup.title)

# Find the title of each article and print it in code. have a class of storylink and a anchor tag
# Title of first article.
article_tag = soup.find(name="span", class_="titleline")

print(article_tag)
# get text in the anchor tag
print(article_tag.getText())

article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(class_="score", name="span").getText()

print(article_link)
print(article_upvote)

# Get all texts and all links
articles = soup.find_all(name="span", class_="titleline")
article_upvotes = soup.find_all(class_="score", name="span").getText()

print("********************")
print(articles)
print(article_upvotes)


article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [score.getText() for score in soup.find_all(class_="score", name="span").getText()]

print(article_upvotes[0]) # returns 40 points so we split it to get the number alone and remove the text
print(article_upvotes[0].split()) # returns ['40', 'points']
print(int(article_upvotes[0].split()[0])) # returns 40

article_upvotes = [int(score.getText().split()[0] )for score in soup.find_all(class_="score", name="span").getText()] # returns a list of all the scores of upvotes
# now we get the index of the highest number that represents the article that is the most popular. Then we use that to get the title, link, etc
most_votes = max(article_upvotes)
print(most_votes)
most_votes_index = article_upvotes.index(most_votes)
print(most_votes_index)
print(article_texts[most_votes_index]) # prints the article text with the most votes
print(article_links[most_votes_index]) # prints the article link with the most votes