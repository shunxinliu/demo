import json
import unittest
import traceback
import requests
import yaml
import sys
sys.path.append('../')
import copy
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
        cls.error = traceback.format_exc()

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
        scontent = copy.deepcopy(content['header'])
        scontent['Content-Type'] = "application/json;charset=UTF-8"
        try:
            res = requests.post(url,data=json.dumps(data),headers=scontent)
            print(json.loads(res.text))
            print(json.loads(res.text)['result'])
            #gl.set_value("result",json.loads(res.text)['result'])
            globals()["result"] = json.loads(res.text)['result']
            self.loger.info(url)
            self.loger.info(data)
            self.loger.info(res.text)
        except:
            self.loger.error(self.error)
        finally:
            self.assertIn('成功', res.text, msg='验签失败')

    #获取token
    def test_gettoken(self):
        url = content['host']+'/api/token'
        params = globals()["result"]
        try:
            res = requests.get(url,params=params,headers=content['header'])
            print(type(res.text))
            gl.set_value("X-TOKEN",(json.loads(res.text)['result']['token']))
            print("sss"+gl.get_value('X-TOKEN'))
            self.loger.info(url)
            self.loger.info(params)
            self.loger.info(res.text)
        except:
            self.loger.error(self.error)
            self.loger.info(content['header'])
        finally:
            print(type(res.text))
            self.assertIn('成功', res.text, msg='获取token失败')


# if __name__ == '__main__':
#     unittest.main()
