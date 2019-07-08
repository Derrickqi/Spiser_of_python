from bs4 import BeautifulSoup
import requests
import request
import urllib
import time
import os

url = 'http://jandan.net/ooxx/page-1'
urls = ['http://jandan.net/ooxx/page-{}'.format(i) for i in range(1, 10)]
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': '_ga=GA1.2.162437312.1562479460; _gid=GA1.2.580201545.1562479460'
}
file_path = 'D:\download'
judg_file = os.path.exists('D:\download')


def get_url(url):
    # judg file is exsist or not
    if judg_file == False:
        os.mkdir(file_path)
    else:
        pass

    wb_data = requests.get(url, header)
    time.sleep(1)
    Soup = BeautifulSoup(wb_data.text, 'lxml')
    pic_url = Soup.find_all('img')
    path = "D://download/"
    down_load = []

    for picture in (pic_url):
        pic_list = picture.get('src')
        down_load.append("http:" + pic_list)

    for item in down_load:
        urllib.request.urlretrieve(item, path + item[-10:])
        print('downloading ............')


def get_more_url():
    for get_more in urls:
        get_url(get_more)


get_more_url()

