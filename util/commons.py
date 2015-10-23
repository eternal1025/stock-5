#!/usr/local/bin/python
#coding=utf-8
# 定义的常量

import os

#DB_WAY:数据存储方式 'csv'  # or 'mysql' or 'redis' or 'sqlite'
DB_WAY = 'mysql'
DB_USER = 'root'
DB_PWD = 'root' # or '123456' in win7
DB_NAME = 'stock'
#TABLE_STOCKS_BASIC = 'stock_basic_list'
DownloadDir = os.path.pardir + '/stockdata/' # os.path.pardir: 上级目录

##################################
# Redis

#基本信息表
PRE_STOCK_BASIC = 'stock_basic_info:' #股票基本信息的前缀
KEY_CODE = 'code'
KEY_NAME = 'name'
KEY_INDUSTRY = 'industry'
KEY_AREA = 'area'
KEY_PE = 'pe' #市盈率
KEY_EPS = 'eps' #每股收益
KEY_PB = 'pb' #市净率
KEY_TimeToMarket = 'timeToMarket'

#历史K线数据
PRE_STOCK_KLINE = 'kline:'
PRE_STOCK_KLINE_Sqlite = 'kline_' # sqlite 不支持 ：，改成_
KEY_DATE = 'date'
KEY_OPEN = 'open'
KEY_HIGH = 'high'
KEY_CLOSE = 'close'
KEY_LOW = 'low'
KEY_VOLUME = 'volume'
KEY_AMOUNT = 'amount'

INDEX_STOCK_BASIC = 'index_basic_all' # 索引：获取所有股票
INDEX_STOCK_KLINE = 'index_kline:' # 索引：获取单只股票的所有日期的K线

##################################

