from selenium import webdriver
from time import sleep
import csv
from selenium.common.exceptions import NoSuchElementException

#Importing files

###Enabling headless browser

option=webdriver.ChromeOptions()
#option.add_argument('headless')
browser = webdriver.Chrome(executable_path='./chromedriver',options=option)
browser.get('https://www.google.com/search?hl=en&tbm=lcl&ei=EHIwXJmxLoz99QPamp6IAw&q=RESTAurants+in++nepal&oq=RESTAurants+in++nepal&gs_l=psy-ab.12...0.0.0.5837.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.oAAOM-yito0#rlfi=hd:;si:;mv:!1m2!1d27.734635500000003!2d85.36469360000001!2m2!1d27.6753043!2d85.30555580000001;tbs:lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9')

def scrape_elements():

    csv_file=open('scraping.csv','w')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Restaurant Name','Restaurant Rating','Restaurant Address','Contact No.','Cuisine','Opening Hours','Google Reviews'])


    csv_file1=open('review.csv','w')
    csv_writer1=csv.writer(csv_file1)


    for j in range(13):
        for i in range(19):
            try:
                browser.find_elements_by_class_name("VkpGBb")[i].click();
            except:
                continue

            sleep(5)
            try:
                browser.find_element_by_class_name("BTP3Ac").click();
            except:
                continue

        #Scraping Name
            try:
                name=browser.find_element_by_class_name("SPZz6b").get_attribute('innerText')
                print(name)
            except NoSuchElementException:
                name='Not Provided'
        #Scraping rating
            try:
                rating=browser.find_elements_by_class_name("BTtC6e")[i].get_attribute('innerText')
        #print(rating)
            except NoSuchElementException:
                rating='Not Provided'

        #Scraping Address
            try:
                address=browser.find_element_by_class_name("LrzXr").get_attribute('innerText')
        #print(address)
            except NoSuchElementException:
                address="Not Provided"

        #Scraping Contact
            try:
                contact=browser.find_element_by_css_selector('.zdqRlf').get_attribute('innerText')
            #print(contact)
            except NoSuchElementException:
                contact="Not Provided"

        #Scraping cuisine
            try:
                cuisine=browser.find_element_by_css_selector('span.YhemCb:nth-child(2)').get_attribute('innerText')
            #print(cuisine)
            except NoSuchElementException:
                cuisine='Not Provided'

        #scraping Opening Hours
            try:
                sleep(2)
                time=browser.find_element_by_class_name('WgFkxc').get_attribute('innerText')
           # print(time)
            except NoSuchElementException:
                time='Not Provided'

        #scraping google review
            try:
                google_review=browser.find_element_by_css_selector("span.fl:nth-child(3)").get_attribute('innerText')
           # print(google_review)
            except NoSuchElementException:
                google_review='Not Provided'

        #scraping comments review
            csv_writer1.writerow(['Restaurant Name:'+name])
            for reviews in range(3):
                try:
                    review=browser.find_elements_by_class_name('jxjCjc')[reviews].get_attribute('innerText')

                except:
                    continue

                csv_writer1.writerow([review])

            csv_writer.writerow([name,rating,address,contact,cuisine,time,google_review])

        if j==13:

        #print('loop break as page ends here')
            break
        browser.find_element_by_id("pnnext").click();
        sleep(5)

    csv_file.close()
    browser.quit()

