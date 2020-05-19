import unittest
import os
import sys
sys.path.append('../')
from report.HTMLTestReportCN import HTMLTestRunner

# print(sys.path)
#from log.loggers import UserLog
from case.test_0_tokensign import TestSign
from case.test_1_signinfo import TestSignInfo

# suite = unittest.TestSuite()
# suite.addTests([TestSign('test_a_token_sign'),TestSign('test_gettoken')])
# suite.addTests([TestSignInfo('test_signinfo')])


# print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+os.getcwd())
class RunAll(unittest.TestCase):
    #run_case不要以test开头，否则多执行一次
    def run_case(self):
        # os.path.join   把目录和文件名合成一个路径
        #os.getcwd    返回当前工作目录
        case_path = os.getcwd()
        #case_path = os.path.join(os.getcwd(),'case')
        suite = unittest.TestSuite()
        # suite.addTests([TestSign('test_a_token_sign'),TestSign('test_gettoken')])
        # suite.addTests([TestSignInfo('test_signinfo')])
        suite = unittest.defaultTestLoader.discover(case_path,'test_*.py')
        f = open("./report/report.html", 'wb') # 二进制写格式打开要生成的报告文件
        HTMLTestRunner(stream=f,title="电子社保卡巡检",description="测试描述",tester='刘').run(suite)
        f.close()


if __name__ == '__main__':
    #unittest.main()
    run = RunAll()
    run.run_case()