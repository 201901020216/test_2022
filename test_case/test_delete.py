# 删除数据
import unittest
import requests


class Delete(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/delete"

    """请求参数 值为空"""
    def test_delete_get_id_null(self):
        r = requests.get(self.base_url, params={'id': ' '})
        self.result = r.json()
        self.assertEqual(self.result['code'], 10003)
        self.assertEqual(self.result['message'], '删除失败！')

    """id值类型错误"""
    def test_delete_get_id_value_error(self):
        r = requests.get(self.base_url, params={'id': "哈哈"})
        self.result = r.json()
        self.assertEqual(self.result["code"], 10003)
        self.assertEqual(self.result["message"], "删除失败！")

    '''删除成功'''

    def test_delete_success(self):
        r = requests.get(self.base_url, params={'id': 30})
        self.result = r.json()
        self.assertEqual(self.result["code"], 200)
        self.assertEqual(self.result["message"], "删除成功！")

    def tearDown(self):
        pass
