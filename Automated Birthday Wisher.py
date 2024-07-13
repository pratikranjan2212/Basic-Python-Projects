import pandas as pd
import datetime
import smtplib

# Entering authentication details
EMAIL_ID = ""
EMAIL_PASSWD = ""

# Function to send email
def SendEmail(to, sub, message):
    print(f"Email to {to} sent with subject: {sub} and message: {message}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(EMAIL_ID, EMAIL_PASSWD)
    s.sendmail(EMAIL_ID, to, f"Subject: {sub}\n\n{message}")
    s.quit()
     
# Main function
if __name__ == '__main__':
    df = pd.read_excel('data.xlsx')
    today = datetime.datetime.now().strftime('%d-%m')
    yearNow = datetime.datetime.now().strftime('%Y')
    writeInd = []

    # Iterating through the data
    for index, item in df.iterrows():
        #print(index, item['Birthday'])
        bday = item['Birthday'].strftime('%d-%m')
        message = "Wish you a very happy birthday with lots of love and happiness. May you have a great year ahead!"
        if today == bday and yearNow not in str(item['Year']):
            SendEmail(item['Email'], "Happy Birthday", message)
            writeInd.append(index)

# Updating the data
for i in writeInd:
    yr = df.loc[i, 'Year']
    df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)

# Saving the data
df.to_excel('data.xlsx', index=False)