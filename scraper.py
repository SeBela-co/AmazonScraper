import csv
from csv import reader
from bs4 import BeautifulSoup

from selenium import webdriver

url = 'https://www.amazon.com'


def main(url):
    driver = webdriver.Chrome('C:\Program Files\ChromeDriver\chromedriver.exe')

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    affiliated_link = ''

    try:
        title = soup.find('span', 'a-size-large product-title-word-break').text.strip()
    except:
        title = 'Page Did Not Load'

    try:
        price = soup.find('span', 'a-size-medium a-color-price priceBlockBuyingPriceString').text
    except:
        try:
            price = soup.find('span', 'a-size-base a-color-price').text
        except:
            price = 'Price Not Found'

    try:
        split_rating = soup.find('span', 'a-icon-alt').text.split(" ")
        rating = split_rating[0]
    except:
        rating = 'Rating Not Found'

    try:
        split_link = url.split("/")
        asin_num = str(split_link[5])
    except:
        asin_num = "Page Didn't Load"

    try:
        img_link_parent = soup.find('div', 'imgTagWrapper')
        img_link = img_link_parent.img['src']
    except:
        img_link = 'No Image Found'

    result = (title, affiliated_link, price, img_link, rating, asin_num)
    records.append(result)


records = []
with open('file.csv', 'r') as f:
    file = csv.reader(f)
    list_of_rows = list(file)
for links in range(len(list_of_rows)):
    print(list_of_rows[links][0])
    main(list_of_rows[links][0])
with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Description', 'Affiliated Link', 'Price', 'Image Link', 'Rating', 'ASIN #'])
    writer.writerows(records)
