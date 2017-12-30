# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import errno
import os
import sys
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    ImageSendMessage
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
# channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
# if channel_secret is None:
#     print('Specify LINE_CHANNEL_SECRET as environment variable.')
#     sys.exit(1)
# if channel_access_token is None:
#     print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
#     sys.exit(1)

line_bot_api = LineBotApi('yCLqDYJLIiRo5xSfnc/9tmKbtKL9oEcBhzG8Mczc0WH+8B+/Q9PT0ifkMT+frqRsgAKYqB1/CVhwx7vWPLKP1nyZszn6gGdqQ0H1CgfLUxFhX2Wgreq3cFZw1D1km/IXBljdJyY4fOw5kyvSQpcu6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('62826fb39d7f3cb6a27f8573bc5e9b29')

#SEGALA INISIALISASI ADA DI SINI HEHEHE

#INISIALISASI USER ID
user_id_admin = 'U36bb6303be7a1563a7d27d0ee2234ea5' #faldi
user_id_tandu_1 ='U36bb6303be7a1563a7d27d0ee2234ea5' #ilham
user_id_tandu_2 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #sarah
user_id_obat_1 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #kahfi
user_id_obat_2 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #rani
user_id_tft_1 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #ivansa
user_id_tft_2 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #fathin ?????
user_id_humas_1 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #atsila
user_id_humas_2 = 'U36bb6303be7a1563a7d27d0ee2234ea5' #benito ?????

#INISIALISASI NAMA
nama_admin = 'faldi'
nama_tandu_1 = 'faldi'
nama_tandu_2 = 'faldi'
nama_obat_1 = 'faldi'
nama_obat_2 = 'faldi'
nama_tft_1 = 'faldi'
nama_tft_2 = 'faldi'
nama_humas_1 = 'faldi'
nama_humas_2 = 'faldi'

#RESOURCE - IMAGE
imgurl_tandu = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/tandu/tandu.jpg'
imgurl_obat = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/obat/obat.jpg'
imgurl_obat_base = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/obat/obat_base.jpg'
imgurl_obat_pj = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/obat/obat_pj.jpg'
imgurl_obat_satuan = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/obat/obat_pilih.jpg'
imgurl_tft = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/tft/tft.jpg'
imgurl_humas = 'https://raw.githubusercontent.com/rrifaldiu/line-bot-medik/master/static/res/jpg/humas/humas.jpg'

form_template = ('\n' +
                'Nama : \n' +
                'Jurusan : \n' +
                'ID Line : \n' +
                'Lembaga : \n' +
                'Tujuan peminjaman : \n' +
                'Tanggal peminjaman : \n' +
                'Tanggal pengembalian : ')

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text == 'menu':
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url=imgurl_tandu,
                                action=PostbackTemplateAction(
                                            label='Pinjam Tandu',
                                            data='tandu')),
            ImageCarouselColumn(image_url=imgurl_obat,
                                action=PostbackTemplateAction(
                                            label='Pinjam Obat',
                                            data='obat')),
            ImageCarouselColumn(image_url=imgurl_tft,
                                action=PostbackTemplateAction(
                                            label='TFT Medik',
                                            data='tft')),
            ImageCarouselColumn(image_url=imgurl_humas,
                                action=PostbackTemplateAction(
                                            label='Hubungi Kami',
                                            data='form_humas'))
        ])
        template_message = TemplateSendMessage(
            alt_text='Silahkan pilih menu yang diinginkan', template=image_carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                StickerSendMessage(
                    package_id='3',
                    sticker_id='242'
                ),
                TextSendMessage(text='Halo! Selamat datang di OA Medik OSKM!\n\n Silahkan pilih menu di bawah ini'),
                template_message
            ]
        )


    elif text.startswith('balas-'):
        profile = line_bot_api.get_profile(event.source.user_id)
        if text.startswith('balas-' + nama_admin):
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_admin)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_tandu_1):
            line_bot_api.push_message(user_id_tandu_1, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tandu_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_tandu_1.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tandu_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_tandu_2):
            line_bot_api.push_message(user_id_tandu_2, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tandu_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_tandu_2.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tandu_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_obat_1):
            line_bot_api.push_message(user_id_obat_1, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_obat_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_obat_1.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_obat_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_obat_2):
            line_bot_api.push_message(user_id_obat_2, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_obat_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_obat_2.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_obat_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_tft_1):
            line_bot_api.push_message(user_id_tft_1, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tft_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_tft_1.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tft_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_tft_2):
            line_bot_api.push_message(user_id_tft_2, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tft_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_tft_2.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_tft_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_humas_1):
            line_bot_api.push_message(user_id_humas_1, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_humas_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_humas_1.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_humas_1)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif text.startswith('balas-' + nama_humas_2):
            line_bot_api.push_message(user_id_humas_2, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text='Menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_humas_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.push_message(user_id_admin, [ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
                ),
                TextSendMessage(text=nama_humas_2.title() + 'menerima balasan dari ' + profil.display_name + ':\n' + text[(6+len(nama_humas_2)) : ]),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
                TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        else:
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Nama admin tidak ditemukan\nPastikan nama admin tidak dituliskan dengan kapital')
            )






    elif text.startswith('balas_admin-'):
        user_id_balas = text[(text.find('-') + 1) : (text.find(':') - 1)]
        balasan = text[(text.find(':')+2) : ]
        profile = line_bot_api.get_profile(event.source.user_id)
        if (event.source.user_id == user_id_admin):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_admin.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_admin +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_tandu_1):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tandu_1.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_tandu_1 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_tandu_1 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tandu_1.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_tandu_2):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tandu_2.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_tandu_2 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_tandu_2 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tandu_2.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_obat_1):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_obat_1.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_obat_1 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_obat_1 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_obat_1.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_obat_2):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_obat_2.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_obat_2 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_obat_2 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_obat_2.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_tft_1):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tft_1.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_tft_1 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_tft_1 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tft_1.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_tft_2):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tft_2.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_tft_2 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_tft_2 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_tft_2.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_humas_1):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_humas_1.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_humas_1 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_humas_1 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_humas_1.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        elif (event.source.user_id == user_id_humas_2):
            line_bot_api.push_message(user_id_balas, [
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_humas_2.title()),
                TextSendMessage(text='Untuk membalas pesan di atas, silahkan ketik \u0027balas-' + nama_humas_2 +'\u0027 diikuti dengan pesan Anda'),
            ])
            line_bot_api.push_message(user_id_admin, [
                TextSendMessage(text=nama_humas_2 + ' membalas untuk ' + profile.display_name + ' (User ID = ' + profile.user_id + ')'),
                TextSendMessage(text=balasan + '\n\nSalam, ' + nama_humas_2.title())
            ])
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Pesan telah terkirim')
            )
        else:
            line_bot_api.reply_message(
                event.reply_token, 
                TextSendMessage(text='Anda bukan admin')
            )




    elif text.startswith('[Form Peminjaman Tandu]'):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.push_message(user_id_tandu_1, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.push_message(user_id_tandu_2, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.push_message(user_id_admin, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.reply_message(
                event.reply_token, TextSendMessage(
                    text='Form telah dikirimkan\n\nKami akan memproses secepatnya. Harap bersabar dan menunggu'
                )
        )
    elif text.startswith('[Form Peminjaman Obat '):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.push_message(user_id_obat_1, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.push_message(user_id_obat_2, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.push_message(user_id_admin, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.reply_message(
                event.reply_token, TextSendMessage(
                    text='Form telah dikirimkan\n\nKami akan memproses secepatnya. Harap bersabar dan menunggu'
                )
        )
    elif text.startswith('[Form TFT Medik]'):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.push_message(user_id_tft_1, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        # line_bot_api.push_message(user_id_tft_2, [
        #     ImageSendMessage(
        #         original_content_url=profile.picture_url, preview_image_url=profile.picture_url
        #     ),
        #     TextSendMessage(
        #         text=text + '\nDisplay Name: ' + profile.display_name
        #     ),
        #     TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
        #     TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        # ])
        line_bot_api.push_message(user_id_admin, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.reply_message(
                event.reply_token, TextSendMessage(
                    text='Form telah dikirimkan\n\nKami akan memproses secepatnya. Harap bersabar dan menunggu'
                )
        )
    elif text.startswith('[Form Kontak]'):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.push_message(user_id_humas_1, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        # line_bot_api.push_message(user_id_humas_2, [
        #     ImageSendMessage(
        #         original_content_url=profile.picture_url, preview_image_url=profile.picture_url
        #     ),
        #     TextSendMessage(
        #         text=text + '\nDisplay Name: ' + profile.display_name
        #     ),
        #     TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
        #     TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        # ])
        line_bot_api.push_message(user_id_admin, [
            ImageSendMessage(
                original_content_url=profile.picture_url, preview_image_url=profile.picture_url
            ),
            TextSendMessage(
                text=text + '\nDisplay Name: ' + profile.display_name
            ),
            TextSendMessage(text='Untuk membalas pesan di atas, silahkan gunakan format di bawah:'),
            TextSendMessage(text='balas_admin-' + profile.user_id + ':\n<pesan Anda>')
        ])
        line_bot_api.reply_message(
                event.reply_token, TextSendMessage(
                    text='Form telah dikirimkan\n\nKami akan memproses secepatnya. Harap bersabar dan menunggu'
                )
        )


    elif text == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(
                        text='Display name: ' + profile.display_name
                    ),
                    TextSendMessage(
                        text='Status message: ' + profile.status_message
                    ),
                    TextSendMessage(
                        text='User ID: ' + event.source.user_id
                    )
                ]
            )
            line_bot_api.push_message(event.source.user_id, TextSendMessage(text='Hello World!'))
            line_bot_api.push_message(user_id_admin, TextSendMessage(text='Hello World!!'))
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="Bot can't use profile API without user ID"))
    
    elif text == 'imgwithurl':
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=imgurl_tft, preview_image_url='https://via.placeholder.com/240x240'
            )
        )

    # elif text == 'menu':

    elif text == 'bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="Bot can't leave from 1:1 chat"))
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Do it?', actions=[
            MessageTemplateAction(label='Yes', text='Yes!'),
            MessageTemplateAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URITemplateAction(
                    label='Go to line.me', uri='https://line.me'),
                PostbackTemplateAction(label='ping', data='ping'),
                PostbackTemplateAction(
                    label='ping with text', data='ping',
                    text='ping'),
                MessageTemplateAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'carousel':
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='hoge1', title='fuga1', actions=[
                URITemplateAction(
                    label='Go to line.me', uri='https://line.me'),
                PostbackTemplateAction(label='ping', data='ping')
            ]),
            CarouselColumn(text='hoge2', title='fuga2', actions=[
                PostbackTemplateAction(
                    label='ping with text', data='ping',
                    text='ping'),
                MessageTemplateAction(label='Translate Rice', text='米')
            ]),
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'image_carousel':
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url=imgurl_tandu,
                                action=DatetimePickerTemplateAction(label='datetime',
                                                                    data='datetime_postback',
                                                                    mode='datetime')),
            ImageCarouselColumn(image_url=imgurl_obat,
                                action=DatetimePickerTemplateAction(label='date',
                                                                    data='date_postback',
                                                                    mode='date')),
            ImageCarouselColumn(image_url=imgurl_tft,
                                action=DatetimePickerTemplateAction(label='date',
                                                                    data='date_postback',
                                                                    mode='date')),
            ImageCarouselColumn(image_url=imgurl_humas,
                                action=PostbackTemplateAction(
                                    label='pingwithtext',
                                    #text='ping',
                                    data='ping'
                                )
                            )
        ])
        template_message = TemplateSendMessage(
            alt_text='ImageCarousel alt text', template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, [template_message, TextSendMessage(text='Halo! Selamat datang di OA Medik OSKM! Silahkan pilih menu di bawah ini \uDBC0'),
                ])
    elif text == 'imagemap':
        pass
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title=event.message.title, address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


