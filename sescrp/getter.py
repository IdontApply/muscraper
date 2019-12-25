from bs4  import BeautifulSoup  # opining modul bs4 is html parser
import io  # for opning and saving fails
import re
from selenium import webdriver  # web automation driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  # for making the page not appering on the screen
import time
import mualchemy.aualchemy as au

from os.path import dirname, join  # realpath,
from os import getcwd
from sys import exit
import datetime


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++initials

d = getcwd()
# dirname = os.path.dirname
# ++++++++++++++++++++
# d_path =
main_path = dirname(d)
# ++++++++++++++++++++




def insert_into_seller(session, s, seller_date, item_count):
    s.rated = True
    s.eneterydate = seller_date
    s.totalsales = int(item_count)
    session.commit()


def insert_items(session, seller_id, items_list, sales_table):

    for items in items_list:
        items_row = sales_table(seller_id=seller_id, date_of_sale=items[0], price=items[1], product_info=items[2])
        session.add(items_row)
    pass


def htmlgetter(sellername, main_path=main_path):

    # make option oprator that opens the web driver as a headless driver
    options = Options()
    #options.add_argument('--headless')


    # open webdriver and website. use oprator option oprator.
    #main>
    driver = webdriver.Chrome(options = options, executable_path = join(main_path , 'webdriver','chromedriver'))
    url = f'https://saudi.souq.com/sa-en/{sellername}/p/profile.html'
    driver.get(url)
    soucenum = BeautifulSoup(driver.page_source, 'html.parser')
    #########


    # Gets the sellers date of entering the market
    dm = driver.find_element_by_xpath('//*[@id="content-body"]/div/div[3]/div/div[1]/div[1]/div/div/div[3]').text
    p = re.compile('\d{2}\s[A-Z][a-z]+\s\d{4}')
    memberS = p.findall(dm)[0]
    member_sense = datetime.datetime.strptime(memberS, '%d %B %Y')
    print(f'\n\n\n{memberS}\n\n\n')
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


    #loop-click the show-more button to show the whole page
    Action = ActionChains(driver)
    for x in range(0, clicks):

        time.sleep(1.5)
        WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.ID, 'showMoreResult')))
        show_more = driver.find_element_by_id('showMoreResult')
        Action.move_to_element(show_more).click().perform()
        print(f"\n\n\nclick number {x}\n\n\n")
    ###########


    # get the Html
    souce = driver.page_source
    #######


    #convert html of the whole page into a string
    soup = str(BeautifulSoup(souce, 'html.parser'))
    ####


    #save html into a file
    with io.open(join(main_path ,'html' , sellername + '.html'), 'w' , encoding='utf8') as f:
        f.write(soup)
    ######


    return soup , member_sense, numb


def Pcsv(souce, seller):


    # find date-of-purches, price and item-info in the html
    soup = BeautifulSoup(souce, 'html.parser')
    soup_date = soup.find_all("small", class_="gray-color")
    soup_info = soup.find_all("a", class_="display-inline")
    soup_price1 = soup.find_all("ul")
    res_date = []
    res_info = []
    res_price = []



    # cleaning tools for finding the price
    f = re.compile("[A-Z][a-z ]{2}\s[a-z ]{2}\s[a-z ]{3}\s[a-z ]{3}\s\d+[.]")
    p = re.compile("\d+")



    #clean item price and put it in a list
    for price_h in soup_price1:
        info = f.findall(str(price_h))
        if len(info) == 1:
            res_price.append(int(str(p.findall(info[0])[0])))



    # clean item info and put it in a list
    for info_h in soup_info:
        info = info_h.get_text().strip()
        res_info.append(str(info))



    # clean item purches date and put it in a list
    for dater_h in soup_date:
        dater_h = dater_h.get_text().strip()
        p = re.compile('\d{2}\s[A-Z][a-z]+\s\d{4}')
        dater1 = str(p.findall(dater_h)).strip("[]''")
        dater = datetime.datetime.strptime(dater1, '%d %B %Y')
        res_date.append(dater)

    return zip(res_date, res_price, res_info)




def main(main_path=main_path, ):
    print(getcwd())
    pdates, search, product, sales, seller, session = au.tables(join(main_path, 'config\dbconfig.yaml'))
    sellertable = session.query(seller).filter_by(rated=None).first()  # clean
    s = sellertable  # cleab
    sellername = s.name
    seller_id = s.id

    try:
        souce, seller_date, item_count = htmlgetter(sellername)
        print(seller_date)
    except ec.NoSuchElementException:
        print('zero sales')
        s.rated = False
        session.commit()
        exit()

    items_list = Pcsv(souce, sellername)
    insert_into_seller(session, s, seller_date, item_count)
    insert_items(session, seller_id, items_list, sales)
    session.commit()



