from email import message
import smtplib
import datetime as dt
import random
import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
account_id = "*******************************"
auth_token = "*******************************"
my_twilio_number = "+................."

from_my_email = ".........................@yahoo.com"
from_my_password = "********************"
to_mail_addr =".......................@gmail.com"

now= dt.datetime.now()
weekday = now.weekday()

def pick_motivate():
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quotes = random.choice(all_quotes)
    
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
    
        connection.login(user=from_my_email, password=from_my_password)
        connection.sendmail(from_addr=from_my_email,
                             to_addrs=to_mail_addr,
                             msg=f"Subject:Motivation \n\n{quotes}")

if weekday == 0:
    pick_motivate()
elif weekday == 1:
    pick_motivate()
elif weekday == 2:
    pick_motivate()
elif weekday == 3:
    pick_motivate()
elif weekday == 4:
    pick_motivate()
elif weekday == 5:
    pick_motivate()
else:
    pick_motivate()
    

    






