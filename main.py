import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = Your Email
MY_PASSWORD = Your Password
SEND_TO = Your Email

amazon_product_url = "https://www.amazon.com/Backbone-Mobile-Gaming-Controller-PlayStation-iOS/dp/B09ZXTRKQ9/ref=sr_1_18?qid=1672677143&s=electronics&sr=1-18&th=1"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/108.0.0.0 Safari/537.36"
}

response = requests.get(url=amazon_product_url, headers=header)
# print(response.text)
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price_tag = soup.find(id="priceblock_ourprice").getText()
# print(price_tag)
price_without_currency = price_tag.split("$")[1]
# print(price_without_currency)
float_price = float(price_without_currency)
# print(float_price)
product_title = soup.find(id="productTitle").getText()
# half_product_title = product_title.split()[:9]

if float_price < 120:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_TO, msg=f"Subject:Amazon price alert: {product_title}"
                            f" is now {float_price} buy from here\n {amazon_product_url}".encode('utf-8'))



