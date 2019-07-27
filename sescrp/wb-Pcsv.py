from bs4 import BeautifulSoup
import io
import re
import csv


# open html file
with io.open(f'html\{input("enterName/>")}.html',  "r",encoding='utf8') as f:
    souce =f.read()


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
with open(f'csv\{input("input CSV/>")}.csv','w', encoding='utf-8')  as c:

    C_writer = csv.writer(c, delimiter=' ')
    C_writer.writerows(zip(res_date, res_price, res_info))
##########
