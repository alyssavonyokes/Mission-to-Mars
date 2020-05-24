#!/usr/bin/env python
# coding: utf-8

# In[66]:
import sys
print(sys.path)
# In[67]:
# Import Splinter and BeautifulSoup.
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
# In[68]:
# Path to chromedriver.
get_ipython().system('which chromedriver')
# In[69]:
# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
# In[70]:
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
# In[71]:
# Set up HTML Parser.
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')
# In[72]:
# Scrape for title with html elements.
slide_elem.find("div", class_='content_title')
# In[73]:
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
# In[74]:
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p
# In[75]:
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
# In[76]:
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()
# In[77]:
# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()
# In[78]:
# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
# In[79]:
# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel
# In[80]:
# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url
# In[81]:
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df
# In[82]:
df.to_html()
# In[ ]:
browser.quit()
