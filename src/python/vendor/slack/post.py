# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

if __name__ == '__main__':

    slack = Slacker(slackbot_settings.API_TOKEN)
    attachment = {
        'author_name': 'PASORI',
        'image_url': 'https://qiita-image-store.s3.amazonaws.com/0/79598/ca17f1ac-fc73-0877-86a9-40f794155337.jpeg',
        'color': '#6A8CC7'
    }
 
    slack.chat.post_message(
        slackbot_settings.CHANNEL,
        'masatoshi.atsumi さんが出社しました',
        as_user=True,
        attachments=[attachment]
    )