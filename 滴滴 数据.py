# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:15:08 2016
@author: yiyuezhuo
"""

'''
cityId:510100
scope:city
date:3
dimension:satisfy
num:300
'''

import request
import json
import pandas as pd
import os

def get(cityId='510100',scope='city',date='3',dimension='satisfy',num=1000):
    url='http://v.kuaidadi.com/point'
    params={'cityId':cityId,'scope':scope,'date':date,'dimension':dimension,'num':num}
    res=requests.get(url,params=params)
    return json.loads(res.content.decode())
    
class Downloader(object):
    def __init__(self,cityId_list=None):
        self.cityId_list=cityId_list if cityId_list!=None else ['510100']
        self.scope_list=['city']
        self.date_list=[str(i) for i in range(7)]
        self.dimension_list=['distribute','satisfy','demand','response','money']
        # money好像get字段不太一样，不过暂且用一样的方法请求
        self.num_list=[1000]
        
        self.pkey=('cityId','scope','date','dimension','num')
        
        self.data={}
    def keys(self):
        for cityId in self.cityId_list:
            for scope in self.scope_list:
                for date in self.date_list:
                    for dimension in self.dimension_list:
                        for num in self.num_list:
                            yield (cityId,scope,date,dimension,num)
    def download(self,verbose=True):
        for key in self.keys():
            pkey=self.pkey
            params=dict(zip(pkey,key))
            self.data[key]=get(**params)
            if verbose:
                print('clear',key)
                
def to_csv(key,json_d,prefix='data/'):
    data=json_d['result']['data']
    city_id=json_d['result']['cityID']
    date=json_d['result']['date']
    dimension=key[3]
    fname='_'.join([dimension,date,city_id,'.csv'])
    fname=fname.replace('/','.')
    fname=prefix+fname
    cdata=[]
    for hour,section in enumerate(data):
        for record in section:
            cdata.append([hour]+record[1:])
    df=pd.DataFrame(cdata,columns=['hour','longitude','latitude','value'])
    df.to_csv(fname)
    
def to_csv_all(datas,path='data/'):
    for key,json_d in datas.items():
        to_csv(key,json_d,prefix=path)
        
def run(city,path='data'):
    if not os.path.isdir(path):
        print('create dir path',path)
        os.mkdir(path)
    downloader=Downloader([city])
    downloader.download()
    to_csv_all(downloader.data,path=path+'/')

        
def CLI():
    import argparse
    parser = argparse.ArgumentParser(usage=u'python main.py 510100',
                                     description=u"苍穹平台数据抓取器")
    parser.add_argument('city',help=u'城市序号，成都是510100,其他ID参见cityId.json文件')
    parser.add_argument('--dir',default='data',help=u'保存路径,默认为data')
    args=parser.parse_args()
    run(args.city,args.dir)

        
if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        CLI()

'''
downloader=Downloader()
downloader.download()
to_csv_all(downloader.data)
'''
