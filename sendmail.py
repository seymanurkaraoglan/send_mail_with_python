import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 


#The mail addresses and  password
sender_address = 'eynanur18@gmail.com'              
sender_pass = 'wvvrepigzszxegja'                                      

# list of reciver email_id to the mail 
li = ['melisacakicii@outlook.com','sudemkaraoglan11@gmail.com']                                                         
#[item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id


# getting length of list 
length = len(li) 
   
# Iterating the index 
# same as 'for i in range(len(list))' 

# Here we iterate the loop and send msg one by one to the reciver
for i in range(length): 
    
    X = li[i]
    reciver_mail = X
    
    print(reciver_mail)
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] =  reciver_mail             #  Pass Reciver Mail Address
    message['Subject'] =  'Sending mail with python'       #The subject line
     

    mail_content = '''This is a test mail'''
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    # open the file to be sent  
    filename = 'dene.txt'                                                    #str(input('Enter File Name With Extension To Attchment :- '))

    # Open PDF file in binary mode
    # The file is in the directory same as where you run your Python script code from 
    with open(filename, "rb") as attachment:
        # MIME attachment is a binary file for that content type "application/octet-stream" is used
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # encode into base64 
    encoders.encode_base64(part) 

    part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # attach the instance 'part' to instance 'message' 
    message.attach(part) 


    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.ehlo()
    s.login(sender_address, sender_pass) 
    text = message.as_string()
    s.sendmail(sender_address, reciver_mail, text) 
    s.quit() 

    print('Mail Sent')

# It Send Separated Mail one by one each receiver mail 
