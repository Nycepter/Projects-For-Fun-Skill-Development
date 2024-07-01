import smtplib
import random
import pandas
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os
from pydrive2.auth import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

# Service Account Authorization
service_account_key_file ="artemissender.json"
scope = ['https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_key_file, scope)
gauth = GoogleAuth()
gauth.credentials = credentials
drive = GoogleDrive(gauth)


#SMTP Info
my_email = "nycepter@gmail.com"
my_password = "wzgiirneenpphias"
 
# Drive Getting Photos-------------------------------------------
folder_id = '1tw_v59Mqep3oq52LPA0wVCk9D27n8Rsi'
file_list = drive.ListFile({
    'q': f"'{folder_id}' in parents and mimeType contains 'image/' and trashed=false"
}).GetList()
image_files = [(file['id'], file['title']) for file in file_list]

if not image_files:
    print("No images found in the folder.")
else:
    # Randomly Select An Image
    selected_image_id, selected_image_name = random.choice(image_files)
    print(f"Selected image: {selected_image_name}")

file = drive.CreateFile({'id': selected_image_id})
file.GetContentFile(selected_image_name)
# --------------------------------------------------------

# Email Details
from_email = 'nycepter@gmail.com'
to_email = ''
subject = 'Daily Picture Of Artemis'

# Functions
def send_email(email):
    with  smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, email, msg.as_string())

#CSV file
data = pandas.read_csv("people.csv")
people_dict = {(data_row["email"]): data_row for (index, data_row) in data.iterrows()}

# Any True Statement
if 2 == 2:
    for email, person_data in people_dict.items():

        # Email Container
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attaching Image
        with open(selected_image_name, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {selected_image_name}',
            )
            msg.attach(part)

        #Body Text
        file_path = "letter_1.txt"
        with open(file_path, 'r') as letter_file:
            contents = letter_file.read()
            body = contents.replace("[NAME]", person_data["name"])
            msg.attach(MIMEText(body, 'plain'))
        send_email(email)

#Delete Photo After Sending
if os.path.exists(selected_image_name):
    os.remove(selected_image_name)
    print(f"Deleted the file: {selected_image_name}")
else:
    print(f"The file {selected_image_name} does not exist.")



