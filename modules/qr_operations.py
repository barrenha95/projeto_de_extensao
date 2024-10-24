import qrcode
from PIL import Image
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib

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

        return img
    
    def sending_qr(self, first, email):
        """
        This class was created send the QR Code to the desired email
        """

        msg = EmailMessage()

        # Headers
        msg['Subject'] = 'Gagos Beer Ticket'
        msg['From'] = 'GagoBeerAdmin <gago@beer.com.br>'
        msg['To'] = "'" + str(first) + '<' + str(email) + ">'"

        # the plain text body
        msg.set_content('Here is your ticket to the Gago Beer.')

        # now create a Content-ID for the image
        image_cid = make_msgid(domain='beer.com')

        msg.add_alternative("""\
        <html>
            <body>
                <p>Here is your ticket to the:<br>
                   GAGO BEER.
                </p>
                <img src="cid:{image_cid}">
            </body>
        </html>
        """.format(image_cid=image_cid[1:-1]), subtype='html')

        with open('outputs/qr_code.png', 'rb') as img:
            maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
            msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)
            
        username = str('yourMail@yahoo.com')  
        password = str('yourPassWord')  
  
        try :
            server = smtplib.SMTP("smtp.mail.yahoo.com",587)
            server.login(username,password)
            server.sendmail(fromMy, to,msg)
            server.quit()    
            print('ok the email has sent ')
        except :
            print('can\'t send the Email')
            
        

if __name__ == '__main__':
    
    qr = QrOperations()
    qr.generating_qr(first = 'qr', last = 'test', id5 = 11111)

    #pil_img = Image.open('outputs/qr_code.png', 'r')
    #pil_img.show()

    qr.sending_qr(first = 'qr', email='barrenha95@yahoo.com.br')