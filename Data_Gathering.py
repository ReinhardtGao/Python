import requests
import json
from selenium import webdriver
from lxml import etree
import os
query = "吴亦凡"
picpath = '/Users/jgao-mdp/PycharmProjects/Python/Gathered_Result'
if not os.path.isdir(picpath):
    os.mkdir(picpath)

'''Image download'''
def download(src, id):
    dir = picpath + '/' + str(id) + '.webp'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('Unable to load picture')

'''Cycle Getting'''
def getImage(page):
    print('Downloading #', page+1, 'page')
    page = page * 15
    request_url = 'https://movie.douban.com/subject_search?search_text=' + query + '&cat=1002'
    driver = webdriver.Chrome('/Users/jgao-mdp/Downloads/chromedriver')
    url = request_url + '&start=' + str(page)
    driver.get(url)
    html = etree.HTML(driver.page_source)
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_path = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_path)
    for src, title in zip(srcs, titles):
	    download(src, title.text)
    print('Gathering complete!')
    driver.close()

if __name__ == '__main__':
    for i in range(0, 5):
        getImage(i)
