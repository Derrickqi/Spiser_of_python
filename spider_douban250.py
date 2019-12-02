import requests
import time
import csv
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

url = 'https://movie.douban.com/top250'
urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]



def get_info(source):
    resp = requests.get(source,headers=headers)
    html = resp.text
    dom_tree = etree.HTML(html)
    MovieItemList = dom_tree.xpath('//div[@class="info"]')
    time.sleep(5)
    MovieList = []
    for Single in MovieItemList:
        MovieDict = {}
        titles = Single.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        actors = Single.xpath('div[@class="bd"]/p[@class=""]/text()')[0]
        stars = Single.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        intros = Single.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')
        links = Single.xpath('div[@class="hd"]/a/@href')[0]
        # 判断简介是否为空值
        if intros:
            intros = intros[0]
        else:
            intros = "None"
        MovieDict['title'] = titles
        MovieDict['actors'] = actors.strip()
        MovieDict['stars'] = stars
        MovieDict['intros'] = intros
        MovieDict['links'] = links
        MovieList.append(MovieDict)
    return MovieList


def writemovie(MovieList):
    #将数据导入CSV文件
    with open('doubantop250_movieList.csv','a',encoding="UTF-8",newline='')as f:
    #插入标题头信息
        writer = csv.DictWriter(f,fieldnames=['title','actors','stars','intros','links'])
        writer.writeheader()
        for i in MovieList:
            writer.writerow(i)

def main():
    all_movoeList=[]
    for item in urls:
        source = get_info(item)
        print(source)
        all_movoeList += source
    writemovie(all_movoeList)
if __name__ == '__main__':
    main()














