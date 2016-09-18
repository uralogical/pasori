#!/usr/bin/env python
# coding: utf-8

import MySQLdb

def main():
    conn = MySQLdb.connect(
        user='root',
        passwd='pass',
        host='127.0.0.1',
        db='pasori'
    )
    c = conn.cursor()

    sql = 'select systems table '

    tables = [ 
        ['systems', '(id int, SYS varchar(32))'],
        ['products', '(id int, PMm varchar(32))'],
        ['users', '(id int, name varchar(32), IDm varchar(32))']
    ]

    for table in tables:
      sql =  "SHOW TABLES LIKE '" + str(table[0]) + "';"
      is_exist = c.execute("SHOW TABLES LIKE %s", (str(table[0])))
      if is_exist:
        print('Already Inserted...\n')
        continue
      # テーブルの作成
      sql = 'create table ' + str(table[0]) + ' ' + str(table[1])
      c.execute(sql)
      print('Created ' + str(table[0]) + ' table.\n')

    # # テーブル一覧の取得
    # sql = 'show tables'
    # print c.execute(sql)
    # print('===== テーブル一覧 =====')
    # print(c.fetchone())

    # # レコードの登録
    # sql = 'insert into test values (%s, %s)'
    # c.execute(sql, (1, 'hoge'))  # 1件のみ
    # datas = [
    #     (2, 'foo'),
    #     (3, 'bar')
    # ]
    # c.executemany(sql, datas)    # 複数件
    # print('\n* レコードを3件登録\n')

    # # レコードの取得
    # sql = 'select * from test'
    # c.execute(sql)
    # print('===== レコード =====')
    # for row in c.fetchall():
    #     print('Id:', row[0], 'Content:', row[1])

    # # レコードの削除
    # sql = 'delete from test where id=%s'
    # c.execute(sql, (2,))
    # print('\n* idが2のレコードを削除\n')

    # # レコードの取得
    # sql = 'select * from test'
    # c.execute(sql)
    # print('===== レコード =====')
    # for row in c.fetchall():
    #     print('Id:', row[0], 'Content:', row[1])

    # データベースへの変更を保存
    conn.commit()

    c.close()
    conn.close()


if __name__ == '__main__':
    main()