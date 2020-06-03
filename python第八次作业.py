import requests
import lxml.etree as tree

url = "https://movie.douban.com/chart"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77"}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
h_tree = tree.HTML(response.text)
name = h_tree.xpath('//div[@class="pl2"]/a/text()')
actor = h_tree.xpath('//div[@class="pl2"]/p[@class="pl"]/text()')
rank = h_tree.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
num = h_tree.xpath('//div[@class="star clearfix"]/span[@class="pl"]/text()')
pic = h_tree.xpath('//a[@class="nbg"]/img/@src')
for i in range(0, 10):
    print(name[i])
    print(actor[i])
    print(rank[i])
    print(num[i])
    print(pic[i])
    print("\n")




