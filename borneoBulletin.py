import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

response = requests.get("https://borneobulletin.com.bn/")
soup = BeautifulSoup(response.content, "html.parser")

urls = []

for h3_tags in soup.find_all("h3"):
    a_tags = h3_tags.find("a")
    urls.append(a_tags.string)

i=1
for titles in urls:
    print(i,titles)
    analysis = TextBlob(titles)
    print(analysis.sentiment)
    i+=1

