import os

from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv

load_dotenv()

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

AMAZON_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.in/dp/B0DW47XR3X/ref=QAHzEditorial_en_IN_5?pf_rd_r=2DRV6E5ZK0JP3XRWFESR&pf_rd_p=9602344e-de25-4783-bc7f-eb9c112163d2&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-11&pf_rd_t=&pf_rd_i="
response = requests.get(LIVE_URL,headers=header)
data = response.text

soup = BeautifulSoup(data,"html.parser")

# price = soup.find("span",class_="a-price-whole")
price = float(soup.find(class_="a-offscreen").get_text().split("₹")[1].replace(",",""))
title = soup.find(id="productTitle").getText().strip()
l_price: float = 30000

email = os.environ["email"]
password = os.environ["APP_PASSWORD"]

if price < l_price:
    message = f"{title} is on sale prize {price}"
    print(message)
    with smtplib.SMTP ("smtp.gmail.com",port=587)  as con:
        con.starttls()
        con.login(user=email,password=password)
        message = con.sendmail(
            from_addr =os.environ["email"],
            to_addrs="mohamedyasin@voicesnap.com",
            msg=f"Subject:{title} Price drop\n\n{message}\nURL : {LIVE_URL}"
        )
        print(message)

