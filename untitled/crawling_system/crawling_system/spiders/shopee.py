import scrapy
import json
from datetime import datetime

class crawlShopee(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['shopee.vn']
    idProduct = ['10753341705','9994458817','13017662822']
    idShop = ['88201679']
    offset =['0', '6', '12', '18', '24', '30', '36', '42', '48', '54', '60', '66', '72', '78', '84', '90', '96', '102',
             '108', '114', '120', '126', '132', '138', '144', '150', '156', '162', '168', '174', '180', '186','192']
    urls = []
    for i in idProduct:
        for k in offset:
            urls.append("https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=" + i
                        + "&limit=6&offset=" + k + "&shopid=88201679&type=0")
    start_urls = urls

    def parse(self, response):
            #print(response.body)
            resp = json.loads(response.body)
            data = resp.get('data')
            ratings = data.get('ratings')
            for rating in ratings:
                    yield {
                            'Username': rating.get('author_username'),
                            'Comment': rating.get('comment'),
                            'Rating': rating.get('rating_star'),
                            'Time': datetime.fromtimestamp(rating.get('ctime')).strftime('%Y-%m-%d %H:%M:%S'),
                            'IdProduct': rating.get('itemid')
                    }
            with open('outputTMDT.csv', 'a', encoding='utf8') as f:
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.write('\n')
                    print('SUCCESS:', response.url)

                        #print(response.body)
            #url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=4010229477&limit=6&offset=0&shopid=79711504&type=0'

            #url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=10753341705&limit=6&offset=0&shopid=88201679&type=0'
