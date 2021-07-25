##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv("birthdays.csv", dtype={"month": int, "day": int}, squeeze=True).to_dict(orient='records')
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

for i in data:
    if i['month'] == today_month and i['day'] == today_day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as fp:
            letter = fp.read()
            letter = letter.replace("[NAME]", '123')
# 4. Send the letter generated in step 3 to that person's email address.
            MY_EMAIL = "x"
            MY_PASSWORD = "x"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=i["email"],
                    msg=f"Subject:Happy Birthday\n\n{letter}"
                )

