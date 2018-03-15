#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random
import sys
import csv

max_number_of_google_search_pages = int(sys.argv[1])

index = 1
index = int(index)

links = []
headings = []
images = []

print("------------------------------------------------")
print("WELCOME TO \"MEDIUM\" DESIGNER...BLAH - TROLL CLUB")
print("------------------------------------------------\n")

d = webdriver.Chrome()

# Log in to medium seq
######################
#                    #
#                    #
#                    #
#                    #
#                    #
######################

# search seq
d.get("https://www.google.com")
search_bx = d.find_element_by_name("q")
time.sleep(3)

search_bx.send_keys(str(random.randint(0,9)) + '..' + str(random.randint(10,50)) 
    + ' * design * + site:medium.com')

search_bx.send_keys(Keys.RETURN)

time.sleep(30)

urls = d.find_elements_by_css_selector('h3.r a')

for l in urls:
    links.append(l.get_attribute("href"))
    # print(l.get_attribute('href'))

print(str(index) + " page scraped")



while index < max_number_of_google_search_pages:
    index+=1
    # print "curr_index: " + str(index)
    # print "max_index: " + str(max_number_of_google_search_pages)
    # print len(links)

    next_page = d.find_elements_by_css_selector('#pnnext')
    next_page[0].send_keys(Keys.RETURN)

    # time.sleep(30)

    urls = d.find_elements_by_css_selector('h3.r a')

    for l in urls:
        if "tag" in str(l):
            print(l.get_attribute('href'))
            print("\nlink is not of an article but it is a collection " 
                "of pages with tags in them\n")
        elif int(l.get_attribute('href').count('/')) < 4:
            print(l.get_attribute('href'))
            print("\nThis is not a valid article as it is a medium micro-site"
                " not an article\n")
        else:
            links.append(l.get_attribute("href"))
            # print(l.get_attribute('href'))

    print(str(index) + " pages scraped")

    time.sleep(2)

print("\nFinished scraping "+str(max_number_of_google_search_pages)+ 
    " google searches for medium articles related to design\n")

print len(links)

time.sleep(2)
print("\nNow looking for headings and writing them\n")
time.sleep(2)

myFile = open('data.csv', 'w')

subtractor = 1

with myFile:

    myFields = ['Headings', 'Links', 'Images']
    writer = csv.DictWriter(myFile, fieldnames=myFields)
    writer.writeheader()

    for indiv_link in links:
        print("LINK: " + indiv_link)
        d.get(indiv_link)


        heading = d.title 
        heading = heading.encode('utf-8')
        print("HEADING: " + heading)
        headings.append(heading)



        # if there is a main image, scrape it, if not give it a stockimage
        try:
            image = d.find_element_by_class_name('progressiveMedia-image').get_attribute("src").encode('utf-8')
            print "Successfully found main image link"
            print image
            # images.append(image)
        except:
            print "No main image link found"
            image = 'http://www.ropeworksgear.com/site/skin/img/no-image.jpg'
            # images.append(image)
            pass
        finally:
            images.append(image)

            # d.get(str(image))
            # iml = d.find_element_by_tag_name('img')
            # ac = ActionChains(d)
            # ac.move_to_element(iml)
            # ac.context_click(iml)
            # time.sleep(2)
            # ac.send_keys(Keys.ARROW_DOWN)
            # ac.send_keys(Keys.ARROW_DOWN)
            # ac.send_keys(Keys.ARROW_UP)
            # ac.send_keys(Keys.ARROW_UP)
            # ac.send_keys(Keys.ENTER)
            # ac.send_keys(Keys.ENTER)
            # ac.perform()
            
        print("\n"+str(len(links) - subtractor)+"links left to visit\n")

        subtractor+=1

        writer.writerow({'Headings': heading, 'Links': str(indiv_link), 'Images': str(image)})

print"----------------------"
print"saved data in data.csv\n"
print"----------------------"

d.close()
exit()


