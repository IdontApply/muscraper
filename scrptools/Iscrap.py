from bs4 import BeautifulSoup as bs #opining modul bs4 is html parser
#import io #for opning and saving fails
#import re
from selenium import webdriver #web automation driver
#from selenium.webdriver.support import expected_conditions as EC #delet later
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.chrome.options import Options #for making the page not appering on the screen
import time
from selenium.webdriver.support.ui import WebDriverWait

def fun1():
    urls = ["https://www.linkedin.com/jobs/search/?f_E=2&f_TP=1%2C2&keywords=data%20science&location=Worldwide&locationId=OTHERS.worldwide&start={}".format(i) for i in range(25, 975, 25)]
    page1 = 'https://www.linkedin.com/jobs/search/?f_E=2&f_TP=1%2C2&keywords=data%20science&location=Worldwide&locationId=OTHERS.worldwide'
    urls.insert(0,page1)
    driver = webdriver.Chrome(executable_path = r'C:\Users\hmayt\coding\webdriver\chromedriver.exe')
    driver.get('https://linkedin.com')
    return driver, urls

def fun2(driver, urls):
    for c, url in enumerate(urls, 1):
        driver.get(url)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1019"]/span[2]')))
        time.sleep(0.5)
        thtml = driver.page_source


        with open(r'C:\Users\hmayt\coding\venv\projects\skeleton_scrap\html\html' + str(c) + '.html', 'w' ,encoding='utf8') as f:
            f.write(thtml)

def fun3():
    htmlsn = list(range(1,40))
    print(htmlsn)






















# make option oprator that opens the web driver as a headless driver
#main> options = Options()
#main> options.add_argument('--headless')
#####


# open webdriver and website. use oprator option oprator. ask the user for input
#main> options=options, executable_path=
#driver = webdriver.Chrome(input('Enter chromedriverpath'))
#main> driver.get(input("enter link here/> "))
#driver.get(input('Enter Url for the seller'))


#soucenum = BeautifulSoup(driver.page_source, 'html.parser')


# Gets the sellers date of entering the market
#dm = driver.find_element_by_xpath('//*[@id="content-body"]/div/div[3]/div/div[1]/div[1]/div/div/div[3]').text
#p = re.compile('\d{2}\s[A-Z][a-z]+\s\d{4}')
#memberS = p.findall(dm)[0]
#print(memberS)
###################


#gets the count/number of sales/review
#f = re.compile("[A-Z][a-z ]{4}\s[A-Z][a-z ]{6}\\:\s\d+")
#n = re.compile("\d+")
#g = str(soucenum.find("section"))
#soucen = f.findall(g)
#num = n.findall(soucen[0])
#numb = int(num[0])
########


# gets the number of clicks needed to load the whole page
#clicks = abs(-numb//25)
#####


# test point
#print('\n\n\n\nno prob\n\n\n')
###


#loop-click the show-more button to show the whole page
#Action = ActionChains(driver)
#for x in range(0, clicks):

#    time.sleep(1.5)
#    show_more = driver.find_element_by_id('showMoreResult')
#    Action.move_to_element(show_more).click().perform()
#    print(f"\n\n\nclick number {x}\n\n\n")
###########


# get the Html
#souce = driver.page_source
#######


# close the webdriver
#driver.quit()
#######


#to sort and clean
#f = driver.find_element_by_tag_name('span')
#dataP_num = f.page_source
#print(f"\n\n\n after this the data should work \n\n\n    \>")
#print(dataP_num)
#ex>except TimeoutException:
######


#convert html of the whole page into a string
#soup = str(BeautifulSoup(souce, 'html.parser'))
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
#with io.open(input('name/> '), 'w' ,encoding='utf8') as f:
#    f.write(soup)
######
