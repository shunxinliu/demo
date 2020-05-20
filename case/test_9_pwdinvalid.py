import unittest
import yaml
import sys
sys.path.append('../')
from conf import globalvar as gl
import requests
import json
import traceback
from log.loggers import UserLog

yml = open(r'./conf/conf.yml',encoding='utf-8')
content = yaml.load(yml,Loader=yaml.FullLoader)



class TestPwdInvid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.userlog = UserLog()
        cls.loger = cls.userlog.get_log()
        cls.error = traceback.format_exc()

    @classmethod
    def tearDownClass(cls):
        cls.userlog.close_handle()

    def test_pwd_invid(self):
        url = content['host']+'/portal/forward?service=/ecard/v1/pwd/valid'
        data = {"channelNo":content['channelNo'],"signNo":gl.get_value('signNo'),"pwd":content['pwd']}
        try:
            res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
            print(json.dumps(data))
            print(res.text)
            # self.assertIn('成功', res.text, msg="选择密码解除关联失败")
            self.loger.info(url)
            self.loger.info(data)
            self.loger.info(res.text)
            gl.set_value('busiSeq',json.loads(res.text)['result']['busiSeq'])
        except:
            self.loger.error(self.error)
        finally:
            self.assertIn('成功', res.text, msg="选择密码解除关联失败")



    def test_sign_invid(self):
        url = content['host']+'/portal/forward?service=/ecard/v1/sign/invalid'
        data = {"channelNo":content['channelNo'],"signNo":gl.get_value('signNo'),"busiSeq":gl.get_value('busiSeq')}
        try:
            res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
            print(json.dumps(data))
            print(res.text)
            self.loger.info(url)
            self.loger.info(data)
            self.loger.info(res.text)
        except:
            self.loger.error(self.error)
        finally:
            self.assertIn('成功', res.text, msg='密码解除关联失败')