# Other Message Type
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save content.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix='file-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '-' + event.message.file_name
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save file.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Got follow event'))


@handler.add(UnfollowEvent)
def handle_unfollow():
    app.logger.info("Got Unfollow event")


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))


@handler.add(LeaveEvent)
def handle_leave():
    app.logger.info("Got leave event")

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'tandu':
        buttons_template = ButtonsTemplate(
            title='Pastikan Anda telah memahami SOP di atas', text='Klik tombol di bawah untuk melanjutkan', actions= [
                PostbackTemplateAction(
                    label='Oke', data='form_tandu')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Pahamilah SOP', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[SOP Peminjaman Tandu]\n' +
                                                    '\n' +
                                                    '1. Peminjaman dilakukan dengan terlebih dahulu menghubungi OA line Medik 2017 lalu mengikuti format yang telah disediakan.\n' +
                                                    '\n' +
                                                    '2. Peminjam lalu akan dihubungi untuk konfirmasi peminjaman jika peminjaman dapat dilakukan.\n' +
                                                    '\n' +
                                                    '3. Peminjam dan perwakilan dari medik kemudian akan bertemu untuk pengambilan tandu.\n' +
                                                    'Untuk pengembalian, peminjam dan perwakilan medik akan bertemu kembali untuk penyerahan tandu.\n' +
                                                    '\n' +
                                                    '4. Setiap tandu dapat dipinjam oleh massa kampus selama tandu masih tersedia.\n' +
                                                    '\n' +
                                                    '5. Untuk peminjaman, peminjam diminta untuk menitipkan KTM sebagai jaminan.\n' +
                                                    '\n' +
                                                    '6. Peminjaman tandu gratis, tidak dipungut biaya.\n' +
                                                    '\n' +
                                                    '7. Peminjam wajib melakukan penggantian apabila tandu hilang, atau terjadi kerusakan pada tandu yang bukan diakibatkan oleh penggunaan.\n' +
                                                    '\n' +
                                                    '8. Peminjam diminta untuk mencuci mitela yang terdapat pada tandu apabila kotor setelah penggunaan.\n' +
                                                    '\n' +
                                                    '9. Selama durasi peminjaman, peminjam melakukan sendiri pengencangan dan perawatan terhadap tandu. Saat peminjaman, peminjam dapat mengutus perwakilan untuk diberi pengarahan tentang cara pengencangan dan perawatan tandu.'
                                                ),
                                template_message
                                ])
    elif event.postback.data == 'obat':
        buttons_template = ButtonsTemplate(
            title='Pastikan Anda telah memahami SOP di atas', text='Klik tombol di bawah untuk melanjutkan', actions= [
                PostbackTemplateAction(
                    label='Oke', data='pilih_obat')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Pahamilah SOP', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[SOP Peminjaman Obat]\n' +
                                                    '\n' +
                                                    '1. Menghubungi OA Medik OSKM 2017 maksimal 3 hari sebelum peminjaman.\n' +
                                                    '\n' +
                                                    '2. Memperkenalkan diri serta menyampaikan tujuan peminjaman obat.\n' +
                                                    '\n' +
                                                    '3. Menyebutkan obat apa saja yang akan dipinjam.\n' +
                                                    '\n' +
                                                    '4. Peminjam menentukan lama waktu peminjaman obat. Peminjaman obat maksimal 14 hari dan jika terjadi keterlambatan dalam pengembalian obat, peminjam akan dikenakan sanksi yang akan diberitahukan lebih lanjut.(jika peminjam ingin meminjam lebih dari 14 hari dapat memperpanjang dengan menghubungi ke OA Medik)\n' +
                                                    '\n' +
                                                    '5. Peminjam memberikan jaminan peminjaman berupa KTM/KTP.\n' +
                                                    '\n' +
                                                    '6. Peminjam diwajibkan untuk menuliskan data penggunaan obat dengan format yang sudah ditentukan oleh Medik.\n' +
                                                    '\n' +
                                                    '7. Pengembalian obat dilakukan dengan menghubungi OA Medik sesuai dengan waktu yang telah ditentukan diawal peminjaman.\n' +
                                                    '\n' +
                                                    '8. Apabila obat yang dikembalikan rusak ataupun hilang, peminjam diharuskan mengganti obat tersebut'
                                                ),
                                TextSendMessage(text='9. Apabila obat yang dikembalikan habis dikarenakan pemakaian, kemasan obat tersebut tetap harus disertakan saat pengembalian obat. Apabila kemasan hilang, peminjam dianggap menghilangkan obat.'),                                            
                                template_message
                                ])
    elif event.postback.data == 'pilih_obat':
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(title='Obat Base', text='Obat yang digunakan di Base saat OSKM',
            thumbnail_image_url=imgurl_obat_base, actions=[
                PostbackTemplateAction(label='List Obat', data='list_obat_base'),
                PostbackTemplateAction(label='Pinjam', data='form_obat_base')
            ]),
            CarouselColumn(title='Obat PJ Obat', text='Obat yang dibawa oleh PJ Obat saat OSKM',
            thumbnail_image_url=imgurl_obat_pj, actions=[
                PostbackTemplateAction(label='List Obat', data='list_obat_pj'),
                PostbackTemplateAction(label='Pinjam', data='form_obat_pj')
            ]),
            CarouselColumn(title='Obat Satuan', text='Pilih obat-obatan tertentu yang Anda butuhkan',
            thumbnail_image_url=imgurl_obat_satuan, actions=[
                PostbackTemplateAction(label='List Obat', data='list_obat_satuan'),
                PostbackTemplateAction(label='Pinjam', data='form_obat_satuan')
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='Silahkan pilih jenis obat yang ingin Anda pinjam\n'),
                template_message
            ]
        )
    elif event.postback.data == 'list_obat_base':
        buttons_template = ButtonsTemplate(
            text='Kembali ke pemilihan obat', actions= [
                PostbackTemplateAction(
                    label='Kembali', data='pilih_obat')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Kembali ke pemilihan obat', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[List Obat Base]\n' +
                                                    '\n' +
                                                    '1. Bioplacenton\n' +
                                                    '2. Thrombophob\n' +
                                                    '3. Counterpain Patch Hot\n' +
                                                    '4. Counterpain Cool\n' +
                                                    '5. Ethyl Chloride\n' +
                                                    '6. Rivanol\n' +
                                                    '7. Oxycan\n' +
                                                    '8. Imboost\n' +
                                                    '9. Sangobion\n' +
                                                    '10. Mylanta Cair\n' +
                                                    '11. Ranitidin Cair\n' +
                                                    '12. Fludane\n' +
                                                    '13. Spasminal\n' +
                                                    '14. Parasetamol\n' +
                                                    '15. Feminax\n' +
                                                    '16. Ibuprofen\n' +
                                                    '17. Oralit\n' +
                                                    '18. Sanadryl\n' +
                                                    '19. Komix\n' +
                                                    '20. Salbutamol Syrup\n' +
                                                    '\n' +
                                                    'Perlu diingat bahwa obat-obat tersebut mungkin tidak tersedia karena habis atau sedang dipinjam. Info lebih lanjut akan dihubungi setelah pengisian form peminjaman.'
                                                ),
                                template_message
                                ])
    elif event.postback.data == 'list_obat_pj':
        buttons_template = ButtonsTemplate(
            text='Kembali ke pemilihan obat', actions= [
                PostbackTemplateAction(
                    label='Kembali', data='pilih_obat')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Kembali ke pemilihan obat', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[List Obat PJ Obat]\n' +
                                                    '\n' +
                                                    '1. Bioplacenton\n' +
                                                    '2. Thrombophob\n' +
                                                    '3. Counterpain\n' +
                                                    '4. Ethyl Chloride\n' +
                                                    '5. Rivanol\n' +
                                                    '6. Oxycan\n' +
                                                    '7. Sangobion\n' +
                                                    '8. Mylanta Cair\n' +
                                                    '9. Ranitidin Cair\n' +
                                                    '10. Komix\n' +
                                                    '\n' +
                                                    'Perlu diingat bahwa obat-obat tersebut mungkin tidak tersedia karena habis atau sedang dipinjam. Info lebih lanjut akan dihubungi setelah pengisian form peminjaman.'
                                                ),
                                template_message
                                ])
    elif event.postback.data == 'list_obat_satuan':
        buttons_template = ButtonsTemplate(
            text='Kembali ke pemilihan obat', actions= [
                PostbackTemplateAction(
                    label='Kembali', data='pilih_obat')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Kembali ke pemilihan obat', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[List Obat Satuan]\n' +
                                                    '\n' +
                                                    '1. Bioplacenton\n' +
                                                    '2. Thrombophob\n' +
                                                    '3. Counterpain Patch Hot\n' +
                                                    '4. Counterpain Cool\n' +
                                                    '5. Ethyl Chloride\n' +
                                                    '6. Rivanol\n' +
                                                    '7. Oxycan\n' +
                                                    '8. Imboost\n' +
                                                    '9. Sangobion\n' +
                                                    '10. Mylanta Cair\n' +
                                                    '11. Ranitidin Cair\n' +
                                                    '12. Fludane\n' +
                                                    '13. Spasminal\n' +
                                                    '14. Parasetamol\n' +
                                                    '15. Feminax\n' +
                                                    '16. Ibuprofen\n' +
                                                    '17. Oralit\n' +
                                                    '18. Sanadryl\n' +
                                                    '19. Komix\n' +
                                                    '20. Salbutamol Syrup\n' +
                                                    '\n' +
                                                    'Perlu diingat bahwa obat-obat tersebut mungkin tidak tersedia karena habis atau sedang dipinjam. Info lebih lanjut akan dihubungi setelah pengisian form peminjaman.'
                                                ),
                                template_message
                                ])
    elif event.postback.data == 'tft':
        buttons_template = ButtonsTemplate(
            title='Pastikan Anda telah memahami SOP di atas', text='Klik tombol di bawah untuk melanjutkan', actions= [
                PostbackTemplateAction(
                    label='Oke', data='form_tft')
                ]
            )
        template_message = TemplateSendMessage(
            alt_text='Pahamilah SOP', template=buttons_template)
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='[SOP TFT Medik]\n' +
                                                    '\n' +
                                                    '1. Maksimal permintaan TFT medik adalah H-5 dari hari pemberian TFT medik.\n' +
                                                    '\n' +
                                                    '2. Mengisi form yang telah disediakan.'
                                                ),
                                template_message
                                ])
    elif event.postback.data == 'form_tandu':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form Peminjaman Tandu]\n' + form_template
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'form_obat_base':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form Peminjaman Obat Base]\n' + form_template
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'form_obat_pj':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form Peminjaman Obat PJ Obat]\n' + form_template
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'form_obat_satuan':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form Peminjaman Obat Satuan]\n' + form_template + '\nObat yang ingin dipinjam : '
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'form_tft':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form TFT Medik]\n' +
                                                        '\n' +
                                                        'Nama : \n' +
                                                        'Jurusan : \n' +
                                                        'ID Line : \n' +
                                                        'Lembaga : \n' +
                                                        'Gambaran keberjalanan acara : \n' +
                                                        'List obat yang telah disediakan : \n' +
                                                        'Sasaran peserta TFT : \n' +
                                                        'Estimasi jumlah peserta TFT : \n' +
                                                        'Alokasi waktu TFT : \n' +
                                                        'Sarana dan prasarana yang telah disediakan : \n' +
                                                        'Lokasi TFT : '
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'form_humas':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text= '[Form Kontak]\n' +
                                                        '\n' +
                                                        'Nama : \n' +
                                                        'Jurusan : \n' +
                                                        'ID Line : \n' +
                                                        'Pesan : '
                                ),
                                TextSendMessage(text= 'Mohon isi form di atas dan pastikan form yang Anda isikan sudah benar\n' +
                                            'Form yang dikirim akan langsung dimasukkan ke dalam sistem'
                                )
            ])
    elif event.postback.data == 'ping':
        line_bot_api.reply_message(
            event.reply_token, [TextSendMessage(text='pong'),TextSendMessage(text='pong2')])
    elif event.postback.data == 'datetime_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
    elif event.postback.data == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))
    elif event.postback.data == 'time_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['time']))


@handler.add(BeaconEvent)
def handle_beacon(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                event.beacon.hwid, event.beacon.dm)))


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    # create tmp dir for download content
    make_static_tmp_dir()

    app.run(debug=options.debug, port=options.port)
