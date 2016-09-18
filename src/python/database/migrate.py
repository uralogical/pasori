#!/usr/bin/env python
# coding: utf-8

import MySQLdb
from datetime import datetime

def main():
  conn = MySQLdb.connect(
      user='root',
      passwd='pass',
      host='127.0.0.1',
      db='pasori'
  )
  c = conn.cursor()

  now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

  tables = [ 
      # ['systems', '(id int, SYS varchar(32))'],
      # ['products', '(id int, PMm varchar(32))'],
      ['books', '(id int(11) AUTO_INCREMENT, name varchar(32), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP NOT NULL, index(id))'],
      ['organizations','(id int(11) AUTO_INCREMENT, name varchar(32), sysid varchar(32), pmmid varchar(32), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP NOT NULL, index(id))'],
      ['users', '(id int(11) AUTO_INCREMENT, name varchar(32), IDm varchar(32), created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP NOT NULL, index(id))'],
  ]

  # Delete Tables
  for table in tables:
    c.execute("DROP TABLE IF EXISTS " + (str(table[0])))

  # Create Tables
  for table in tables:
    create = 'create table ' + str(table[0]) + ' ' + str(table[1])
    c.execute(create)
    print('Created ' + str(table[0]) + ' table.')

  # Register Records
  insert_orgs = 'insert into organizations values (%s, %s, %s, %s, %s, %s)'
  c.execute(insert_orgs, (None, 'SeattleConsulting', 8725, '0120220427674eff', None, None))
  print('Inserted Organizations...\n')

  insert_users = 'insert into users values (%s, %s, %s, %s, %s)'
  datas = [
    (None, 'masatoshi.atsumi', '01100d0053135d01', None, None),
    (None, 'masayuki.tooyama', '0110070053136101', None, None),
  ]
  c.executemany(insert_users, datas)
  print('Inserted Organizations...\n')

  conn.commit()

  c.close()
  conn.close()

if __name__ == '__main__':
  main()
  print 'Migration done!'