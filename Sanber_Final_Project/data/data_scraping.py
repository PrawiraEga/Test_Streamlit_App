# library
import streamlit as st
import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup

# request header
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

header = {
        "User-Agent":user_agent
    }

list_item = []
items_one = []
items_two = []
items_tri = []
items_four = []
items_five = []

df = pd.DataFrame()

def data_scrap_one():

    time.sleep(0.75)
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

def data_scrap_two():
    time.sleep(0.25)
    url = "https://cryptopotato.com/"

    #requests
    response_page = requests.get(url)
    response = response_page.content

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

    return list_txt_post

def data_scrap_tri():
    time.sleep(0.25)
    url = "https://decrypt.co/news-explorer"

    #requests
    response_page = requests.get(url)
    response = response_page.content

    # response ke beautifulsoup
    soup_obj = BeautifulSoup(response, "html.parser")

    body_tag = soup_obj.find("body")
    next_tag = body_tag.find("div", {"id":"__next"})
    main_tag = next_tag.find("main")
    latest_tag = main_tag.find("div", {"class":"flex flex-col -mx-4 md:mx-0 mt-2"})
    news_div = latest_tag.find_all("div", {"class":"flex gap-2 flex-col py-5 px-4 pb-3 md:p-6 md:pb-4 border-[1px] border-solid border-b-0 undefined relative"})

    list_txt_post = []

    for row in news_div:
        post = row.find("span", {"class":"hidden md:inline"})
        quote_text = post.get_text()
        list_txt_post.append(quote_text)
        # print(quote_text)

    return list_txt_post

def data_scrap_four():
    time.sleep(0.25)
    url = "https://www.fxcryptonews.com/crypto-news/"

    #requests
    response_page = requests.get(url)
    response = response_page.content

    #masukkan response ke dalam obyek beautifulsoup
    soup_obj = BeautifulSoup(response, "html.parser")

    body_tag = soup_obj.find("body")
    section_tag = body_tag.find("section", {"class":"elementor-section elementor-top-section elementor-element elementor-element-5fdf9bd elementor-section-boxed elementor-section-height-default elementor-section-height-default"})
    elementor_tag = section_tag.find("div", {"class":"ultp-block-wrapper"})
    wrap_tag = elementor_tag.find("div", {"class":"ultp-block-items-wrap ultp-block-row ultp-pg1a-style1 ultp-block-column-3 ultp-layout1"})
    items_tag = wrap_tag.find_all("div", {"class":"ultp-block-content-wrap"})
    
    list_txt_post = []

    for row in items_tag:
        post = row.find("div", {"class":"ultp-block-excerpt"})
        post = row.find("p")
        quote_text = post.get_text()
        list_txt_post.append(quote_text)
        # print(quote_text)

    return list_txt_post

def data_scrap_five():
    url = "https://www.investing.com/news/cryptocurrency-news"

    #requests
    response_page = requests.get(url)
    response = response_page.content

    #masukkan response ke dalam obyek beautifulsoup
    soup_obj = BeautifulSoup(response, "html.parser")

    body_tag = soup_obj.find("body")
    next_tag = body_tag.find("div", {"id":"__next"})
    relative_tag = next_tag.find("div", {"class":"relative flex"})
    news_container = relative_tag.find("div", {"data-test":"news-container"})
    news_list = news_container.find_all("li", {"class":"list_list__item__dwS6E !mt-0 border-t border-solid border-[#E6E9EB] py-6"})

    list_txt_post = []

    for row in news_list:
      post = row.find("article", {"class":"news-analysis-v2_article__wW0pT flex w-full sm:flex-row-reverse md:flex-row"})
      post = row.find("div", {"class":"news-analysis-v2_content__z0iLP w-full text-xs sm:flex-1"})
      post = row.find("p", {"data-test":"article-description"})
      quote_text = post.get_text()
      list_txt_post.append(quote_text)

      return list_txt_post

def get_all_items():
    items_one = data_scrap_one()
    items_two = data_scrap_two()
    items_tri = data_scrap_tri()
    items_four = data_scrap_four()
    items_five = data_scrap_five()    
    list_item = items_one + items_two + items_tri + items_four + items_five
    
    return list_item
