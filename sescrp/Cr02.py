import io
import re
from listsprater import list_sprater
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
import csv
from scraperCr import scraper, introscrap
from multiprocessing import Pool, current_process
import datetime


#/home/mytham9/workspace/working/thescraper/
def deletsearched():
    with open(r'/home/mytham9/workspace/working/thescraper/oplist/catgorylist.txt', 'r', encoding='utf-8') as fo:
        lines = fo.readlines()
        line = fo.readline()
    with open(r'/home/mytham9/workspace/working/thescraper/oplist/Bkcatgorylist.txt', 'w', encoding='utf-8') as fw:
        fw.writelines(lines)
    with open(r'/home/mytham9/workspace/working/thescraper/oplist/catgorylist.txt', 'w', encoding='utf-8') as fw:
        fw.writelines(lines[1:])
    return line.rstrip('\n')


def singlecsv(values, date1, search1):
    filename2 ='/home/mytham9/workspace/working/thescraper/sellersclist/' + search1  + '_' + str(date1) +'.csv'
    with open(filename2,'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for val in values:
            writer.writerow([val])


#if __name__ == '__main__':


def log(url):



    filename = '/home/mytham9/workspace/working/thescraper/mon/' + str(current_process()) + '.txt'
    with open( filename , 'a') as file:
        file.write( url + '\n')
        file.close()
        #locks and logs in the log file



# scraper function that runs a function  that takes url and scrap the page, clicking every  item elements in the page in the process to show the data
#    def scrp(url):

        #log(url)
#        return scraper(url) # this function is imported from scraperCr



def cr():



    urls, serach = introscrap()
    # scraper function that runs a function  that takes url and scrap the page, clicking every  item elements in the page in the process to show the data


    #urlsodd = ["https://saudi.souq.com/sa-en/" + search1 + "/s/?as=1&section=2&page={}".format(j) for j in oddnums]
    #urlseven = ["https://saudi.souq.com/sa-en/" + search1 + "/s/?as=1&section=2&page={}".format(k) for k in evennums]

    #if initpage_oddnum % 2 != 0:
    #    urlseven.append(int(0))
    #else:
    #    urlsodd.append(int(0))
            # initialize sellers, iteminfo, prics, links and ratings list. p.s rating is donted by having a rating or not having a rating
    #sellers = []
    #itemsinfo = []
    #prices = []
    #links = []
    #ratings = []
    #################
    with open( '/home/mytham9/workspace/working/thescraper/mon/1.text', 'a') as file:
        file.write('started')




                #print(f'\nbefore the run of scrapern\n')
                #s, i, p, l, r, E_finished = scraper(url, 60, 1, driver)
    pool = Pool(processes=3)
    results_page_blocks = pool.map(scraper, urls)

    print('results_page_blocks')
    print(results_page_blocks)
    print('results_page_blocks')
#    results = []
#    for r in range(1, 2):
#        results.append(pool.apply_async(foo, args=(words[i], numbers[i])))


    pool.close()
    pool.join()
#    results = [r.get() for r in results]

    #print('\n\n\n\n\n\n\n')
    results, sellers = list_sprater(results_page_blocks, serach)
    #print(results)

    print('results')
    print(results)
    print('results')

    print('sellers')
    print(sellers)
    print('sellers')

    search1 = deletsearched()
    print('search1')
    print(search1)
    print('search1')

    date1 = datetime.date.today()
    filename1 ='/home/mytham9/workspace/working/thescraper/csv/' + serach  + '_' + str(date1) +'.csv'
    print(sellers)
    print(type(sellers))
    singlecsv(sellers, date1, serach)

    with open( filename1 , 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        writer.writerows(results)

    with open( r'/home/mytham9/workspace/working/thescraper/oplist/csvfilesfordb.txt' , 'w', encoding='utf-8') as f:
        f.write(filename1+'\n')


def con1():
    with open(r'/home/mytham9/workspace/working/thescraper/oplist/control.txt', 'r', encoding='utf-8') as fo:
        l = fo.readline()
    return l


# close driver
