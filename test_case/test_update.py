# 修改数据
import unittest

import requests


class Update(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/update"

    """请求参数 值为空"""

    def test_update_params_null(self):
        r = requests.get(self.base_url, params={"id": " ", "name": " ", "age": " "})
        self.result = r.json()
        self.assertEqual(self.result["code"], 10004)
        self.assertEqual(self.result["message"], "修改失败！")

    '''修改成功'''

    def test_add_success(self):
        r = requests.get(self.base_url, params={"id": 20, "name": "我想运行成功", "age": 22})
        self.result = r.json()
        self.assertEqual(self.result["code"], 200)
        self.assertEqual(self.result["message"], "修改成功！")

    def tearDown(self):
        pass
