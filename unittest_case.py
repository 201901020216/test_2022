import os

import unittest


from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from gevent import time

from test_case.test_add import Add
from test_case.test_delete import Delete
from test_case.test_query import Query
from test_case.test_update import Update

if __name__ == '__main__':
    # unittest.main()
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Add)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Delete)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Update)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Query)
    suite = unittest.TestSuite([suite1])
    # 获取当前文件所在的路径
    base_dir = os.path.dirname(os.path.realpath(__file__))
    print(base_dir)
    dir_path = base_dir + "\\..\\201901020216_陈彬彬_1\\report\\"
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    report_path = dir_path + now + "result.html"
    with open(report_path,'wb')as f:
        runner = HTMLTestRunner(stream=f,verbosity=2,title="unittest报告",description="html测试")
        runner.run(suite)