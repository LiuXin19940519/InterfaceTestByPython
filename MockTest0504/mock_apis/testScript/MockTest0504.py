<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.11

import  unittest
import  requests

class MockTest(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:12306'

    def tearDown(self):
        pass

    def test_login(self,url='/login'):
        '''验证登录的接口'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.url+url,json=data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'],'liuxin')
        print('responseData:' + r.content)  #r.content读取response返回内容

    def getToken(self,url='/login'):   #getToken方法
        '''登录成功后获取token'''
        data = {
            "username": "admin",
            "password": "admin",
            "roleID": 22
        }
        r=requests.post(self.url+url,json=data)
        return r.json()['token']

    def test_parkingside(self,url='/parkinside'):
        '''验证查询停车时长的接口'''
        headers = {
            'Content-Type': 'application/json',
            'token': self.getToken()  #token参数传递
        }
        data = {
            "vpl":"AJ3585"
        }
        r = requests.post(self.url + url, headers=headers,json=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['Parking time long'], '20h18mins')
        self.assertEqual(r.json()['Parking fee'], u'$20')
        print('responseData:' + r.content)  #r.content读取response返回内容

    if __name__ == '__main__':
=======
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#python version 2.7.11

import  unittest
import  requests

class MockTest(unittest.TestCase):
    def setUp(self):
        self.url='http://localhost:12306'

    def tearDown(self):
        pass

    def test_login(self,url='/login'):
        '''验证登录的接口'''
        data={
            "username":"admin",
            "password":"admin",
            "roleID":22
        }
        r=requests.post(self.url+url,json=data)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'],'liuxin')
        print('responseData:' + r.content)  #r.content读取response返回内容

    def getToken(self,url='/login'):   #getToken方法
        '''登录成功后获取token'''
        data = {
            "username": "admin",
            "password": "admin",
            "roleID": 22
        }
        r=requests.post(self.url+url,json=data)
        return r.json()['token']

    def test_parkingside(self,url='/parkinside'):
        '''验证查询停车时长的接口'''
        headers = {
            'Content-Type': 'application/json',
            'token': self.getToken()  #token参数传递
        }
        data = {
            "vpl":"AJ3585"
        }
        r = requests.post(self.url + url, headers=headers,json=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json()['Parking time long'], '20h18mins')
        self.assertEqual(r.json()['Parking fee'], u'$20')
        print('responseData:' + r.content)  #r.content读取response返回内容

    if __name__ == '__main__':
>>>>>>> 同步本地文件2020/10/16 14:17
        unittest.main(verbosity=2)