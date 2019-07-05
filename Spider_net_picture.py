# -*-coding:utf-8-*-

import  requests
from bs4 import  BeautifulSoup
import time
import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.174.134:27017/")
mydb = myclient["ddsdb"]
mycol = mydb["t5"]
url = "https://shenzhen.cncn.com/jingdian/"
urls = ["https://shenzhen.cncn.com/jingdian/1-{}-0-0.html" .format(str(i)) for i in range(1,14,1)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'cookie':'local_city_name=%E5%8C%97%E4%BA%AC; local_zone=110000%7Cbeijing%7C%B1%B1%BE%A9%7C54511; local_city_name=%E5%8C%97%E4%BA%AC; UM_distinctid=16bb0687a372f9-043522f3aecb89-e353165-1fa400-16bb0687a383de; CNZZDATA1089612=cnzz_eid%3D1133401860-1562027537-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1562027537; PHPSESSID=497t0sddltl9nsrm5bbnndms50; Hm_lvt_d64174522c86449826babe56fb2a88ff=1562032766; Hm_lpvt_d64174522c86449826babe56fb2a88ff=1562032769'
}

def get_url(url):
    wb_data = requests.get(url,headers)
    time.sleep(2)
    Soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = Soup.select("img[width='287']")
    titles = Soup.select("  div.title > b")

    for title,img in zip(titles,imgs):
        data = {
            'title':title.get_text(),
            'img':img.get('data-original')
        }
        print(data)
        mycol.insert_one(data)

for single_url in urls:
    get_url(single_url)



"""
body > div.content.mt20 > div.box_list > div.city_spots > div.icon > ul > li.first > a > img
body > div.content.mt20 > div.box_list > div.city_spots > div.city_spots_list > ul > li:nth-child(2) > a > div.title > b
"""





