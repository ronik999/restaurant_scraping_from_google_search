# Restaurant data scraping

Restaurants in Nepal is scraped which is provided by google using Selenium web automation. The data are then stored in csv file named as scraping.csv for storing all restaurants information and review.csv for restaurants review posted by the users in www.google.com.
___
# Execution
1. Clone the repository and install all the required dependencies from requirement.txt.

        pip install -r requirement.txt

2. Download and install python (version 3.7.1) and also download and install the latest version of chrome browser.
3. Download [chrome driver]: http://chromedriver.chromium.org/downloads and update the path of chrome driver on scrape.py and input the path where chromedriver is installed.

        browser = webdriver.Chrome(executable_path='chromedriverpath',options=option)
4. Open package and run __init__.py in terminal:

        python __init__.py
5. Check initially by turning off the headless chrome.

        #option.add_argument('headless')
6. Enable the headless chrome mode and run again.Now the elements are scraped and placed in scraping.csv and review.csv.

_________________


