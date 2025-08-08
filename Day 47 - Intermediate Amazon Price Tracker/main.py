import requests
from bs4 import BeautifulSoup
import smtplib

MY_SMTP_ADDRESS="test@mail.com"
MY_EMAIL = "test2@mail.com"
MY_PASSWORD = "asdtn3we54hj35"

URL = "https://www.amazon.com/SAMSUNG-Mini-LED-FreeSync-Adjustable-LS55CG970NNXGO/dp/B0CDQKYXTC/ref=sr_1_18?crid=1I86ICJ2QBW1F&dib=eyJ2IjoiMSJ9.O-E0P_q5rh56RljQEB5lTl45Erf-EUowmcRBJuPGq-7vV6iitXYUleJ9uJEBkHi7kcPuwmeBvXvz5fn-efHi0PAtU5oDsSZO2Wroir5NKixzGvPAXuGu7NdpPAOVHUf-x6CsL4g0gtkQJn-TA6K3CbMvQLN2f8vWiWjadLrVyPzJrZieRjd-EL11PvamXkTvA0-gYMsm8RSwevpi95hNG6hjSwaHFRrx1jEthJoAvAk.YiplfGtNKmnN7_idUo9D8F3YzPQQW4nHNHBolgozfjg&dib_tag=se&keywords=55+in+curved+tv&qid=1754660910&sprefix=55+in+cu,aps,151&sr=8-18"

# Set the price below which you would like to get a notification
BUY_PRICE = 2000


MY_HEADERS = {
        "sec-ch-ua-platform" : "Windows",
        "upgrade-insecure-requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site" : "cross-site",
        "sec-fetch-mode" : "navigate",
        "sec-fetch-user" : "?1",
        "sec-fetch-dest" : "document",
        "Accept-Encoding":"gzip, deflate, br, zstd",
        "Accept-Language" : "en-US,en;q=0.9",
        "priority" : "u=0, i",
        "Cookie" : "PHPSESSID=09bf8378396532a6b6290c7ed0649a40",
        "x-forwarded-proto" : "https",
        "x-https" : "on"
    }


# Write your code below this line 👇
response = requests.get(URL, headers = MY_HEADERS)
website_html = response.text

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price_line = soup.find("span", class_="a-price-whole").getText() 
print(price_line)
# item_price = [price.getText() for price in price_line]
# final_price = item_price.split("$")[1]
floating_price = float(price_line)
print(floating_price)

title = soup.find(id="productTitle").get_text().strip()
print(title)


if floating_price < BUY_PRICE:
    message = f"{title} is on sale for {price_line}!"

    with smtplib.SMTP(MY_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_SMTP_ADDRESS,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )