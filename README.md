# Toronto Restaurants Price Predictions Classification
- Developed a classification machine learning model that will predict the price of Toronto Restaurants **(F1-Score: 0.75 or 75%)**. This project was intended for people who want to explore the different cultures and restaurants the wonderful city of Toronto has to offer
- Utilized Python and BeautifulSoup to scrape 1000 restaurants and restaurant information from Yelp, you can find the scarping code [here](https://github.com/jason-huynh83/Toronto_Restaurant_Predictions/blob/master/yelp_scraper.py)
- The data was cleaned and ready to use for the machine learning algorithm
- Exploratory Data Analysis (EDA) was performed to help understand the data better and visualize the data at hand
- The machine learning classification models that were used are:
  - K-Nearest Neighbours
  - Decision Tree Classifier
  - Random Forest Classifier
  - Logistic Regression

# Code and Resources Used
- Python: Version 3.8
- Packages: Pandas, Numpy, Sklearn, Matplotlib, Seaborn, BeautifulSoup, Imblearn
- [Yelp]('https://www.yelp.ca/search?find_desc=Restaurants&find_loc=Toronto%2C%20ON&start=0)

# The Dataset
- Rest_name: Name of the restaurant
- Rest_rating: Average Rating of the restaurant
- Rest_noreviews: Number of reviews on the restaurant
- Rest_price: Average Price of the restaurant
- Rest_cuisine: Type of cuisine of the restaurant
- Rest_add: Address of the restaurant
- Rest_tel: Restaurant telephone number
- Rest_nbh: The neighbourhood of the restaurant

# Data Cleaning
This part of the project took a great deal of time as there was a lot of cleaning that needed to be done in order to achieve clean data to feed into the machine learning model.
- Parse out restaurant ratings
- Change restaurant prices to inbtegers instead of strings ($$)
- Categorize the type of cuisine into 9 different categories
  - American
  - Asian
  - Caribbean
  - African
  - Middle Eastern
  - European
  - Mexican
  - South American
  - Other
## Handling Missing Data
- Parsed out just streets from rest_add
- Created a dictionary of streets matching to respective neighbourhood
- Mapped the dictionary to any NaN values in the neighbourhood column
- This replaced all NaN values in neighbourhood to the respective neighbourhood the street was in
- In the price section, there are alot (184 records) of values listed as 0, which indicates no price value has been recorded for that restaurant
- In order to account for this missing data, the price will be determined by the average price of restaurants in the given neighbourhood

# Exploratory Data Analysis (EDA)
Developped many visuals that helped understand and explore the data, a full EDA can be found [here](https://github.com/jason-huynh83/Toronto_Restaurant_Predictions/blob/master/Exploratory%20Data%20Analysis.ipynb)below are some highlights:
![](https://github.com/jason-huynh83/Toronto_Restaurant_Predictions/blob/master/Images/graphs.PNG)
![](https://github.com/jason-huynh83/Toronto_Restaurant_Predictions/blob/master/Images/nbh.PNG)

# Model Building
For this model, we will use the following machine learning algorithms:
- K-Nearest Neighbours
- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression

# Model Evaluation

# Conclusion
- In conclusion, the random forest classification performed the best at an average F1 score of 0.75 or 75%. 
- From the classification report we can see that the Random Forest Classifier partnered with the SMOTETomek imbalanced learning performed the best. 
- The average precision score was 0.75 (75%) and average recall score 0.78 (78%)
- **What does this mean for our analysis?**
  - The precision score tells us, of all the restaurant prices we predicted using the model, what fraction or percentage was actaully true?
  - In other words, it is the True Positives/(True Positives + False Positives)
  - In our model, the precision score is separated by the price ranges (1-4) and each precision score is represented respectively
  - The recall score tells us, of all the restaurants that gave it's price listings, what fraction did we correctly predict the price using our model?
  - In other words, it is the True Positives/(True Positives + False Negatives)
