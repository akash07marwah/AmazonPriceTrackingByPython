import requests 
from bs4 import BeautifulSoup
import smtplib
import time
#############################################################

URL = 'https://www.amazon.in/gp/product/1119576156/ref=ox_sc_act_title_9?smid=A1S46CEHK621UY&psc=1'
desired_price = 3500
times = 1440

#############################################################
time_interval=86400/times
converted_price=0
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'  }
def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="soldByThirdParty").get_text()
    global converted_price
    converted_price = price[3:8]
    converted_price = converted_price.split(',')
    converted_price = ("".join(converted_price))
    converted_price = float(converted_price)

    print(title.strip())
    print(converted_price)
    global desired_price
    if(converted_price<desired_price):
        send_mail()
    

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('akashmarwah07@gmail.com','stupid-string-egan')

    subject = 'Price fell down to {converted_price}'
    body = "Check the Amazon link https://www.amazon.in/gp/product/1119576156/ref=ox_sc_act_title_9?smid=A1S46CEHK621UY&psc=1"

    msg = "Subject:Price fell down to "+ str(converted_price)  +"\n\n Check the Amazon link https://www.amazon.in/gp/product/1119576156/ref=ox_sc_act_title_9?smid=A1S46CEHK621UY&psc=1"
    server.sendmail(
        'akashmarwah07@gmail.com',
        'akashmarwah07@gmail.com',
        msg
    )    
    print('Email Sent')
    server.quit()



while(True):
        check_price()
        global time_interval
        time.sleep(time_interval)
