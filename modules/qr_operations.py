import qrcode
import os
from PIL import Image
from email.message import EmailMessage
from email.utils import make_msgid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class QrOperations:
    """
    This class was created to center all operations related to QR Code
    
    Operations:
    - Creation of personalized QR Code given an input
    - [Debug purpose] Reading of a QR Code checking if it works properly
    """

    def generating_qr(self, first, last, id5):
        
        # Create a QR code object with a larger size and higher error correction
        qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

        # Define the data to be encoded in the QR code
        data = "http://127.0.0.1:5000/auth/" + str(first) + "/" + str(last) + "/" + str(id5)

        # Add the data to the QR code object
        qr.add_data(data)

        # Make the QR code
        qr.make(fit=True)

        # Create an image from the QR code with a black fill color and white background
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        img.save("outputs/qr_code.png")

        #return img
    
    def sending_qr(self, first, email):
        """
        This class was created send the QR Code to the desired email
        """

        username = str('email_used_to_send_qr_code')  
        password = str('my_pwd')  

        msg = MIMEMultipart()
        msg['From'] = username 
        msg['To']   = email
        msg['Subject'] ='TheSubject'

        
        text=MIMEText('Olá ' + str(first) + ' aqui está seu ingresso para a Gago Beer.')
        msg.attach(text)

        with open('outputs/qr_code.png', 'rb')as f:
            img_data = f.read()

        image = MIMEImage(img_data)
        msg.attach(image)

        try :
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            server.starttls() 
            server.login(username,password)
            server.sendmail(msg['From'], msg['To'],msg.as_string())
            server.quit()    
            print('ok the email has sent ')
        except :
            print('can\'t send the Email')
            
        

if __name__ == '__main__':
    
    qr = QrOperations()
    qr.generating_qr(first = 'qr', last = 'test', id5 = 11111)

    #pil_img = Image.open('outputs/qr_code.png', 'r')
    #pil_img.show()

    qr.sending_qr(first = 'qr', email='email_i_want_to_send')