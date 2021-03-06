__author__ = 'TianluWang'

import datetime

default_port = 8000
mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': '123',
         'db': 'TORNADO',
         'port': 3306,
         'connect_timeout': 3,
         'table_name': 'userinfo_tbl'}
secret = 'password'
algorithm = 'HS256'
token_timedelta = datetime.timedelta(days=1)
reset_timedelta = datetime.timedelta(hours=1)
errors = {'other error': 100,
          'incorrect password': 101,
          'user not exists': 102,
          'user already exists': 103,
          'timeout': 104,
          'illegal email address': 105,
          'illegal user': 106,
          'incorrect account': 107,
          'input cannot be null': 108,
          'success': 0}