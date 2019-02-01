from selenium import webdriver
from time import sleep
import os
import csv
import argparse
import time
from selenium.common.exceptions import NoSuchElementException

path= r'./Record'
if not os.path.exists(path):
    os.makedirs(path)
#Importing files

###Enabling headless browser and passing argument
option=webdriver.ChromeOptions()
parser = argparse.ArgumentParser()
parser.add_argument('--headless', help='for headless argument',action="store_true")
args = parser.parse_args()
if args.headless:
    print("HEADLESS MODE ENABLED.")
    option.add_argument('headless')
else:
    print("HEADLESS mode DISABLED. To enable Headless mode run 'python scrape.py --headless'")
browser = webdriver.Chrome(executable_path='chromedriver',options=option)
os.system('chmod +x ./chromedriver')
chromedriver = './chromedriver'
browser.get('https://www.google.com/search?hl=en&tbm=lcl&ei=qkFRXOXnNdf69QOJ07CoAg&q=restaurants+in+nepal&oq=restaurants+in+nepal&gs_l=psy-ab.12...0.0.0.4479.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.uDrCYZozVUA#rlfi=hd:;si:;mv:!1m2!1d27.724099199999998!2d85.3324016!2m2!1d27.7054214!2d85.3073836;tbs:lrf:!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9')



ts=time.time()
scrape_file=open('Record/'+str(ts)+'Scrape.csv','w')
scrape_csv_writer=csv.writer(scrape_file)
scrape_csv_writer.writerow(['Restaurant Name','Restaurant Rating','Restaurant Address','Contact No.','Cuisine','Opening Hours','Google Reviews'])

review_file=open('Record/'+str(ts)+'Review.csv','w')
review_csv_writer=csv.writer(review_file)


def browser_initialization():
    print('THE NAME OF SCRAPED RESTAURANTS WITH ITS DATA ARE AS FOLLOWS:')


def clicking_buttons_to_load_required_data():
    try:
        browser.find_elements_by_class_name("VkpGBb")[i].click();
    except:
        pass

    sleep(5)
    try:
        browser.find_element_by_class_name("BTP3Ac").click();
    except:
        pass

def scrape_restaurants_name():
    try:
        name=browser.find_element_by_class_name("SPZz6b").get_attribute('innerText')
        return(name)
        print(name)
    except NoSuchElementException:
        name='Not Provided'
        return(name)

def scrape_restaurants_rating():
    try:
        rating=browser.find_elements_by_class_name("BTtC6e")[i].get_attribute('innerText')
        return(rating)
    #print(rating)
    except NoSuchElementException:
        rating='Not Provided'
        return(rating)


def scrape_restaurants_address():
    try:
        address=browser.find_element_by_class_name("LrzXr").get_attribute('innerText')
        return(address)
    #print(address)
    except NoSuchElementException:
        address="Not Provided"
        return(address)

def scrape_restaurants_contact():
    try:
        contact=browser.find_element_by_css_selector('.zdqRlf').get_attribute('innerText')
        return(contact)
        #print(contact)
    except NoSuchElementException:
        contact="Not Provided"
        return(contact)

def scrape_restaurants_cuisine():
    try:
        cuisine=browser.find_element_by_css_selector('span.YhemCb:nth-child(2)').get_attribute('innerText')
        return(cuisine)
            #print(cuisine)
    except NoSuchElementException:
        cuisine='Not Provided'
        return(cuisine)

def scrape_restaurants_opening_hours():
    try:
        sleep(2)
        time=browser.find_element_by_class_name('WgFkxc').get_attribute('innerText')
        return(time)
       # print(time)
    except NoSuchElementException:
        time='Not Provided'
        return(time)

def scrape_restaurants_google_review():
    try:
        google_review=browser.find_element_by_css_selector("span.fl:nth-child(3)").get_attribute('innerText')
        return(google_review)
           # print(google_review)
    except NoSuchElementException:
        google_review='Not Provided'
        return(google_review)

def scrape_comments_review(name):
    review_csv_writer.writerow(['Restaurant Name:'+name])
    for reviews in range(3):
        try:
            review=browser.find_elements_by_class_name('jxjCjc')[reviews].get_attribute('innerText')

        except:
            continue
        review_csv_writer.writerow([review])




#################################################      MAIN    #####################################

if __name__ == "__main__":
    for j in range(13):
        for i in range(19):
            clicking_buttons_to_load_required_data()
            name=scrape_restaurants_name()
            print(name)
            rating=scrape_restaurants_rating()
            address=scrape_restaurants_address()
            contact=scrape_restaurants_contact()
            cuisine=scrape_restaurants_cuisine()
            time=scrape_restaurants_opening_hours()
            google_review=scrape_restaurants_google_review()
            scrape_csv_writer.writerow([name,rating,address,contact,cuisine,time,google_review])
            scrape_comments_review(name)
        if j==13:
            break
        #print('loop break as page ends here')

        browser.find_element_by_id("pnnext").click();
        sleep(5)



scrape_file.close()
review_file.close()
browser.quit()
