import scrapy

class RestaurantDataSpider(scrapy.Spider):
    name = "SwagMeals" #We have a little fun
    start_urls = [
        'https://www.yelp.com/biz/basil-thai-cuisine-ballantyne-charlotte-2',
        'https://www.yelp.com/biz/chick-fil-a-charlotte-24?osq=Chick-fil-A',
        'https://www.yelp.com/biz/chipotle-mexican-grill-charlotte-10',
        'https://www.yelp.com/biz/clean-juice-stonecrest-charlotte',
        'https://www.yelp.com/biz/crumbl-charlotte-charlotte?osq=Crumbl+Cookies',
        'https://www.yelp.com/biz/firebirds-wood-fired-grill-charlotte?osq=firebirds',
        'https://www.yelp.com/biz/the-flying-biscuit-cafe-charlotte-8?osq=flying+biscuit',
        'https://www.yelp.com/biz/gong-cha-charlotte-2?osq=gong+cha',
        'https://www.yelp.com/biz/ilios-crafted-greek-stonecrest-charlotte?osq=Ilios+Greek',
        'https://www.yelp.com/biz/jersey-mikes-subs-charlotte-15?osq=jersey+mikes',
        'https://www.yelp.com/biz/marble-slab-creamery-charlotte',
        'https://www.yelp.com/biz/nothing-but-noodles-charlotte-3',
        'https://www.yelp.com/biz/ramen-bar-kazoku-charlotte',
        'https://www.yelp.com/biz/smashburger-charlotte-5',
        'https://www.yelp.com/biz/starbucks-charlotte-44',
        'https://www.yelp.com/biz/super-chix-charlotte',
        'https://www.yelp.com/biz/tap-and-vine-stonecrest-charlotte',
        'https://www.yelp.com/biz/the-office-craft-bar-and-kitchen-charlotte-2',
        'https://www.yelp.com/biz/wendys-charlotte-6',
    ]
    custom_settings = {
       'DOWNLOAD_DELAY': 5,# Dont want to overload their servers 😱😱😱
       'FEED_EXPORT_FIELDS': ['restaurant_name', 'rating', 'num_ratings'],#Creates fields in the csv
       'FEED_FORMAT': 'csv',#File type specified
       'FEED_URI': r'D:\WebScraper\Restaurant_Data_Scraped.csv',#Change this to where you want to save it
       'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',#Im a real person 🤫
   }
   
    def parse(self, response):
        #Get the name
         restaurant_name = response.css('h1::text').get().strip()
        #Get the rating
         ratings = response.css('div[role="img"][aria-label$="star rating"]::attr(aria-label)').getall()
        #Get amount of ratings
         reviews_text = response.css('a.css-19v1rkv::text').get()
         num_reviews = reviews_text.split()[0][1:] #Remove parantheses and the word "ratings". "(400 ratings)" becomes "400"
        #Yelp had the incorrect name for Clean Juice on their site so this fixes that in the csv. Not sure how practical this is if I didn't know of the error and was using a much larger sample set of restaurants
         if restaurant_name == "Stonecrest":
             restaurant_name = "Clean Juice"
         for rating in ratings:
             numeric_rating = rating.split()[0] #Removes "star rating" from "x star rating". "3 star rating" becomes "3"
             yield {
                'restaurant_name': restaurant_name,
                'rating': numeric_rating,
                'num_ratings': num_reviews,
             }
             
