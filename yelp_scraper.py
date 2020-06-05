# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:57:47 2020

@author: Jason
"""

import bs4 as bs
import urllib.request as url
import pandas as pd
import numpy as np

def data_scrape():
    #Empty list for main list items
    pages = np.arange(0,990,30)
    busname = []
    ratings = []
    noreviews = []
    price = []
    cuisine = []
    add = []
    tel = []
    nbh = []
    for i in pages:
        source = url.urlopen('https://www.yelp.ca/search?find_desc=Restaurants&find_loc=Toronto%2C%20ON&start='+str(i))
        page_soup = bs.BeautifulSoup(source, 'html.parser')
        mains = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc mainAttributes__373c0__1r0QA arrange-unit__373c0__o3tjT arrange-unit-fill__373c0__3Sfw1 border-color--default__373c0__3-ifU"})
        main = mains[0]
        secondarys = page_soup.find_all("div", {"class": "lemon--div__373c0__1mboc container__373c0__19wDx padding-l2__373c0__1Dr82 border-color--default__373c0__3-ifU text-align--right__373c0__1XDu3"})
        sec = secondarys[0]
        
        for main in mains:
            try:
                busname.append(main.find("a").text)
            except:
                busname.append("None")
            try:
                ratings.append(main.find("span", {"class": "lemon--span__373c0__3997G display--inline__373c0__3JqBP border-color--default__373c0__3-ifU"}).div.get('aria-label'))
            except:
                ratings.append("None")
            try:
                noreviews.append(main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"}).text)
            except:
                noreviews.append("None")
            try:
                price.append(main.find("span", {"class": "lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z"}).text)
            except:
                price.append("None")
            try:
                cuisine.append(main.find('span', {'class':'lemon--span__373c0__3997G text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-'}).text)
            except:
                cuisine.append('None')
        
        for sec in secondarys:
            try:       
                add.append(sec.address.find("span", {"class": "lemon--span__373c0__3997G raw__373c0__3rcx7"}).text)
            except:
                add.append("None")
            try:
                tel.append(sec.div.div.text)
            except: 
                tel.append("None")
            try:
                nbh.append(sec.find('div', {'class':'lemon--div__373c0__1mboc margin-b1__373c0__1khoT border-color--default__373c0__3-ifU'}).text)
            except:
                nbh.append('None')
                
    data = {}
    data = {'Rest_name': busname, 'Rest_ratings': ratings, 'Rest_noreviews': noreviews, 'Rest_price': price, 'Rest_add': add, 'Rest_tel': tel, 'Rest_nbh': nbh}
    rest = pd.DataFrame(data)
    header = ["Rest_name", "Rest_ratings", "Rest_noreviews", "Rest_price", "Rest_add", "Rest_tel", 'Rest_nbh']
    rest.to_csv("yelp_foods.csv", columns = header, index = False)

if __name__=='__main__':
    data_scrape()
    
