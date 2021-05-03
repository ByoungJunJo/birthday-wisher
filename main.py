import datetime as dt
import pandas as pd
import smtplib
import random
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv => Go into the birthdays.csv and edit it

# 2. Check if today matches a birthday in the birthdays.csv
# Use the datetime module to obtain the current day of the week
now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv("birthdays.csv")
# Use dictionary comprehension to create a dictionary from birthday.csv
birthdays_dict = {(df_row.month, df_row.day): df_row for (index, df_row) in df.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]["name"]
    birthday_email = birthdays_dict[today]["email"]

    with open(file_path) as letter:
        contents = letter.read()
        contents_with_name = contents.replace("[NAME]", birthday_person)

        # 4. Send the letter generated in step 3 to that person's email address
        # ***WARNING***:
        # Make sure you use a dummy email account to test this out!
        my_email = "YOUR_EMAIL"
        password = "YOUR_EMAIL_PASSWORD"

        with smtplib.SMTP("YOUR_EMAIL_PROVIDERS_SMTP_ADDRESS", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            # Write messages
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_email,
                msg=f"Subject:Happy Birthday, {birthday_person}!\n\n{contents_with_name}"
            )






