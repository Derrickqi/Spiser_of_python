import random
import requests
import urllib
import os
from urllib.parse import urlparse
from lxml import etree

user_agent_list = [
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
  'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]
user_agent = random.choice(user_agent_list)
headers = { 'User-Agent': user_agent }
url = 'https://www.xiachufang.com'
res = requests.get(url,headers=headers)
dom_tree = etree.HTML(res.text)
imgs = dom_tree.xpath('//img')
img_path = 'F:/download/'
img_list = []
for img in imgs:
    data_src = img.xpath("@data-src")
    img_src = img.xpath('@src')
    if data_src:
        img_list.append(data_src)
    else:
        img_list.append(img_src)


imgs_list = []
for Single_img in img_list:
    imgs_one = Single_img[0].split('?')[0].split('@')[0]
    imgs_list.append(imgs_one)


for end_img in imgs_list:
     path_name = urlparse(end_img).path[1:]
     Path = os.path.join(img_path,path_name)
     print(end_img)
     urllib.request.urlretrieve(end_img,Path)




