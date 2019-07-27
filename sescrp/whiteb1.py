import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
import time
import random
import math
from multiprocessing import Pool, Lock
import datetime
import csv
from listsprater import list_sprater
import io
import logging




logging.basicConfig(filename = '/home/mytham9/workspace/working/thescraper/log/log1.Log', level = logging.DEBUG )


def log(url, logger = logging.getLogger()):

    lock.acquire()
    logger.info(multiprocessing.current_process() + url)
    lock.release()
    #locks and logs in the log file
def introscrap(search):

    #====================4

    # make oprator for starting the program headless
    mode = 1

    options = Options()
    if mode > 0:
        options.add_argument('--headless')




        ###########

    #++++++++++++++++++++ 1
    #d_path =
    #++++++++++++++++++++
    #website =
    #++++++++++++++++++++

        # open a chrome webdriver as driver
        #driver = webdriver.Chrome(r'C:\Users\maytahm\coding\chr\chromedriver')*981
    driver = webdriver.Chrome(options = options, executable_path = r'/home/mytham9/workspace/webdriver/chromedriver')
#    driver = webdriver.Chrome(options = options, executable_path = r'/home/mytham9/workspace/webdriver/chromedriver')

        ##########
        # enter search element ##### first input
    search1 = search
    ########


        #get the website {improve}
    driver.get('https://saudi.souq.com/sa-en/' + search1 + '/s/?as=1&section=2&page=1')
        #######





        # get all blocks of itemsin the first  page
    blocks = driver.find_elements_by_class_name('overlay')
        #xpath("//*[contains(text(), 'Quick View')]")
        ########


        # gets count of blocks in a page
    pitems = int(len(blocks))
        #print(type(blocks))
        #####

        # initialize sellers, iteminfo, prics, links and ratings list. p.s rating is donted by having a rating or not having a rating
    sellers = []
    itemsinfo = []
    prices = []
    links = []
    ratings = []
        #################

        # gets the total number of items in the whole search
    j = driver.find_element_by_class_name('total').text
        #print(j)
    j1 = j.replace(r",", "")
        #print(j1)
    Titems = int(re.findall('\d+', j1)[0])
        ##########


    print(f"===================")
    driver.quit()


        # get count/number of page ,rondimg up.
    pages = math.ceil(Titems/pitems)
        #print(pages)
        #####
    #initpage_oddnum = math.ceil(pages/2)
        #finalpage_oddnum  = pages
        #initpage_evennum  = 1
        #finalpage_evennum = int(pages/2)
        #########
        # make the even and odd number list
    #oddnums = []
    #evennums = []

    #for num in range(1, pages):
    #    if num % 2 != 0:
    #        oddnums.append(str(num))
    #    else:
    #        evennums.append(str(num))



    urls = ["https://saudi.souq.com/sa-en/" + search1 + "/s/?as=1&section=2&page={}".format(i) for i in range(1, pages)]

    return urls





def scraper(search):

    url = introscrap(search)
    log(url)
    print('\n\n')
    print(url)
    print('\n\n')
    print('start scraper')
    #print(f'\nscraper is working\n')
    Psellers = []
    Pitemsinfo = []
    Pprices = []
    Plinks = []
    Prating = []

    mode = 0
    options = Options()


    if mode > 0:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options = options, executable_path = r'/home/mytham9/workspace/webdriver/chromedriver')

    if len(url) <= 1:
        return
    driver.get(url)
    #print(f'\nthe problom is not here\n')
    blocks = driver.find_elements_by_class_name('overlay')




    for block in blocks:

        print('start block loop')
        E_loaded = False
        count1 = 0


        try:
            #print('scrapb run')
            #print('\n\n')
            #print( url )
            #print('\n\n')
            time.sleep(1)
            #print('\n\n')
            #print( 'after timesleep' )
            #print('\n\n')
            Action = ActionChains(driver)
            #print('\n\n')
            #print( 'after ActionChains' )
            #print('\n\n')
            Action.move_to_element(block).click().perform()
            #print('\n\n')
            #print( 'after move element before webdriverwait' )
            #print('\n\n')
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="quickViewReveal"]/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/img')))
            #print('\n after wait')
            seller = driver.find_element_by_class_name('sellerName').text
            Psellers.append(str(seller))

            i = driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/h1/a').text
            item = i.replace(',','')
            #print(f'>>>>>>>>>>>>>>>>>>')
            #print(item)
            #print(seller)
            #print(f'<<<<<<<<<<<<<<<<<<')
            Pitemsinfo.append(item)




            #print(item.text)
            #print(price.text)
            #print(seller.text)
            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)

            #print('scrapb end')





        except TimeoutException:
            #print('expect 1')
            Pitemsinfo.append('non')
            Psellers.append('non')
            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)

        except StaleElementReferenceException:
            print('expect 2')
            Action1 = ActionChains(driver)

            Action1.move_to_element(driver.find_element_by_xpath('//*[@id="quickViewReveal"]/div[1]/button/span')).click().perform()
            time.sleep(1)

        count1 = count1 + 1
        #print(f"count:")
        #print(count1)









        time.sleep(2 + (2 / random.randint(1,10)))

    # find all the prices after all the page has loaded
    prices = driver.find_elements_by_class_name('itemPrice')
    for p in prices:
                p1 = re.findall('\d*[,]*\d+[.]\d\d', p.text)
                #print(price)
                if len(p1) > 0:
                    #print(p1)
                    price = p1[0]
                    Pprices.append(price)
    #############

    # find all links after all the page has loaded
    links1 = driver.find_elements_by_css_selector('div div.columns.small-7.medium-12 a')

    for l in links1:

        link = l.get_attribute('href')
        Plinks.append(link)
    #print(Plinks)
    ###################

    # find all  items whice is rated, after all the page has loaded.
    ratings = driver.find_elements_by_xpath('//*[@id="content-body"]/div[7]/div/div/div/div/div[2]/a/ul/li[2]')
    regexp = re.compile(r'star')
    for r in ratings:
        #print(f'<<<<<<<<<<<<<<<<<<')
        #print (r.get_attribute('innerHTML'))
        #print(f'<<<<<<<<<<<<<<<<<<')

        if regexp.search(r.get_attribute('innerHTML')):
            Prating.append('1')
        else:
            Prating.append('non')

    ################################
    driver.quit()

    return Psellers, Pitemsinfo, Pprices, Plinks, Prating
    # function that loops over blocks to get seller name, item name/details, item-profile-link and price.




def init(l):
    global lock
    lock = l
    #initialize lock to be geven to the pool

def cr(search = 'speaker'):


    l = Lock()
    pool = Pool(processes=3, initializer=init, initargs=(l,))
    results_page_blocks = pool.map(scraper, search)


    pool.close()
    pool.join()
    #    results = [r.get() for r in results]

    print('\n\n\n\n\n\n\n')
    results = list_sprater(results_page_blocks)
    print(results)

    date1 = datetime.date.today()
    filename1 ='csv/' + search1  + '_' + str(date1) +'.csv'
    with open( filename1 , 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerows(results)
        #main fun

cr()
