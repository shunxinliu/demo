import unittest
import sys
import yaml
import requests
import json
from log.loggers import UserLog
sys.path.append('../')
from conf import globalvar as gl

yml = open(r'./conf/conf.yml',encoding='utf-8')
content = yaml.load(yml,Loader=yaml.FullLoader)


class TestSetPwd(unittest.TestCase):
    def test_setpwd(self):
        url = content['host']+'/portal/forward?service=/ecard/v1/pwd/set'
        data = {"channelNo":content['channelNo'],"aab301":gl.get_value('aab301'),"aac002":content['aac002'],"aac003":content['aac003'],"signSeq":gl.get_value('signSeq'),"pwd":content['pwd']}
        res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
        print(data)
        self.assertIn("成功", res.text, msg="密码设置失败")
        userlog = UserLog()
        loger = userlog.get_log()
        loger.info(url)
        loger.info(data)
        loger.info(res.text)
        userlog.close_handle()
