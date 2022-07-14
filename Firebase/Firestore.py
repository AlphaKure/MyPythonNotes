from typing import Dict
import flask  # 範例使用框架:flask

import firebase_admin as firebase
from firebase_admin import firestore  # 一定要這樣取

'''
本範例使用class的方法寫

非唯一使用方法
'''


class database:
    '''
    本class有以下成員變數:
    1.database: firestore客戶端
    '''
    __slots__ = ('database')

    def __init__(self) -> None:
        '''
        初始化
        '''
        cred = firebase.credentials.Certificate('/path/to/your/key.json')  # 讀取key
        firebase.initialize_app(cred)  # 驗證key

        self.database = firestore.client()

    def createData(self) -> None:
        '''
        新增範例
        假設從前端post兩筆資料，分別為data1、data2
        '''
        data1 = flask.request.values.get(data1) # 獲得data1
        data2 = flask.request.values.get(data2) # 獲得data2
        '''
        假設我希望在firestore中'test'collection中存入名為data1的doc，
        裡面放data:data2。
        '''
        data={
            'data':data2
        }
        self.database.collection('test').document(data1).set(data) # 存入data

    def deleteData(self) -> None:
        '''
        刪除範例
        假設從前端post一筆資料docName，把'test'collection中對應名稱的doc刪除
        '''
        docName = flask.request.values.get(docName) # 獲得docName
        self.database.collection('test').document(docName).delete() # 刪除該筆doc

    def updataData(self) -> None:
        '''
        修改範例
        假設我要把'test'collection中對應名稱的doc裡面的data刪除，並新增一個number資料
        !!! 假設你要刪除document中任一資料建議使用這種方法 !!!
        '''
        targetDocument=flask.request.values.get(targetDocument) # 獲得目標document
        number=flask.request.values.get(number) # 獲得number

        data:Dict=self.database.collection('test').document(targetDocument).get().to_dict() # 獲得原document裡的所有資料，並轉為dict格式

        data.pop('data') # 刪除document中的'data'
        data['number']=number #新增一項{'number':number}

        # print(data)

        self.database.collection('test').document(targetDocument).update(data) # 將data回傳更新
