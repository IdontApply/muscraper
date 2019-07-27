from bs4 import BeautifulSoup #opining modul bs4 is html parser
import io #for opning and saving fails
import re
from selenium import webdriver #web automation driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options #for making the page not appering on the screen
import time
import csv

def htmlgetter():

    # make option oprator that opens the web driver as a headless driver
    options = Options()
    options.add_argument('--headless')
    #####

    #open the sellers file

    with open(r'C:\Users\hmayt\coding\venv\projects\skeleton_scrap\oplist\sellerlist.txt', 'r') as f:
        seller = f.readline().rstrip('\n')

    print(seller)
    # open webdriver and website. use oprator option oprator. ask the user for input
    #main> options=options, executable_path=
    driver = webdriver.Chrome(r'C:\Users\hmayt\coding\webdriver\chromedriver')
    #main> driver.get(input("enter link here/> "))
    driver.get(f'https://saudi.souq.com/sa-en/{seller}/p/profile.html')


    soucenum = BeautifulSoup(driver.page_source, 'html.parser')


    # Gets the sellers date of entering the market
    dm = driver.find_element_by_xpath('//*[@id="content-body"]/div/div[3]/div/div[1]/div[1]/div/div/div[3]').text
    p = re.compile('\d{2}\s[A-Z][a-z]+\s\d{4}')
    memberS = p.findall(dm)[0]
    print(memberS)
    ###################


    #gets the count/number of sales/review
    f = re.compile("[A-Z][a-z ]{4}\s[A-Z][a-z ]{6}\\:\s\d+")
    n = re.compile("\d+")
    g = str(soucenum.find("section"))
    soucen = f.findall(g)
    num = n.findall(soucen[0])
    numb = int(num[0])
    ########


    # gets the number of clicks needed to load the whole page
    clicks = numb//25
    #####


    # test point
    print('\n\n\n\nno prob\n\n\n')
    ###


    #loop-click the show-more button to show the whole page
    Action = ActionChains(driver)
    for x in range(0, clicks):

        time.sleep(1.5)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'showMoreResult')))
        show_more = driver.find_element_by_id('showMoreResult')
        Action.move_to_element(show_more).click().perform()
        print(f"\n\n\nclick number {x}\n\n\n")
    ###########


    # get the Html
    souce = driver.page_source
    #######


    # close the webdriver
    driver.quit()
    #######


    #to sort and clean
    #f = driver.find_element_by_tag_name('span')
    #dataP_num = f.page_source
    #print(f"\n\n\n after this the data should work \n\n\n    \>")
    #print(dataP_num)
    #ex>except TimeoutException:
    ######


    #convert html of the whole page into a string
    soup = str(BeautifulSoup(souce, 'html.parser'))
    ####


    # sort and clean
    #print(soup)
    #print(type(soup))
    #c = soup.prettify()
    #print(type(soup.get_text()))
    #print(soup.prettify().encode("utf-8"))
    #print(soup.find_all('label'))
    ######


    #save html into a file
    with io.open('C:\\Users\\hmayt\\coding\\venv\projects\\skeleton_scrap\\html\\' + seller + '.html', 'w' ,encoding='utf8') as f:
        f.write(soup)
    ######

    return soup , seller

def Pcsv(souce, seller):

# find date-of-purches, price and item-info in the html
    soup = BeautifulSoup(souce, 'html.parser')
    soup_date = soup.find_all("small", class_="gray-color")
    soup_info = soup.find_all("a", class_="display-inline")
    soup_price1 = soup.find_all("ul")
    res_date = []
    res_info = []
    res_price = []
    ##########

    # cleaning tools for finding the price
    f = re.compile("[A-Z][a-z ]{2}\s[a-z ]{2}\s[a-z ]{3}\s[a-z ]{3}\s\d+[.]")
    p = re.compile("\d+")
    #####

    #clean item price and put it in a list
    for price_h in soup_price1:
        info = f.findall(str(price_h))
        if len(info) == 1:
            res_price.append(int(str(p.findall(info[0])[0])))
    ##############

    # clean item info and put it in a list
    for info_h in soup_info:
        info = info_h.get_text().strip()
        res_info.append(str(info))
    ########


    # clean item purches date and put it in a list
    for dater_h in soup_date:
        dater_h = dater_h.get_text().strip()
        p = re.compile('\d{2}\s[A-Z][a-z]+\s\d{4}')
        dater = p.findall(dater_h)
        res_date.append(str(dater).strip("[]''"))
    ######


    # writing csv file while zip combines the to dat lists
    with open(f'C:\\Users\\hmayt\\coding\\venv\\projects\\skeleton_scrap\\csv\\{seller}.csv','w', encoding='utf-8')  as c:

        C_writer = csv.writer(c, delimiter=' ')
        C_writer.writerows(zip(res_date, res_price, res_info))
    ##########


souce, seller = htmlgetter()

Pcsv(souce, seller)
