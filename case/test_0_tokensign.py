import json
import unittest

import requests
import yaml

from conf import globalvar as gl

yml = open(r'.\..\conf\conf.yml',encoding='utf-8')

#y = yaml.load(yml)
content = yaml.load(yml, Loader=yaml.FullLoader)
#print (type(y))
#print(content)
#print(y['host'])
#print(y['channelNo'])

class TestSign(unittest.TestCase):
    gl._init()

    #验签
    def test_a_token_sign(self):
        url = content['host']+'/portal/token/sign'
        data = {"aac002": " ", "aac003": "", "accessKey": content['accessKey'],
                "channelNo": content['channelNo']}
        res = requests.post(url,data=json.dumps(data),headers=content['header'])
        print(json.loads(res.text)['result'])
        #gl.set_value("result",json.loads(res.text)['result'])
        globals()["result"] = json.loads(res.text)['result']


    #获取token
    def test_gettoken(self):
        url = content['host']+'/api/token'
        params = globals()["result"]
        res = requests.get(url,params=params)
        print(type(res.text))
        gl.set_value("X-TOKEN",(json.loads(res.text)['result']['token']))
        print("sss"+gl.get_value('X-TOKEN'))


# if __name__ == '__main__':
#     unittest.main()
