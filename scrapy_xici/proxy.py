import urllib
from urllib import request
import traceback
import pymongo
class GetIp():
    def __init__(self):
        MONGO_URL = 'localhost'
        MONGO_DB = 'xici'
        MONGO_TABLE = 'xici_get_ip'
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        self.result = db[MONGO_TABLE].find({'IP': {'$exists': True}})
    def del_ip(self,record):
        MONGO_URL = 'localhost'
        MONGO_DB = 'xici'
        MONGO_TABLE = 'xici_get_ip'
        client = pymongo.MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        db[MONGO_TABLE].delete_one(record)
    def judge_ip(self,record):
        http_url = 'http://www.kugou.com/'
        https_url = 'https://www.baidu.com/'
        proxy_type = record['属性'].lower()
        url = http_url if proxy_type == 'http' else https_url
        proxy = '%s:%s'%(record['IP'],record['端口'])
        print(proxy)
        try:
            req = urllib.request.Request(url=url)
            req.set_proxy(proxy,proxy_type)
            response = urllib.request.urlopen(req,timeout=10)
        except Exception:
            # traceback.print_exc()
            print('无效的proxy', record)
            self.del_ip(record)
            return False
        else:
            code = response.getcode()
            if code>=200 and code<300:
                print('有效的proxy',record)
                return True
            else:
                print('无效的proxy',record)
                return False
    def get_ips(self):
        http = []
        https = []
        for h in self.result:
            if h['属性'] == 'HTTP' and self.judge_ip(h):
                http.append(h['IP'] + ':' + h['端口'])
            elif h['属性'] == 'HTTPS' and self.judge_ip(h):
                https.append(h['IP'] + ':' + h['端口'])
        print('HTTP:',len(http),"HTTPS:",len(https))
        return {'http':http,'https':https}

