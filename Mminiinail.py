from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    ImageSendMessage,LocationSendMessage
)

app = Flask(__name__)

# 請替換為你自己的 Channel Access Token 與 Secret
line_bot_api = LineBotApi('Token')
handler = WebhookHandler('Secret')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text

    if mtext == "@預約時間": #如果消息為特定命令
        try:
            message = TextSendMessage(text="🐬六月份可預約時間🐬\n6/10 13:00 18:00\n6/11 13:00 18:00\n6/13 13:00 18:00\n6/15 18:00\n6/17 13:00 18:00\n6/18 18:\n6/19 18:00\n6/21 13:00 18:00\n6/23 18:00\n6/25 13:00 18:00\n6/27 13:00 18:00\n6/28 13:00 18:00")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤！"))

    elif mtext == "@作品集": #如果消息為作品集命令
        try:
            message = ImageSendMessage(
                original_content_url="https://u.fmyeah.com/i111/68411cd07d32b.jpg",
                preview_image_url="https://u.fmyeah.com/i111/68411cd07d32b.jpg"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤！"))

    elif mtext == "@預約": #如果消息為預約命令
        try:
            message = TextSendMessage(text="🐬預約請填寫以下表格🐬\n真實姓名：\n聯絡電話：\n預約日期及時間：\n欲施作項目：\n是否需卸甲：\n⤷可先提供欲施作的造型圖.ᐟ")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤！"))

    elif mtext == "@注意事項": #如果消息為注意事項
       try:
           message = TextSendMessage(text="🐬注意事項🐬\n我是目前還在學的大學生，也正在努力練習美甲中，以下是一些小提醒，希望您可以理解跟包容🥺💗\n🐬地點在景美捷運站出來搭車約15分鐘，或從萬芳醫院捷運站搭車約10分鐘，會再提供詳細地點喔！\n🐬 因為還是新手，在剪死皮的時候有可能會有一點點小出血（我會非常小心處理！）\n🐬持久度方面可能沒辦法跟專業美甲師一樣，但一般情況下可以維持差不多一個月左右～")
           line_bot_api.reply_message(event.reply_token, message)
       except:
           line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤！"))

    elif mtext == "@地點": #如果消息為傳送位置命令
        try:
            message = LocationSendMessage(
                title='Mminiinail',
                address='116台北市文山區木柵路二段161巷',
                latitude=24.98861,
                longitude=121.56333
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="發生錯誤！"))



if __name__ == "__main__":
    app.run()



if __name__ == "__main__":
    app.run()
