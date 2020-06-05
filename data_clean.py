# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:18:21 2020

@author: Jason
"""

import pandas as pd
import numpy as np
import os

#Define working directory
os.chdir('C:\\Users\\User\\Documents\\School\\code\\Toronto Food')

# Read in data (csv file)
df = pd.read_csv('yelp_foods.csv')

# Parse out restaurant ratings
df['Rating'] = df['Rest_ratings'].apply(lambda x: x.split(' ')[0])
df['Rating'] = df['Rating'].astype(float)

# Change restaurant prices to ints instead of $
df['Rest_price'].unique()
price_dict = {'$':1, '$$':2,'$$$':3,'$$$$':4,'None':0}
df['Price'] = df['Rest_price'].map(price_dict)

# Categorize Restaurant cuisine
df['Rest_cuisine'].unique()
df['Rest_cuisine'].nunique()

df['Rest_cuisine'] = df['Rest_cuisine'].apply(lambda x: x.replace(', ',''))
# American
# Asian
# Caribbean
# African
# Middle Eastern
# European
# Mexican
# South American
# Other

def cuisine_simplifier(rest_name):
    if ('american' in rest_name.lower() or 'barbeque' in rest_name.lower() 
     or 'canadian' in rest_name.lower() or 'pizza' in rest_name.lower() or 'burger' in rest_name.lower()
     or 'steak' in rest_name.lower() or 'breakfast' in rest_name.lower() or 'bar' in rest_name.lower() 
     or 'pub' in rest_name.lower() or 'poutine' in rest_name.lower() or 'fish' in rest_name.lower() 
     or 'chicken wings' in rest_name.lower() or 'hot dogs' in rest_name.lower() or 'sandwich' in rest_name.lower()
     or 'breweries' in rest_name.lower() or 'desserts' in rest_name.lower() or 'cafes' in rest_name.lower()
     or 'comedy' in rest_name.lower() or 'seafood' in rest_name.lower() or 'soup' in rest_name.lower()
     or 'chicken soup' in rest_name.lower() or 'food truck' in rest_name.lower() or 'food court' in rest_name.lower() 
     or 'salad' in rest_name.lower() or 'shop' in rest_name.lower() or 'salad' in rest_name.lower() or 'chicken shop' in rest_name.lower()
     or 'southern' in rest_name.lower() or 'hawaiian' in rest_name.lower() or 'food court' in rest_name.lower() or 'vegan' in rest_name.lower()
     or 'street' in rest_name.lower() or 'fast food' in rest_name.lower() or 'bistros' in rest_name.lower()):
        return 'American'
    elif ('thai' in rest_name.lower() or 'hong kong' in rest_name.lower() or 'japan' in rest_name.lower() 
       or 'laotian' in rest_name.lower() or 'filipino' in rest_name.lower() or 'dim sum' in rest_name.lower()
       or 'taiwan' in rest_name.lower() or 'burmese' in rest_name.lower() or 'chinese' in rest_name.lower()
       or 'korean' in rest_name.lower() or 'indian' in rest_name.lower() or 'ramen' in rest_name.lower() 
       or 'vietnam' in rest_name.lower() or 'asian' in rest_name.lower() or 'dumplings' in rest_name.lower()
       or 'noodles' in rest_name.lower() or 'hot pot' in rest_name.lower() or 'malaysian' in rest_name.lower()
       or 'mongolian' in rest_name.lower() or 'hakka' in rest_name.lower() or 'tibet' in rest_name.lower() 
       or 'himalayan' in rest_name.lower() or 'indonesian' in rest_name.lower() or 'buffet' in rest_name.lower()):
        return 'Asian'
    elif ('caribbean' in rest_name.lower()):
        return 'Carribean'
    elif ('african' in rest_name.lower() or 'ethiopian' in rest_name.lower() or 'egyptian' in rest_name.lower()):
        return 'African'
    elif ('mediterranean' in rest_name.lower() or 'halal' in rest_name.lower() or 'lebanese' in rest_name.lower()
       or 'afghan' in rest_name.lower() or 'turkish' in rest_name.lower() or 'syrian' in rest_name.lower() 
       or 'pakistani' in rest_name.lower() or 'persian' in rest_name.lower() or 'kebab' in rest_name.lower() 
       or 'pomegranate' in rest_name.lower() or 'middle eastern' in rest_name.lower() or 'tabule' in rest_name.lower()
       or 'fat pasha' in rest_name.lower() or 'zaad' in rest_name.lower() or 'camel' in rest_name.lower() or 'arabian' in rest_name.lower()
       or 'souk' in rest_name.lower()):
        return 'Middle Eastern'
    elif ('peruvian' in rest_name.lower() or 'italian' in rest_name.lower() or 'hungarian' in rest_name.lower()
       or 'greek' in rest_name.lower() or 'portuguese' in rest_name.lower() or 'spanish' in rest_name.lower()
       or 'french' in rest_name.lower() or 'polish' in rest_name.lower() or 'german' in rest_name.lower() or 'ukrainian' in rest_name.lower()
       or 'european' in rest_name.lower() or 'belgian' in rest_name.lower() or 'slovakian' in rest_name.lower() or 'tapas' in rest_name.lower()
       or 'british' in rest_name.lower()):
        return 'European'
    elif ('mexican' in rest_name.lower() or 'tex mex' in rest_name.lower() or 'tex-mex' in rest_name.lower()):
        return 'Mexican'
    elif ('brazilian' in rest_name.lower() or 'argentine' in rest_name.lower() or 'venezuelan' in rest_name.lower()
       or 'cuban' in rest_name.lower() or 'colombian' in rest_name.lower() or 'salvadoran' in rest_name.lower()):
        return 'South American'
    else:
        return 'Other'
    
df['Cuisine'] = df['Rest_cuisine'].apply(cuisine_simplifier)
df['Cuisine'].value_counts()

df_other['Rest_cuisine'].unique()

# Exploring the Other category
df_other = df[df['Cuisine']=='Other']

# Fixing values by adding in to cuisine simplifier function

# Group restaurant neighbourhood
df['Rest_nbh'].nunique()
df['Rest_nbh'].unique()

df.isnull().sum()
df['Rest_nbh'].fillna(0, inplace=True)


# All neighbours not reported in the data set
df_nbh = df[df['Rest_nbh'] == 0]

# Parsing out just streets
df_nbh['Street_add'] = df_nbh['Rest_add'].apply(lambda x: x.split(' ')[1:])
df_nbh['Street_add'] = df_nbh['Street_add'].apply(lambda x: ','.join(map(str,x)))
df_nbh['Street_add'] = df_nbh['Street_add'].apply(lambda x: x.replace(',',' '))

# Creating a list of unique Street Address'
list_nbh = df_nbh['Street_add'].unique().tolist()

# Dictionary for Street and respective neighbourhood
add_nbh_dict = {'St Clair Avenue W':'Corso Italia',
                'Wellington Street W':'Entertainment District',
                'Harbord Street':'Bickford Park',
                'King Street W':'Entertainment District',
                'Saint Clair Avenue W':'Wychwood',
                'Carlton Street':'Church-Wellesley Village',
                'Parkway Forest Drive':'Scarborough',
                'St Clair Avenue West':'Corso Italia',
                'Don Mills Road':'Scarborough',
                'Victoria Park Avenue':'Scarborough',
                'Dufferin Street':'Downtown Core',
                'Romar Crescent':'Glen Park',
                'Portland Street':'Entertainment District',
                'Harbord Street':'Entertainment District',
                'York Street':'Entertainment District',
                'Eglinton Avenue W':'York',
                'Carlton Street':'Cabbage Town',
                'Keele Street':'North York',
                'Jane Street':'North York',
                'College St':'Downtown Core',
                'Bathurst St':'North York',
                'King Street W':'Entertainment District',
                'Jarvis Street':'Entertainment District',
                'Rogers Road':'Financial District',
                'York Mills Road':'North York',
                'Yorkmills Road':'North York',
                'Wilson Avenue':'North York',
                'Weston Road':'North York',
                'Street Clair Ave W':'Corso Italia',
                'College Street':'Downtown',
                'Adelaide Street W':'Financial District',
                }
df.isnull().sum()

# Parsing out just streets for data manipulation
df['Street_add'] = df['Rest_add'].apply(lambda x: x.split(' ')[1:])
df['Street_add'] = df['Street_add'].apply(lambda x: ','.join(map(str,x)))
df['Street_add'] = df['Street_add'].apply(lambda x: x.replace(',',' '))

# Parsing out nan values
df['neighbourhood'] = df.apply(lambda x: 1 if pd.isnull(x['Rest_nbh']) else x['Rest_nbh'], axis=1)

# Creating new columns by applying the dictionary to minimize nan values
df['neighbourhood_good'] = df.apply(lambda x: x['neighbourhood_'] if x['neighbourhood'] == 1 else x['neighbourhood'], axis =1)

# Choosing relevant columns for our data set, dropping rest of nan values
df1 = df[['Rest_name','Rest_noreviews','Rating','Price','Cuisine','neighbourhood_good']]
df1.dropna(inplace=True)

# Renaming column names
df1.columns = ['Name','# of Reviews','Rating','Price','Cuisine','Neighbourhood']

# To csv file
df.to_csv('yelp_foods_cleaned.csv', index = False)
