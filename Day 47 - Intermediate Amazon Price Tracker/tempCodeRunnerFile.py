
price_line = soup.find("span", class_="a-price-whole") 
print(price_line)
item_price = [price.getText() for price in price_line]
final_price = item_price.split("$")[1]
floating_price = float(final_price)
print(final_price)

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