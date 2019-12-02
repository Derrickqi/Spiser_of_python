import requests
import random
import urllib
import time
import os
from urllib.parse import urlparse

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
urls = ['https://www.duitang.com/napi/blog/list/by_album/?album_id=95408818&limit=100&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start={}'.format(i) for i in range(24,120+24,24)]
download_path = 'F:/download/'
img_list = []
i = 1
def get_url(url):
  res = requests.get(url)
  resp = res.json()
  for item in resp['data']['object_list']:
     img_url = item['photo']['path']
     img_list.append(img_url)



def main():
  global i
  for img_url in urls:
      get_url(img_url)
      for img in img_list:
          path_name = urlparse(img).path.split('/')[-1]
          img_path = download_path + str(i) + "-" + path_name
          print(img_path)
          time.sleep(1)
          urllib.request.urlretrieve(img,img_path)
          i += 1
if __name__ == '__main__':
  main()