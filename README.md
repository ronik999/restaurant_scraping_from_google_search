# Restaurant data scraping

Restaurants in Nepal is scraped which is provided by google using Selenium web automation. The data are then stored in csv file named as scraping.csv for storing all restaurants information and review.csv for restaurants review posted by the users in www.google.com.
___
# Execution
1. Install all the required dependencies from requirement.txt.
2. Update the path of chrome driver on scrape.py and input the path where chromedriver is installed.

        browser = webdriver.Chrome(executable_path='chromedriverpath',options=option)
3. Run __init__.py in terminal:

        python __init__.py
4. Check intially by turning off the headless chrome.

        #option.add_argument('headless')
5. Enable the headless chrome mode and the elements are scraped and placed in scraping.csv and review.csv.

_________________


