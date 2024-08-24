#persiapkan library
import requests
import pandas as pd
from bs4 import BeautifulSoup

# import re
# import nltk

#siapkan request header
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

header = {
    "User-Agent":user_agent
}

url = "https://cryptorank.io/news"
df = pd.DataFrame()

  #requests
response_page = requests.get(url, headers=header)
response = response_page.content

  #masukkan response ke dalam obyek beautifulsoup
soup_obj = BeautifulSoup(response, "html.parser")
#display(soup_obj)

body_tag = soup_obj.find("body")
next_tag = body_tag.find("div", {"id":"__next"})
root_contain = next_tag.find("div", {"id":"root-container"})
content_tag = root_contain.find("div", {"class":"sc-785e1c4d-0 iCRHOt"})
articles_div = content_tag.find_all("div", {"class":"sc-3a0fb232-3 efSCUF"})

# display(len(articles_div))
# display(articles_div)

list_title = []

#Ambil Judul

for row in articles_div:
  section = row.find("img", {"class":"sc-3a0fb232-0 fBHye"})
  title_text = section.get("alt")
  list_title.append(title_text)
  print(title_text)  

# for txt in list_title:
#   print(txt)
print("==============")
df = pd.DataFrame(list_title, columns=['Berita'])
print(df)
print("==============")
print(df.dtypes)