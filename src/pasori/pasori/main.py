# -*- coding: utf-8 -*-
import binascii
import nfc
from slacker import Slacker
from slack import slackbot_settings
import MySQLdb

class MyCardReader(object):

  def on_connect(self, tag):
    print "touched"
    self.idm = binascii.hexlify(tag.idm)
    self.pmm = binascii.hexlify(tag.pmm)
    self.sys = binascii.hexlify(tag.sys)

    self.create(self.idm)
    return True

  def create(self, idm):
    conn = MySQLdb.connect(
      user='root',
      passwd='pass',
      host='127.0.0.1',
      db='pasori'
    )
    c = conn.cursor()

    fetch = "select * from users where iDm like '%s'" % str(idm)
    c.execute(fetch)
    record = c.fetchone()
    self.user = record[1]
    print record

    sql = 'insert into books values (%s, %s, %s, %s)'
    c.execute(sql, (None, 'atsumi', None, None))
    conn.commit()
    c.close()
    conn.close()

    self.post()

  def read_id(self):
    clf = nfc.ContactlessFrontend('usb')
    try:
      clf.connect(rdwr={'on-connect': self.on_connect})
    finally:
      clf.close()

  def post(self):
    slack = Slacker(slackbot_settings.API_TOKEN)
    attachment = {
      'author_name': 'PASORI',
      'image_url': 'https://qiita-image-store.s3.amazonaws.com/0/79598/ca17f1ac-fc73-0877-86a9-40f794155337.jpeg',
      'color': '#6A8CC7'
    }

    slack.chat.post_message(
      slackbot_settings.CHANNEL,
      '%s さんが出社しました！' % self.user,
      as_user=True,
      attachments=[attachment]
    )

if __name__ == '__main__':
  cr = MyCardReader()
  while True:
    print "touch card:"
    cr.read_id()
    print "released"