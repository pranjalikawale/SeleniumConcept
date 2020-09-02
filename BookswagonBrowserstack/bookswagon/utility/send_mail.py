import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from utility.xls_util import XlsUtility
from utility.custom_logger import CustomLogger
from exception.bookswagon_exception import BookswagonException

class SendMail():

    def sent_email_report(self,path,sheet,report):
        try:
            data=[]
            data=XlsUtility.read_data_from_sheet(path,sheet)
            email_user = data[0]
            email_password = data[1]
            email_send = data[2]

            subject = 'Test Report for Capsulecrm'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            body = 'Hi there, sending this email from report!'
            msg.attach(MIMEText(body,'plain'))
            attachment =open(report,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+report)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)

            server.sendmail(email_user,email_send,text)
            server.quit()
        except:
            log=CustomLogger.log_utility()
            log.error("Mail not sent")
            raise BookswagonException("Mail not sent","Mail_Not_Sent")
            