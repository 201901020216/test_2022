# "添加数据"
import unittest
import requests


class Add(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/add"

    '''参数为空'''
    def test_add_params_null(self):
        r = requests.get(self.base_url, params={'name': ' ', 'age': ' '})
        self.result = r.json()
        self.assertEqual(self.result['code'], 10002)
        self.assertEqual(self.result['message'], '添加失败！')

    '''添加成功'''
    def test_add_success(self):
        r = requests.get(self.base_url, params={'name': '添加成功', 'age': 2022})
        self.result = r.json()
        self.assertEqual(self.result['code'], 200)
        self.assertEqual(self.result['message'], '添加成功！')

    def tearDown(self):
        pass
