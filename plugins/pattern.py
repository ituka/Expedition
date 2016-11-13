from time import sleep
from slackbot.bot import respond_to

@respond_to('コーヒー')
def cofee(message):
    message.reply('少々お待ちを')
    sleep(15)
    message.reply('どうぞ')

#長距離練習航海
@respond_to('長距離練習航海')
@respond_to('長距離')
@respond_to('長')
def t(message):
    message.reply('やりました。')
    sleep(60*30)
    message.reply('作戦完了。艦隊が帰投します。')

#海上護衛任務
@respond_to('海上護衛任務')
@respond_to('海上護衛')
@respond_to('海')
def t(message):
    message.reply('やりました。')
    sleep(60*90)
    message.reply('作戦完了。艦隊が帰投します。')

#防空射撃演習
@respond_to('防空射撃演習')
@respond_to('防空射撃')
@respond_to('防空')
def t(message):
    message.reply('やりました。')
    sleep(60*40)
    message.reply('作戦完了。艦隊が帰投します。')

#タンカー護衛任務
@respond_to('タンカー護衛任務')
@respond_to('タンカー')
def t(message):
    message.reply('やりました。')
    sleep(60*240)
    message.reply('作戦完了。艦隊が帰投します。')

#ボーキサイト輸送任務
@respond_to('ボーキサイト輸送任務')
@respond_to('ボーキサイト')
@respond_to('ボーキ')
def t(message):
    message.reply('やりました。')
    sleep(60*300)
    message.reply('作戦完了。艦隊が帰投します。')

#北方鼠輸送作戦
@respond_to('北方鼠輸送作戦')
@respond_to('鼠輸送')
@respond_to('北方')
def t(message):
    message.reply('やりました。')
    sleep(60*140)
    message.reply('作戦完了。艦隊が帰投します。')

#東京急行
@respond_to('東京急行')
@respond_to('東京弌')
@respond_to('東弌')
def t(message):
    message.reply('やりました。')
    sleep(60*165)
    message.reply('作戦完了。艦隊が帰投します。')

#東京急行（弐）
@respond_to('東京急行（弐）')
@respond_to('東京（弐）')
@respond_to('東（弐）')
def t(message):
    message.reply('やりました。')
    sleep(60*175)
    message.reply('作戦完了。艦隊が帰投します。')
