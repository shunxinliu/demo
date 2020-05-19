import json
import unittest

import requests
import yaml
import sys
sys.path.append('../')

from conf import globalvar as gl
from log.loggers import UserLog

yml = open(r'.\conf\conf.yml',encoding='utf-8')

#y = yaml.load(yml)
content = yaml.load(yml, Loader=yaml.FullLoader)
#print (type(y))
#print(content)
#print(y['host'])
#print(y['channelNo'])

class TestSign(unittest.TestCase):
    gl._init()
    @classmethod
    def setUpClass(cls):
        cls.userlog = UserLog()
        cls.loger = cls.userlog.get_log()

    @classmethod
    def tearDownClass(cls):
        cls.userlog.close_handle()

    #验签
    def test_a_token_sign(self):
        # userlog = UserLog()
        # loger = userlog.get_log()
        url = content['host']+'/portal/token/sign'
        data = {"aac002": " ", "aac003": "", "accessKey": content['accessKey'],
                "channelNo": content['channelNo']}
        res = requests.post(url,data=json.dumps(data),headers=content['header'])
        print(json.loads(res.text))
        print(json.loads(res.text)['result'])
        #gl.set_value("result",json.loads(res.text)['result'])
        self.assertIn('成功', res.text, msg='验签失败')
        globals()["result"] = json.loads(res.text)['result']
        self.loger.info(url)
        self.loger.info(data)
        self.loger.info(res.text)


    #获取token
    def test_gettoken(self):
        url = content['host']+'/api/token'
        params = globals()["result"]
        res = requests.get(url,params=params)
        print(type(res.text))
        gl.set_value("X-TOKEN",(json.loads(res.text)['result']['token']))
        print("sss"+gl.get_value('X-TOKEN'))
        self.assertIn('成功', res.text, msg='获取token失败')
        self.loger.info(url)
        self.loger.info(params)
        self.loger.info(res.text)


# if __name__ == '__main__':
#     unittest.main()
