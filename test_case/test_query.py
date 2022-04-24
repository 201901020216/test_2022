# 查询数据
import unittest
import requests


class Query(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/query"

    ''' id= 查询结果为空 '''
    def test_get_id_null(self):
        r = requests.get(self.base_url, params={'id': ''})
        self.result = r.json()
        self.assertEqual(self.result['code'], 10001)
        self.assertEqual(self.result['message'], '参数不能为空！')

    ''' id=901 id不存在 '''
    def test_get_id_error(self):
        r = requests.get(self.base_url, params={'id': 901})
        self.result = r.json()
        self.assertEqual(self.result['code'], 10005)
        self.assertEqual(self.result['message'], '查询失败！')

    """id值类型错误"""
    def test_get_id_value_error(self):
        r = requests.get(self.base_url, params={'id': "哈哈"})
        self.result = r.json()
        self.assertEqual(self.result["code"], 10005)
        self.assertEqual(self.result["message"], "查询失败！")

    ''' 根据 id 查询结果成功 '''
    def test_get_id_success(self):
        r = requests.get(self.base_url, params={'id': 1})
        self.result = r.json()
        self.assertEqual(self.result['code'], 200)
        self.assertEqual(self.result['message'], '查询成功！')

    def tearDown(self):
        pass
