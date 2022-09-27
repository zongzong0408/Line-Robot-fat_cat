from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os

API = "1z/vjWAX0dcEXGP29xQ43Xcr60RHlQjjEDKWNcAONdzwnTYFabgHoJX1ZJC6EDZ04QLc6Azf2HxnQgbGJstU2n9LSMZf6s1iGSY7enqKeo4CZSpV72zaU0VdGTdTD1kRl9vp+Utti3jCIuW+iUgATAdB04t89/1O/w1cDnyilFU="
SECRET = "bf22c97b07a9cc7e3134b23e52c21a58"
USER_ID = "Ued51038c26c9278c4789676bfe2eb215"

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(API)
# Channel Secret
handler = WebhookHandler(SECRET)
# User ID
line_bot_api.push_message(USER_ID, TextSendMessage(text = "Line Bot 'fat_cat' is starting."))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text = True)

    app.logger.info("Request body : " + body)

    # handle webhook body
    try:

        handler.handle(body, signature)

    except InvalidSignatureError:

        abort(200)

    return 'OK'

 
# 訊息傳遞區塊
"""
    基本上程式編輯都在這個 function
"""
@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

"""
    Main Function Start...
"""
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)