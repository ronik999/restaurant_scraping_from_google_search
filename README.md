# Restaurant data scraping

Restaurants in Nepal is scraped which is provided by google using Selenium web automation. The data are then stored in csv file named as scraping.csv for storing all restaurants information and review.csv for restaurants review posted by the users in www.google.com.
___
# Execution
1. Clone the repository and install all the required dependencies from requirement.txt.

        pip install -r requirements.txt

2. Download and install python (version 3.7.1) and also download and install the latest version of chrome browser.

3. Open folder named package and run '__ init__.py' in terminal:

        python __init__.py
4. To turn on the headless mode, edit 'scrape.py' file by removing the hash-comment '#' on the eleventh line  

        option.add_argument('headless')
5. Now the headless mode is enabled. Run the program again and the elements are scraped and placed in scraping.csv and review.csv.

_________________


