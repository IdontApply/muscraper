# todo clean this
import re
import io
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import time
import random
import math
from os.path import dirname, join #  realpath,
import os

# +++ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++initials
d = os.getcwd()
# dirname = os.path.dirname
# ++++++++++++++++++++
# d_path =
main_path = dirname(d)
# ++++++++++++++++++++
# website =

websiteend = '/s/?as=1&section=2&page=1'
websitebeginning = 'https://saudi.souq.com/sa-en/'
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




#get the next search from the search list file
def readsearch( main_path = main_path):
    with open(join(main_path, 'oplist','catgorylist.txt'), 'r') as f:
        line = f.readline()
    return line.rstrip('\n')


# function for get urls adress to be scarped
def introscrap(main_path = main_path):


    # make oprator for starting the program headless
    mode = 1
    options = Options()
    if mode > 0:
        options.add_argument('--headless')



    # open a chrome webdriver as driver
    driver = webdriver.Chrome(options = options, executable_path = join(main_path , 'webdriver','chromedriver'))
    #####


    # get search element ##### first input
    search1 = readsearch()
    ########


    # get the website {improve}
    driver.get(websitebeginning + search1 + websiteend)
    #######


    # gets count of blocks in a page
    blocks = driver.find_elements_by_class_name('overlay')
    pitems = int(len(blocks))
    print(pitems)
    ############


    # gets the total number of items in the whole search
    j = driver.find_element_by_class_name('total').text
    j1 = j.replace(r",", "")
    Titems = int(re.findall('\d+', j1)[0])
    print(Titems)
    ##########


    driver.quit()


    # get count/number of page ,rondimg up.
    pages = math.ceil(Titems/pitems)
    #####

    url1 = websitebeginning + search1 + websiteend[:-1]
    urls = [ url1 + str(i) for i in range(1, pages)]# >>>pages
    # final list of url to be returned
    print('end of intero scrap')
    return urls, search1



# function that loops over blocks to get seller name, item name/details, item-profile-link and price.
def scraper(url, main_path = main_path):

    print('scraper start')
    Psellers = []
    Pitemsinfo = []
    Pprices = []
    Plinks = []
    Prating = []
    Ppage = []

    # run driver headless if mode = 1
    mode = 1
    options = Options()
    if mode > 0:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options = options, executable_path = join(main_path , 'webdriver','chromedriver'))
    #####################

    # {what is this}
    if len(url) <= 1:
        return
    #____________########

    driver.get(url)
    blocks = driver.find_elements_by_class_name('overlay')



    for block in blocks:

        #print('start block loop')
        E_loaded = False
        count1 = 0


        try:

            time.sleep(1)

            Action = ActionChains(driver)

            print( 'after ActionChains' )
            print('\n\n')
            Action.move_to_element(block).click().perform()

            print('\n\n')
            WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="quickViewReveal"]/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/img')))

            seller = driver.find_element_by_class_name('sellerName').text
            Psellers.append(str(seller))

            i = driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/h1/a').text
            item = i.replace(',','')

            Pitemsinfo.append(item)




            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)





        except TimeoutException:
            Pitemsinfo.append('n')
            Psellers.append('n')
            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)

        except StaleElementReferenceException:

            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)

        count1 = count1 + 1










        time.sleep(2 + (2 / random.randint(1,10)))

    # find all the prices after all the page has loaded
    prices = driver.find_elements_by_class_name('itemPrice')
    for p in prices:
                p1 = re.findall('\d*[,]*\d+[.]\d\d', p.text)
                if len(p1) > 0:
                    #print(p1)
                    price = p1[0]
                    Pprices.append(price)
    #############

    # find all links after all the page has loaded
    links1 = driver.find_elements_by_xpath('//*[@id="content-body"]/div[7]/div/div/div')
    for l in links1:

        link1 = l.find_element_by_css_selector('a')
        link = link1.get_attribute('href')
        Plinks.append(link)
    print(Plinks)
    ###################


    # find all  items whice is rated, after all the page has loaded.
    ratings = driver.find_elements_by_xpath('//*[@id="content-body"]/div[7]/div/div/div/div/div[2]/a/ul/li[2]')
    regexp = re.compile(r'star')
    for r in ratings:
        if regexp.search(r.get_attribute('innerHTML')):
            Prating.append('1')
        else:
            Prating.append('0')
    ################################

    # get page number, make a list from that number. and get  the html for the whole page
    page_num1 = url[-6:].split('=')
    for p in page_num1:
        if p.isdigit():
            page_num = p

    Ppage = [page_num]*60
    page_html = driver.page_source
    ############


    driver.quit()

    # save page_html with url name
    regex = re.compile('[^a-zA-Z0-9]')
    urlnochar = regex.sub('', url)
    with io.open(join(main_path , 'html' , urlnochar +'.html'), 'w' ,encoding='utf8') as f:
        f.write(page_html)
    ##############

    print(Psellers, Pitemsinfo, Pprices, Plinks, Prating, Ppage)

    return Psellers, Pitemsinfo, Pprices, Plinks, Prating, Ppage
