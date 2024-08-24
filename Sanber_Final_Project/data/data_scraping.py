#persiapkan library
import streamlit as st
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

list_item = []
df = pd.DataFrame()

def get_data_scrap():


    url = "https://cryptorank.io/news"
    # df = pd.DataFrame()

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

    list_post = []

    #Ambil Text
    for row in articles_div:
        section = row.find("div", {"class":"sc-3a0fb232-6 cmZsmm"})
        post_text = section.get_text()
        list_post.append(post_text)
        # print(post_text)
        # print("=========")
    
    # df = pd.DataFrame(list_title, columns=['Berita'])

    return list_post

def get_data_scrap_two():
    url = "https://cryptopotato.com/"

    #requests
    response_page = requests.get(url)
    response = response_page.content
    # display(response)

    #masukkan response ke dalam obyek beautifulsoup
    soup_obj = BeautifulSoup(response, "html.parser")

    body_tag = soup_obj.find("body")
    widget_pos_tag = body_tag.find("div", {"class":"column-12 widget-column postsmain"})
    list_items_tag = widget_pos_tag.find("div", {"class":"list-items"})

    #Ambil Isi Text
    list_txt_post = []

    for row in list_items_tag:
        post = row.find("div", {"class":"media-body"})
        quote_text = post.find("p")
        quote_text = quote_text.get_text()
        list_txt_post.append(quote_text)
        # print(quote_text)

    return list_txt_post    
