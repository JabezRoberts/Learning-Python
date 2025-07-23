import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "abcd123"

# Create a new SMTP object to allow connection
connection = smtplib.SMTP("smtp.gmail.com") # Location of SMTP's email provider (Gmail)

#after creating connection create start tls - Transport Layer Security --> securing email connections
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com", msg="Subject:Hello \n\nThis is the body of the email")
connection.close()

# How to avoid needing to write connection.close()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="appbrewerytesting@yahoo.com", msg="Subject:Hello \n\nThis is the body of the email")