from pyrogram import Client


api_id = 19497935
api_hash = '66e9f0d151520594daed37ac891d44dc'
app = Client('my_account', api_id, api_hash)

app.start()
app.send_message(567077575, 'Настраиваю бота в телеграм')
app.stop()
