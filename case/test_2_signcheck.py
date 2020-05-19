import unittest
import requests
import json
import sys
import yaml
sys.path.append('../')
from conf import globalvar as gl
from log.loggers import UserLog

yml = open(r'.\conf\conf.yml',encoding='utf-8')
content = yaml.load(yml, Loader=yaml.FullLoader)

class TestSignCheck(unittest.TestCase):
    #@unittest.skip("不执行此用例")
    def test_signcheck(self):
        headers = content['header']
        headers['X-TOKEN'] = gl.get_value("X-TOKEN")
        gl.set_value("headers",headers)
        url = content['host']+'/portal/forward?service=/ecard/v1/sign/check'
        data = {"channelNo":content['channelNo'],"aab301":gl.get_value('aab301'),"aac002":content['aac002'],"aac003":content['aac003'],"aac067":content['aac067']}
        res = requests.post(url=url,data=json.dumps(data),headers=gl.get_value('headers'))
        print(data)
        print(res.text)
        self.assertIn('成功', res.text, msg='实卡认证失败')
        gl.set_value('signSeq',json.loads(res.text)['result']['signSeq'])
        userlog = UserLog()
        loger = userlog.get_log()
        loger.info(url)
        loger.info(data)
        loger.info(res.text)
        userlog.close_handle()


